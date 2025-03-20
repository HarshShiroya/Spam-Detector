from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import joblib
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import re
from werkzeug.exceptions import HTTPException
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Load the trained model
try:
    model = joblib.load('src/models/spam_classifier_model.pkl')
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Error loading model: {str(e)}")
    raise

# Preprocessing function for text
def preprocess_text(text):
    # Input validation
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    if len(text.strip()) == 0:
        raise ValueError("Input cannot be empty")
    
    if len(text) > 10000:  # Maximum length check
        raise ValueError("Input text is too long")
    
    # Normalize text: lower case and remove punctuation
    text = text.lower()
    text = re.sub(r'[\W_]+', ' ', text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@limiter.limit("10 per minute")  # Rate limit for spam detection endpoint
def predict():
    try:
        # Get input message from the form
        message = request.form.get('message')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Log the request
        logging.info(f"Received prediction request from {request.remote_addr}")
        
        # Preprocess the input message
        preprocessed_message = preprocess_text(message)
        
        # Predict with the loaded model
        prediction = model.predict([preprocessed_message])[0]
        
        # Convert prediction to string ('Spam' or 'Not Spam')
        prediction_label = 'Spam' if prediction == 1 else 'Not Spam'
        
        # Log the prediction
        logging.info(f"Prediction made: {prediction_label}")
        
        return jsonify({'prediction': prediction_label})
    
    except ValueError as e:
        logging.warning(f"Validation error: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    logging.error(f"HTTP error: {str(e)}")
    return jsonify({
        "error": e.description,
        "code": e.code
    }), e.code

@app.errorhandler(Exception)
def handle_generic_exception(e):
    logging.error(f"Unexpected error: {str(e)}")
    return jsonify({
        "error": "An unexpected error occurred",
        "code": 500
    }), 500

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode in production
