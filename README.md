# Vortex AI
Vortex AI is a voice-controlled virtual assistant developed in Python that integrates speech recognition, text-to-speech conversion, web automation, and AI-based responses to perform tasks such as browsing websites, playing music, fetching news, and answering queries.

### Features
  • Speech Recognition: Utilizes the SpeechRecognition library to interpret voice commands.​
  • Text-to-Speech: Employs pyttsx3 for converting text responses into speech.​
  • Web Automation: Opens popular websites like YouTube, Facebook, LinkedIn, and Google based on voice commands.​
  • Music Playback: Plays songs from a predefined library using the musicLib module.​
  • News Fetching: Retrieves and reads out the latest news headlines using the NewsAPI.​
  • AI Responses: Handles general queries by interfacing with the OpenAI API to generate intelligent responses.​

### Installation
1. Clone the Repository:
      git clone https://github.com/yourusername/vortex-ai.git
2. Navigate to the Project Directory:
      cd vortex-ai
3. Install the Required Dependencies:
      pip install -r requirements.txt
### Configuration
1. API Keys:
  • OpenAI API Key: Obtain from OpenAI and set it as an environment variable named OPENAI_API_KEY.​
  • NewsAPI Key: Acquire from NewsAPI and set it as an environment variable named NEWSAPI_KEY.​
2. Music Library:
Ensure the musicLib module contains a dictionary named music mapping song names to their respective URLs.​

### Usage
1. Run the Application:
      python vortex_ai.py
2. Activate Vortex AI:
      Say "Vortex" to initiate the assistant.​

### Issue Commands:
Use voice commands such as:​
      • "Open YouTube"
      • "Play [song name]"
      • "What's the news?"
      •  General questions for AI responses.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.​

### Acknowledgments
    • SpeechRecognition​
    • pyttsx3​
    • OpenAI API​
    • NewsAPI
