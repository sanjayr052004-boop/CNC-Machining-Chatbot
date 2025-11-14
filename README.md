# CNC Machining Chatbot

An intelligent AI-powered chatbot designed to answer questions and provide guidance on CNC (Computer Numerical Control) machining. This chatbot helps users understand CNC operations, troubleshoot issues, and learn best practices.

## Features

- **AI-Powered Responses**: Uses natural language processing to understand CNC-related queries
- **Comprehensive Knowledge Base**: Covers topics including:
  - CNC machine types and components
  - Tool selection and management
  - Feed rates and spindle speeds
  - CNC programming basics (G-code, M-code)
  - Troubleshooting common issues
  - Safety protocols
  - Material selection and machining strategies
- **Web-Based Interface**: Easy-to-use chat interface accessible from any browser
- **Real-time Responses**: Get instant answers to your CNC-related questions
- **Open Source**: Fully transparent and customizable codebase

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/NLP**: NLTK, scikit-learn
- **Database**: JSON-based knowledge base

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sanjayr052004-boop/CNC-Machining-Chatbot.git
   cd CNC-Machining-Chatbot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the chatbot**:
   ```bash
   python app.py
   ```

5. **Access the chatbot**:
   Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
CNC-Machining-Chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── chatbot/
│   ├── __init__.py
│   ├── engine.py         # Core chatbot logic
│   ├── knowledge_base.py # Knowledge base management
│   └── nlp_utils.py      # NLP utilities
├── knowledge/
│   └── cnc_knowledge.json # CNC knowledge base
├── static/
│   ├── css/
│   │   └── style.css     # Chatbot styling
│   └── js/
│       └── script.js     # Frontend logic
└── templates/
    └── index.html        # Web interface
```

## Usage

### Starting the Chatbot

1. Run the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`

3. Start asking CNC-related questions in the chat interface

### Example Questions

- "What are the different types of CNC machines?"
- "How do I select the right cutting tool?"
- "What is a reasonable feed rate for aluminum?"
- "How do I troubleshoot tool chatter?"
- "Explain G-code basics"
- "What are safety precautions for CNC machines?"

## Knowledge Base

The chatbot's knowledge is stored in `knowledge/cnc_knowledge.json`. You can extend it by:

1. Adding new Q&A pairs
2. Updating existing responses
3. Categorizing questions by topic

Format:
```json
{
  "topics": {
    "machines": [
      {
        "question": "What are the types of CNC machines?",
        "answer": "CNC machines include..."
      }
    ]
  }
}
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Improvement

- Expand the knowledge base with more CNC topics
- Improve response accuracy with machine learning models
- Add multi-language support
- Implement database storage (SQLite/PostgreSQL)
- Create mobile app version
- Add image/video support in responses

## Deployment

### Deploying to Heroku

1. Create a `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Deploying to AWS/GCP

See deployment guides in the documentation folder.

## Customization

### Adding Custom Responses

Edit `knowledge/cnc_knowledge.json` and add your Q&A pairs.

### Changing Styling

Modify `static/css/style.css` to customize the chatbot appearance.

### Adjusting Behavior

Update parameters in `config.py` or `chatbot/engine.py`.

## API Reference

### POST /api/chat

Send a message to the chatbot.

**Request**:
```json
{
  "message": "Your question here"
}
```

**Response**:
```json
{
  "response": "Chatbot's answer",
  "confidence": 0.85,
  "topic": "machines"
}
```

## Troubleshooting

### Issue: Port 5000 already in use
**Solution**: Change the port in `app.py` or kill the process using that port.

### Issue: Module not found errors
**Solution**: Make sure your virtual environment is activated and run `pip install -r requirements.txt`

### Issue: Chatbot not responding
**Solution**: Check that the knowledge base file exists and is properly formatted JSON.

## Future Enhancements

- Integration with CNC machine APIs
- Real-time machine monitoring
- Integration with CAM software
- Advanced analytics and user insights
- Voice interface support
- Integration with maintenance systems

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

- **GitHub**: [sanjayr052004-boop/CNC-Machining-Chatbot](https://github.com/sanjayr052004-boop/CNC-Machining-Chatbot)
- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Join discussions on GitHub Discussions

## Acknowledgments

- NLTK and scikit-learn libraries for NLP capabilities
- Flask framework for web development
- The open-source community for continuous support

## Disclaimer

This chatbot is designed for educational and informational purposes. Always consult official CNC machine manuals, qualified professionals, and follow industry standards for actual machining operations. The authors are not responsible for any damages or injuries resulting from the use of this chatbot.

---

**Last Updated**: November 2025
**Version**: 1.0.0
