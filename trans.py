import streamlit as st
import torch
import whisper
import requests
import os
from gtts import gTTS  # Import gTTS for Text-to-Speech
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --------------------------
# SET PAGE CONFIG (Must be the first command)
# --------------------------
st.set_page_config(page_title="AI Speech Translator", page_icon="🎙️", layout="wide")

# Custom CSS for UI Styling
st.markdown("""
    <style>
            
        body {
            background-color: #1e1e1e;
            color: #d4af37;
        }
        .stButton>button {
            background-color: #8b5e3c;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stTextArea textarea, .stSelectbox select {
            background-color: #3e2723;
            color: white;
            border-radius: 8px;
        }
        .stAudio audio {
            width: 100%;
        }
        .css-1d391kg p {
            color: #d4af37;
        }
        
    </style>
            
""", unsafe_allow_html=True)

# --------------------------
# CONFIGURE API KEYS (Replace with yours)
# --------------------------
GEMINI_API_KEY = os.getenv("gemini")

# --------------------------
# LOAD WHISPER MODEL ONCE
# --------------------------
@st.cache_resource
def load_whisper():
    return whisper.load_model("large")

whisper_model = load_whisper()

# --------------------------
# FUNCTION: Speech to Text (Whisper)
# --------------------------
def convert_speech_to_text(audio_file):
    try:
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(audio_file.read())
        
        result = whisper_model.transcribe(audio_path)
        os.remove(audio_path)  # Clean up temporary file
        return result["text"]
    except Exception as e:
        return f"Error: {str(e)}"

# --------------------------
# FUNCTION: Translate Text (Gemini API)
# --------------------------
def translate_text(text, target_language):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{"parts": [{"text": f"Translate this to {target_language}: {text}"}]}]
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            response_json = response.json()
            translated_text = response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            return translated_text if translated_text else "Translation not found"
        else:
            return f"API Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

# --------------------------
# FUNCTION: Text to Speech (Using gTTS)
# --------------------------
def text_to_speech(text, language):
    try:
        tts = gTTS(text=text, lang=language)
        audio_path = "output.mp3"
        tts.save(audio_path)
        return audio_path
    except Exception as e:
        return f"Error: {str(e)}"

# --------------------------
# STREAMLIT UI LAYOUT
# --------------------------
st.sidebar.markdown("<h1 style='text-align: center; color :solid black'>🎙️ AI Speech Translator</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>A simple tool for speech-to-text, text-to-speech, and translations* 🎧</p>", unsafe_allow_html=True)

# CHECKBOX SELECTION
mode = st.sidebar.radio("Select Mode", ["Speech to Speech", "Text to Speech", "Speech to Text"], index=0)
# Mapping language codes to full names
language_map = {
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "hi": "Hindi",
    "ur": "Urdu",
    "en": "English",
    "it": "Italian",
    "nl": "Dutch",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean"
}
# --------------------------
# HANDLING MODE SELECTIONS
# --------------------------
if mode == "Speech to Speech":
    st.subheader("🎤 Upload Audio for Translation")
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    target_language = st.selectbox("Select Target Language", list(language_map.keys()), format_func=lambda x: language_map[x])
    
    if st.button("Translate Speech") and audio_file:
        text = convert_speech_to_text(audio_file)
        translated_text = translate_text(text, target_language)
        audio_path = text_to_speech(translated_text, target_language)
        
        if os.path.exists(audio_path):
            st.subheader("🎧 Translated Speech")
            st.audio(audio_path, format="audio/mp3")
            os.remove(audio_path)
        else:
            st.error("Error generating speech")

elif mode == "Text to Speech":
    st.subheader("📝 Enter Text for Speech Synthesis")
    input_text = st.text_area("Enter text to convert to speech")
    language = st.selectbox("Select Language", list(language_map.keys()), format_func=lambda x: language_map[x])
    
    if st.button("Generate Speech") and input_text:
        translated_text = translate_text(input_text, language)
        audio_path = text_to_speech(translated_text, language)
        if os.path.exists(audio_path):
            st.subheader("🔊 Generated Speech")
            st.audio(audio_path, format="audio/mp3")
            os.remove(audio_path)
        else:
            st.error("Error generating speech")

elif mode == "Speech to Text":
    st.subheader("🎙️ Upload Audio for Transcription")
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    language = st.selectbox("Select Language",list(language_map.keys()), format_func=lambda x: language_map[x])
    
    if st.button("Convert to Text") and audio_file:
        text = convert_speech_to_text(audio_file)
        translated_text = translate_text(text, language)
        st.subheader("📄 Transcribed Text")
        st.info(translated_text)

st.markdown("""
    <hr>
    <p style="text-align: center; color: #d4af37;">© 2025 AI Speech Translator | Built by M Ismail Danial</p>
""", unsafe_allow_html=True)
