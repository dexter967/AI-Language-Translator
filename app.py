from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        language = request.form.get("language", "French")

        if text:
            prompt = f"""
You are a professional language translator.

Translate the following text into {language}.

Rules:
- Preserve the original meaning.
- Preserve the tone.
- Do not explain anything.
- Return only the translated text.

Text:
{text}
"""
            try:
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )
                translated_text = response.text
            except Exception as e:
                translated_text = f"Translation failed: {e}"

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)