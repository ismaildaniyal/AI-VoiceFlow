# 🎙️ AI-VoiceFlow: AI-Powered Speech Translator

AI-VoiceFlow is an intelligent **speech-processing** application that enables **real-time transcription, translation, and text-to-speech conversion**. It supports **multiple languages**, allowing users to **speak, transcribe, and listen** to translated speech effortlessly.

## 🌟 Features
✅ **Speech-to-Text**: Convert audio into text using OpenAI's **Whisper**.  
✅ **Text Translation**: Translate transcribed text into multiple languages via **Gemini API**.  
✅ **Text-to-Speech**: Convert text back into speech using **Google Text-to-Speech (gTTS)**.  
✅ **Speech-to-Speech**: Upload an audio file, transcribe it, translate it, and generate speech in the target language.  
✅ **Multi-Language Support**: English, French, Spanish, Hindi, Urdu, German, Chinese, and more!  
✅ **Streamlit UI**: Simple, responsive, and user-friendly.  


## Technologies Used
- **Python**
- **Streamlit**
- **Whisper AI** (Speech-to-Text)
- **Google Gemini API** (Translation)
- **gTTS** (Text-to-Speech)
- **Dotenv** (Environment Variable Management)

- 
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
![Audio](deepgram-asteria-1738782809878.mp3)  

🔊 **Listen to Translated Speech**  
![Translated Speech](b9fcfaf0b0a48735488757a018fb2a56dc130fc43f64958bde129090)  

## Demo Video
Watch the demo video to understand how AI Speech Translator works:

📺 **[Demo Video]([bandicam 2025-02-09 23-23-03-479.mp4](https://github.com/ismaildaniyal/AI-VoiceFlow/blob/main/bandicam%202025-02-09%2023-23-03-479.mp4))**

## Deployment
The application is deployed on Streamlit. You can access the live demo via the link below:

🔗 **[Streamlit Deployment](https://your-streamlit-deployment-link.com)**


## 📜 License
MIT License  

## 💡 Future Enhancements
- Integrate **real-time voice input**.  
- Add **custom language models** for better accuracy.  
- Support **offline mode** for speech processing.  

🚀 **Try it out and start translating speech instantly!**  

## Author
👨‍💻 **Developer:** M Ismail Daniyal

