# 🎙️ AI-VoiceFlow: AI-Powered Speech Translator

AI-VoiceFlow is an intelligent **speech-processing** application that enables **real-time transcription, translation, and text-to-speech conversion**. It supports **multiple languages**, allowing users to **speak, transcribe, and listen** to translated speech effortlessly.

## 🌟 Features
✅ **Speech-to-Text**: Convert audio into text using OpenAI's **Whisper**.  
✅ **Text Translation**: Translate transcribed text into multiple languages via **Gemini API**.  
✅ **Text-to-Speech**: Convert text back into speech using **Google Text-to-Speech (gTTS)**.  
✅ **Speech-to-Speech**: Upload an audio file, transcribe it, translate it, and generate speech in the target language.  
✅ **Multi-Language Support**: English, French, Spanish, Hindi, Urdu, German, Chinese, and more!  
✅ **Streamlit UI**: Simple, responsive, and user-friendly.  

## 🛠️ Installation

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/AI-VoiceFlow.git
cd AI-VoiceFlow
```

### 2️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys  
Create a `.env` file and add your **Gemini API key**:  
```env
gemini=your_api_key_here
```

### 4️⃣ Run the Application  
```sh
streamlit run app.py
```

## 🎯 How to Use?
1. **Choose Mode**: Speech-to-Speech, Speech-to-Text, or Text-to-Speech.  
2. **Upload an Audio File or Enter Text**.  
3. **Select Target Language**.  
4. **Click the Process Button** – and let AI do the magic!  

## 📌 Dependencies
- `streamlit`
- `torch`
- `whisper`
- `requests`
- `gtts`
- `python-dotenv`

## 📷 Screenshots  
🎤 **Upload Audio for Translation**  
![Upload Screen](screenshots/upload.png)  

🔊 **Listen to Translated Speech**  
![Translated Speech](screenshots/speech.png)  

## 📜 License
MIT License  

## 💡 Future Enhancements
- Integrate **real-time voice input**.  
- Add **custom language models** for better accuracy.  
- Support **offline mode** for speech processing.  

🚀 **Try it out and start translating speech instantly!**  
