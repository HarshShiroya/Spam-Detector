# Spam Detector

A machine learning-based web application that detects spam messages using Natural Language Processing (NLP) techniques.

## Features

- Real-time spam detection
- User-friendly web interface
- Pre-trained machine learning model
- Text preprocessing with NLTK
- RESTful API endpoint
- Rate limiting and security features

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spam-detector.git
cd spam-detector
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

You can run the application in two ways:

1. Using the run script (recommended):
```bash
python run.py
```

2. Or directly with the Flask application:
```bash
python src/app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

4. Enter a message in the text input field and click "Check for Spam" to get the prediction.

## Project Structure

```
spam-detector/
├── data/                  # Dataset storage
│   └── SPAM Data.csv      # Training dataset
├── logs/                  # Application logs (created on startup)
│   └── app.log            # Generated log file
├── src/                   # Source code
│   ├── __init__.py        # Package initialization
│   ├── app.py             # Main Flask application
│   ├── models/            # Machine learning models
│   │   ├── __init__.py    # Package initialization
│   │   └── spam_classifier_model.pkl  # Trained model
│   ├── static/            # Static web files
│   │   ├── style.css      # CSS styling
│   │   └── script.js      # Frontend JavaScript
│   ├── templates/         # HTML templates
│   │   └── index.html     # Main application page
│   └── utils/             # Utility scripts
│       ├── __init__.py    # Package initialization
│       └── spam_detector.ipynb  # Model training notebook
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── run.py               # Application launcher script
```

## Security Features

The application includes several security measures:

- Rate limiting to prevent abuse
- Input validation and sanitization
- Comprehensive error handling
- Request logging and monitoring
- Secure file access

## Model Details

The spam detection model is trained using scikit-learn and includes the following features:
- Text preprocessing (lowercase conversion, punctuation removal)
- Stop word removal
- TF-IDF vectorization
- Classification using scikit-learn

## API Endpoints

### POST /predict
Predicts whether a given message is spam or not.

**Request:**
- Content-Type: application/x-www-form-urlencoded
- Body: `message`: The text message to classify

**Response:**
```json
{
    "prediction": "Spam" | "Not Spam"
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset: [SPAM Data.csv]
- Libraries: scikit-learn, NLTK, Flask, Flask-Limiter 