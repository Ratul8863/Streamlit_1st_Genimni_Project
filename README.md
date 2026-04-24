# NoteVision AI 🧠

A powerful AI-powered application that transforms your study notes into interactive learning materials using Google Gemini API.

## Features 🚀

- **AI-Powered Note Analysis**: Extract key topics from note images using Google Gemini 2.0 Flash
- **Smart Summaries**: Get concise bullet-point summaries of your notes
- **Quiz Generation**: Automatically create quizzes based on your study materials
- **Text-to-Speech**: Convert note summaries to audio for on-the-go learning
- **Beautiful UI**: Modern, dark-themed Streamlit interface with smooth interactions

## Technologies Used 💻

- **Frontend**: Streamlit 1.56.0
- **AI Model**: Google Gemini 2.0 Flash API
- **Image Processing**: Pillow (PIL)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Language**: Python 3.x
- **Environment Management**: Virtual Environment

## Prerequisites ✅

Before you start, make sure you have:

1. **Python 3.8 or higher** installed on your system
2. **Git** (optional, for cloning the repository)
3. **Google Gemini API Key** ([Get it here](https://aistudio.google.com/apikey))
4. A text editor or IDE (VS Code, PyCharm, etc.)

## Installation & Setup 📋

Follow these steps to get the application running:

### Step 1: Navigate to the Project Directory

```bash
cd project
```

### Step 2: Set Up the Virtual Environment

The project includes a pre-configured virtual environment in the `project1` folder. Activate it:

**On Windows (PowerShell):**
```bash
./project1/Scripts/Activate.ps1
```

**On Windows (Command Prompt):**
```bash
project1\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source project1/bin/activate
```

### Step 3: Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requiremnet.txt
```

Or manually install packages:

```bash
pip install streamlit google-genai pillow python-dotenv gtts
```

### Step 4: Set Up Your Google Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy your API key

The `.env` file is already included in this folder. Just update it with your API key:

**File: `.env`**
```
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### Step 5: Run the Application

From the project directory, start the Streamlit app:

```bash
streamlit run ../StreamLit/app.py
```

Or if you have a local copy of the app, run it directly:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## How to Use 👨‍💻

1. **Upload Notes**: Click the file uploader to select images of your notes
2. **Extract Key Topics**: The app will automatically analyze the images using AI
3. **View Summary**: Get a concise bullet-point summary of key topics
4. **Generate Quiz**: Create a 3-question quiz to test your understanding
5. **Listen to Audio**: Convert any content to audio for portable learning

## Project Structure 📁

```
project/
├── README.md              # This file
├── api_calling.py         # AI API functions (Gemini integration)
├── app.py                 # Streamlit application
├── audio.py               # Text-to-speech utilities
├── requiremnet.txt        # Python dependencies
├── .env                   # API keys configuration
└── project1/              # Virtual environment
    ├── Scripts/           # Activation scripts
    ├── Lib/               # Installed packages
    ├── Include/           # Header files
    └── ...
```

## Key Files Description 📄

- **`api_calling.py`**: Contains functions for:
  - `genarate_note()` - Extracts topics from images
  - `genarate_audio()` - Converts text to speech
  - `genarate_quiz()` - Generates quiz questions

- **`app.py`**: Streamlit frontend with custom CSS styling and UI components

- **`audio.py`**: Example text-to-speech implementation

- **`requiremnet.txt`**: Complete list of Python package dependencies

## Troubleshooting 🔧

### Issue: "Module not found" errors
**Solution**: Make sure the virtual environment is activated and all dependencies are installed.
```bash
# Verify venv is active (you should see (project1) in your terminal)
pip list  # Check if packages are installed
```

### Issue: "API Key not found" error
**Solution**: Verify that `.env` file exists in the project folder with the correct API key format.
```bash
cat .env  # View .env contents (don't share your API key!)
```

### Issue: Port 8501 already in use
**Solution**: Run with a different port:
```bash
streamlit run ../StreamLit/app.py --server.port 8502
```

### Issue: Image upload not working
**Solution**: Make sure Pillow is installed:
```bash
pip install pillow
```

### Issue: Virtual environment won't activate
**Solution**: Recreate it:
```bash
python -m venv project1
pip install -r requiremnet.txt
```

## Dependencies 📦

Key packages used in this project:

- **streamlit** - Web application framework
- **google-genai** - Google Gemini API client
- **pillow** - Image processing
- **python-dotenv** - Environment variable management
- **gtts** - Google Text-to-Speech
- **numpy** - Numerical computing
- **pandas** - Data manipulation

See `requiremnet.txt` for the complete list with versions.

## API Limits ⚠️

Be aware of Google Gemini API rate limits:
- Free tier has daily quotas
- Monitor your API usage in [Google AI Studio](https://aistudio.google.com/)
- Each request counts toward your daily limit

## Future Enhancements 🎯

- [ ] Support for multiple note formats (PDF, handwriting OCR)
- [ ] Spaced repetition study system
- [ ] Note organization and tagging
- [ ] Export summaries and quizzes as PDFs
- [ ] Multi-language support
- [ ] Offline mode support

## Support 💬

For issues or questions:
1. Check the Troubleshooting section above
2. Review [Google Gemini API documentation](https://ai.google.dev/docs)
3. Check [Streamlit documentation](https://docs.streamlit.io/) for UI-related questions
4. Verify your API key is valid and has not expired

---

**Happy Learning! 📚**

*Last Updated: April 2026*
