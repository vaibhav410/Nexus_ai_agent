# Nexus AI Agent - Mental Wellness Companion

![Nexus AI Agent](<img width="1668" height="728" alt="Screenshot 2025-12-02 005050" src="https://github.com/user-attachments/assets/4754fe7b-7ebd-4c69-8b35-c1bb1e71aae1" />)

> **Today, millions experience anxiety, stress, and emotional burnout without immediate access to support.** Nexus AI Agent provides an always-available companion for emotion regulation, journaling, meditation, and personalized guidance—**without medical advice**.


## 🚀 Why Multi-Agent Architecture?

Mental wellness needs **dynamic, specialized responses**. Nexus uses modular agents that collaborate:

Assessment Agent → Emotional tone detection
Support Agent → Grounding, breathing, journaling prompts
Follow-up Agent → Mood tracking & long-term suggestions


**Benefits**: Intelligent, safe, flexible, and scalable.

## 🏗️ System Architecture

User → HTML/CSS/JS Frontend (Chat UI + Mode Selector)
↓ POST /analyze
Flask Backend → Rule-based emotional filter + Mode router
↓ (Therapy/Meditate/Journal/Crisis)
Tool Layer → Breathing, Grounding, Sleep routines
↓
Gemini 2.5 Flash → Empathetic, safety-filtered replies
↓ mindmate.db+db_manager.py
Frontend → Animated responses + mood tracking


## ✨ Core Features

### **Multi-Mode Support**
- **Therapy Mode**: Comforting emotional support
- **Meditation Mode**: Guided breathing + mindfulness  
- **Journal Mode**: Reflection prompts
- **Crisis Mode**: Grounding + safety messaging [web:4]

### **Smart Rule-Based Layer**
- Anxiety/Stress/Panic detection
- Quick HINGLISH fallbacks
- Cost-efficient (reduces API calls)
- Offline-safe responses

### **Specialized Tools**



## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | HTML/CSS/JS, Google ADK-inspired UI, Mobile-responsive |
| **Backend** | Flask, Flask-CORS, python-dotenv [attached_file:3] |
| **AI Core** | Gemini 2.5 Flash (google-generativeai 0.7.2) |
| **Tools** | Custom Python modules (breathing.py, grounding.py) |
| **Data** | JSON mood storage + simple DB manager |
| **Deployment** | Gunicorn production server |



1. Setup
pip install -r requirements.txt
echo "GEMINI_KEY=your_key_here" > app.env
python verify_setup.py # Verify everything works

2. Development
python app.py

Visit: http://127.0.0.1:5000
3. Production
gunicorn -w 4 -b 0.0.0.0:8000 app:app

text

## 📱 API Endpoints

curl -X POST http://127.0.0.1:5000/analyze
-H "Content-Type: application/json"
-d '{"text": "Feeling anxious", "mode": "therapy"}'

text

**Response**: `{"reply": "AI empathetic response"}` [attached_file:2]

## 📁 File Structure

├── app.py # Flask backend + agent orchestration
├── verify_setup.py # Environment + API verification​
├── requirements.txt # Dependencies​
├── app.env # GEMINI_KEY
├── static/ # CSS/JS (dark UI + animations)
├── templates/index.html # Chat interface
├── tools/ # Breathing, grounding, sleep modules
├── logs.json # Mood + session storage​
└── database/ # Simple mood pattern manager


## 🌟 Future Roadmap

- Voice interaction
- Wearable integration (heart rate, sleep)
- Therapist dashboard
- Multi-language support
- Advanced mood analytics [web:4]

