import io
import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors as genai_errors
from gtts import gTTS

# Load env variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


# ── Custom exceptions ─────────────────────────────────────────────────────────
class QuotaExceededError(Exception):
    """Raised when the Gemini API free-tier quota is exhausted."""
    pass

class GeminiAPIError(Exception):
    """Raised for any other Gemini API error."""
    pass


# ── Central Gemini caller with error handling ─────────────────────────────────
def _call_gemini(model: str, contents: list) -> str:
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
        )
        return response.text

    except genai_errors.ClientError as e:
        msg = str(e)
        if "429" in msg or "RESOURCE_EXHAUSTED" in msg or "quota" in msg.lower():
            raise QuotaExceededError(
                "Free-tier quota exhausted. Please wait a few minutes and try again, "
                "or upgrade your Google AI plan."
            ) from e
        raise GeminiAPIError(f"Gemini API error: {msg}") from e

    except Exception as e:
        raise GeminiAPIError(f"Unexpected error: {str(e)}") from e


# ── Public functions ──────────────────────────────────────────────────────────
def genarate_note(images: list) -> str:
    prompt = """Analyze the image and extract key topics.

Instructions:
- Identify 3 to 5 important topics
- For each topic, write a very short explanation (max 12 words)
- Keep total response under 80 words
- Use bullet points with **bold** topic names
- Avoid long sentences or extra details

Output format:
- **Topic 1**: short explanation
- **Topic 2**: short explanation
- **Topic 3**: short explanation"""

    return _call_gemini("gemini-2.0-flash", [*images, prompt])


def genarate_audio(text: str) -> io.BytesIO:
    try:
        tts = gTTS(text, lang="en")
        audio_buf = io.BytesIO()
        tts.write_to_fp(audio_buf)
        audio_buf.seek(0)
        return audio_buf
    except Exception as e:
        raise GeminiAPIError(f"Audio generation failed: {str(e)}") from e


def genarate_quiz(images: list) -> str:
    prompt = """Analyze the image and create a quiz with exactly 3 questions.

Format each question like this:

**Q1: [Question here]**
- A) option
- B) option
- C) option
- D) option

> ✅ **Answer:** [Correct option]

---

Make sure the questions test genuine understanding, not just recall."""

    return _call_gemini("gemini-2.0-flash", [*images, prompt])