# 🌍 AI Language Translator using Google Gemini

## 👤 Participant Details

**Name:** Abhijith A Kurup

**MUID:** abhijitha-8@mulearn

---

# 📌 Project Overview

AI Language Translator is a web application that translates text into multiple languages using Google's Gemini Large Language Model (LLM). The application provides a simple and interactive interface where users can enter text, select a target language, and instantly receive an accurate translation.

The project demonstrates how Generative AI can be used to solve a real-world communication problem through natural language understanding and translation.

---

# 🎯 Chosen Use Case

**Language Translator**

People often need to communicate across different languages for education, travel, work, and personal conversations. This application helps users translate text quickly while preserving the original meaning and tone using an advanced AI model.

---

# 🤖 AI Platform / Model Used

- **Platform:** Google AI Studio
- **API:** Google Gemini API (Free Tier)
- **LLM:** Gemini Flash
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Development Environment:** Visual Studio Code

---

# ✨ Features

- 🌍 Translate text into multiple languages
- 🤖 AI-powered translations using Google Gemini
- 🎨 Clean and responsive user interface
- ⚡ Fast translation responses
- 🌐 Supports commonly used international languages
- 📝 Preserves the meaning and tone of the original text

---

# 🛠️ Technologies Used

- Python
- Flask
- Google Gemini API
- HTML5
- CSS3
- python-dotenv

---

# 📂 Project Structure

```
AI-Language-Translator/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dexter967/AI-Language-Translator.git
```

Move into the project directory

```bash
cd AI-Language-Translator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 💡 Prompt Engineering

The application uses a structured prompt to improve translation quality.

Example prompt:

```
You are a professional language translator.

Translate the following text into the selected language.

Rules:
- Preserve the original meaning.
- Preserve the tone.
- Do not explain anything.
- Return only the translated text.
```

This prompt helps produce concise, accurate, and context-aware translations.

---

# 🔍 Key Observations

- Google Gemini provides fast and high-quality translations.
- Well-structured prompts significantly improve translation accuracy.
- The model preserves sentence meaning better than direct word-for-word translation.
- The interface is simple and easy for users to interact with.
- AI can translate conversational and formal text effectively.

---

# ⚠️ Challenges Faced

- Configuring the Gemini API and environment variables.
- Managing API authentication securely.
- Deploying the Flask application to a cloud platform.
- Selecting a supported Gemini model for the latest API version.
- Optimizing dependency installation for deployment.

---

# 🚀 Future Improvements

- Support speech-to-text translation.
- Add text-to-speech output.
- Detect source language automatically.
- Store translation history.
- Allow users to copy or download translated text.
- Add support for more languages.
- Improve UI with dark mode and accessibility features.

---

# 📸 Proof of Implementation

The repository includes screenshots demonstrating:

- Application Home Page
- User Input
- AI Generated Translation

A public deployment link can also be provided after deployment.

---

# 📖 Conclusion

This project demonstrates the practical use of Generative AI for solving language translation problems. By integrating Google's Gemini LLM with a Flask-based web application, users can quickly translate text into multiple languages through a clean and interactive interface. The project highlights how prompt engineering and modern AI models can be combined to build useful real-world applications.

---

## 📂 Repository Contents

- ✅ Source Code
- ✅ Flask Application
- ✅ HTML & CSS Files
- ✅ requirements.txt
- ✅ README.md
