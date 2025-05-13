
# 🫁 Breath Safe

[![Presentation](https://docs.google.com/presentation/d/1r_a98Et5a3CCOZtHDk0O5rNGh_tOkeDCvzrJvdH8OQA/edit?usp=sharing)](https://docs.google.com/presentation/d/1r_a98Et5a3CCOZtHDk0O5rNGh_tOkeDCvzrJvdH8OQA/edit?usp=sharing)
🔗 **View the project pitch deck**

A lightweight Flask application that leverages Azure Custom Vision and an AI chatbot to democratize lung-cancer image analysis on a dedicated source-code pad. Breath Safe enables non-technical health workers in low-resource settings to upload histopathology and CT scans from a simple web UI—no coding required.

## 🚀 Features

* 🖼️ **Image Upload**
  Drag-and-drop or browse to send lung histopathology or CT images to Azure Custom Vision.
* 🤖 **AI Chatbot Assistant**
  Ask questions about lung health and get real-time answers via Azure OpenAI.
* 📋 **Viewer List Signup**
  Securely request access to the Custom Vision project via an inline form.
* 🔗 **Custom Vision Link**
  One-click entry to the shared Azure Custom Vision resource.
* 💾 **No-Code ML**
  All model training, tagging, and inference happen in Azure’s portal or on a shared source-code pad.

## 🎯 Uniqueness

1. **Dual-modality support**
   Handles both high-resolution histopathology (15 K trained images) and CT scans (~1K trained images) using DenseNet121 backbones for high-detail feature extraction.
2. **Embedded AI agent**
   An interactive chatbot guides uploads, interprets model outputs, and educates non-specialists in real time.
3. **Role-based access**
   “Viewer list” replaces hard-coded keys, enabling secure, auditable custom vision permissions.
4. **Azure custome vision**
   Users can use our trained model on custom vision to analyze lung image(~800 trained images) after they email for access.

## 🌍 Social Good

* **Bridging diagnostic gaps** in rural clinics (imaging <15 % coverage).
* **Advancing SDG 3.4**: Early detection could save 600 000+ lives annually by reducing premature lung cancer deaths by one-third.
* **Empowering non-technical users**: Intuitive no-code UI lets health workers directly participate in AI-driven diagnosis.
* **Fostering collaboration**: Shared code pad encourages peer review, auditability, and knowledge exchange.

## 🛠️ Getting Started

```bash
# Clone the repo
git clone https://github.com/Jerryblessed/breathsafe.git
cd breathsafe

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask requests azure-ai-vision openai

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser to explore.

© 2025 Breath Safe Initiative
