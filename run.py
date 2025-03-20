#!/usr/bin/env python
"""
Launcher script for the Spam Detector application.
This script makes it easier to run the app from the root directory.
"""

import sys
import os

if __name__ == "__main__":
    # Add the current directory to the path so the imports work correctly
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    # Import and run the Flask app
    from src.app import app
    
    app.run(debug=False, host='0.0.0.0', port=5000) 