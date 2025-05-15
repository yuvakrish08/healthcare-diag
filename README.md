# Healthcare AI Chatbot

A simple healthcare chatbot that provides basic medical information and preliminary symptom analysis. This chatbot is designed to help users understand common symptoms and receive general health recommendations.

## ⚠️ Disclaimer

This chatbot is for informational purposes only and is not a replacement for professional medical advice. Always consult with a qualified healthcare provider for medical diagnosis and treatment.

## Features

- Modern, responsive chat interface
- Basic symptom analysis
- General health recommendations
- Easy-to-use web interface

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository or download the files

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Type your symptoms or health-related questions in the chat input
2. Press Enter or click the Send button
3. The chatbot will analyze your input and provide relevant information and recommendations

## Project Structure

```
├── app.py              # Main Flask application
├── medical_kb.json     # Medical knowledge base
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    └── index.html     # Main HTML template
```

## Customization

You can extend the chatbot's knowledge by adding more entries to the `medical_kb.json` file. Each entry should include:
- Keywords: Terms to match in user input
- Response: Appropriate medical information and recommendations

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 