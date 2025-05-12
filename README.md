# Breath Safe

[![Presentation](https://docs.google.com/presentation/d/1r_a98Et5a3CCOZtHDk0O5rNGh_tOkeDCvzrJvdH8OQA/edit?usp=sharing)](https://docs.google.com/presentation/d/1r_a98Et5a3CCOZtHDk0O5rNGh_tOkeDCvzrJvdH8OQA/edit?usp=sharing)
\:link: **View the project pitch deck**

A lightweight Flask application that leverages Azure Custom Vision and an AI chatbot to democratize lung‐cancer image analysis. Breath Safe enables non-technical health workers in low-resource settings to upload histopathology (and CT) images for instant AI predictions, without writing a single line of code.

## 🚀 Features

* 🖼️ **Image Upload**: Drag-and-drop or browse to send lung histopathology images to Azure Custom Vision.
* 🤖 **AI Chatbot Assistant**: Ask questions about lung health and get real‑time answers via Azure OpenAI.
* 📋 **Viewer List Signup**: Securely request access to the Custom Vision project via an inline form.
* 🔗 **Custom Vision Link**: One-click entry to the shared Azure Custom Vision resource.
* 💾 **No-Code ML**: All model training, tagging, and evaluation happen in Azure’s portal UI—no programming required.

## 🎯 Uniqueness

1. **Dual-modality support**: Handles both histopathology and CT scans in one cohesive platform.
2. **Built-in AI Agent**: An embedded chatbot guides users through uploads, interprets model outputs, and educates non-specialists.
3. **Role-based access**: “Viewer list” replaces exposed secrets, enabling secure, auditable custom vision permissions.
4. **Offline-ready roadmap**: Designed for future containerized inference to support clinics with intermittent internet.

## 🌍 Social Good

* **Bridging the diagnostic gap** in rural clinics (today imaging <15 % of eligible patients).
* **Advancing SDG 3.4**: Early detection could save 600,000+ lives annually by reducing premature lung cancer deaths by one‑third.
* **Empowering non‑technical users**: No-code UI lets health workers directly participate in AI diagnosis.
* **Fostering collaboration**: Shared viewer list encourages peer review and knowledge exchange.

## 🛠️ Getting Started

```bash
# Clone the repo
git clone https://github.com/Jerryblessed/breathsafe.git
cd breathsafe

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask requests openai

# Set environment variables (optional)
# export FLASK_ENV=development

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser to explore.

---

© 2025 Breath Safe Initiative
