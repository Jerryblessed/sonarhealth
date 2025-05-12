import os
import requests
from flask import Flask, render_template_string, request, jsonify, send_from_directory
from openai import AzureOpenAI

# ─── CONFIG (All secrets inlined as requested) ───────────────────────────
AZURE_OPENAI_BASE    = "https://thisisoajo.openai.azure.com/"
AZURE_OPENAI_MODEL   = "gpt-4o"
AZURE_OPENAI_KEY     = "9I4UEJweVUdih04Uv8AXcAxs5H8jSQRfwaugcSQYHcI882wSpFvqJQQJ99BAACL93NaXJ3w3AAABACOGkv4f"
AZURE_OPENAI_VERSION = "2023-06-01-preview"
CUSTOM_VISION_URL    = "https://www.customvision.ai/"

# System prompt for AI assistant
SYSTEM_PROMPT = (
    "You are a friendly lung health AI assistant."
)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_VERSION,
    base_url=f"{AZURE_OPENAI_BASE}/openai/deployments/{AZURE_OPENAI_MODEL}"
)

# ─── FLASK APP ─────────────────────────────────────────────────────────────
app = Flask(__name__)

# HTML template for landing page
HTML = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Lung Health</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { margin: 0; font-family: sans-serif; background: #f8f9fa; }
    .hero {
      position: relative;
      height: 60vh;
      background: url('/static/lung.jpg') no-repeat center center;
      background-size: cover;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      color: #fff;
      text-shadow: 0 0 10px rgba(0,0,0,0.7);
    }
    .overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.4);
    }
    .hero-content {
      position: relative;
      z-index: 1;
      text-align: center;
      padding: 0 1rem;
    }
    .chat-window { max-height: 400px; overflow-y: auto; background: #fff; padding: 1rem; border: 1px solid #dee2e6; border-radius: .5rem; }
    #add-form, #thankyou { margin-top: 1rem; text-align: center; color: #fff; }
  </style>
</head>
<body>
  <div class="hero">
    <div class="overlay"></div>
    <div class="hero-content">
      <h1 class="display-5 fw-bold">Breath Safe</h1>
      <p class="lead">Explore how artificial intelligence is transforming lung health and cancer care.</p>
      <p class="fw-semibold">Get free lung histopathology images now</p>
      <a href="{{ custom_vision_url }}" class="btn btn-primary m-2" target="_blank">Go to Custom Vision →</a>
      <button class="btn btn-outline-light m-2" onclick="showForm()">Add to viewers list</button>

      <div id="add-form" style="display:none;">
        <h5>Add to Custom Vision Lung Image Checkers List</h5>
        <form id="viewer-form" class="d-flex flex-column align-items-start">
          <input type="text" id="name" class="form-control mb-2" placeholder="Name" required>
          <input type="date" id="dob" class="form-control mb-2" placeholder="Date of Birth" required>
          <input type="email" id="email" class="form-control mb-2" placeholder="Email" required>
          <button type="submit" class="btn btn-light">Submit</button>
        </form>
      </div>
      <div id="thankyou" style="display:none;">
        <p>Thank you! You would be emailed shortly.</p>
      </div>
    </div>
  </div>

  <div class="container my-4">
    <h4>AI Chatbot Assistant</h4>
    <div id="chat" class="chat-window mb-3"></div>
    <div class="input-group">
      <input id="user-input" type="text" class="form-control" placeholder="Ask about lung health...">
      <button id="send-btn" class="btn btn-success">Send</button>
    </div>
  </div>

  <script>
    const chatEl = document.getElementById('chat');
    const inputEl = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    function appendMessage(sender, text) {
      const msg = document.createElement('div');
      msg.classList.add('mb-2', sender === 'AI' ? 'text-start' : 'text-end');
      msg.innerHTML = `<small><strong>${sender}:</strong></small> ${text}`;
      chatEl.appendChild(msg);
      chatEl.scrollTop = chatEl.scrollHeight;
    }

    sendBtn.addEventListener('click', () => {
      const text = inputEl.value.trim();
      if (!text) return;
      appendMessage('You', text);
      inputEl.value = '';

      fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      })
      .then(res => res.json())
      .then(data => appendMessage('AI', data.reply))
      .catch(err => appendMessage('AI', 'Error: ' + err));
    });

    inputEl.addEventListener('keypress', e => { if (e.key === 'Enter') sendBtn.click(); });

    function showForm() {
      document.getElementById('add-form').style.display = 'block';
    }

    document.getElementById('viewer-form').addEventListener('submit', function(e) {
      e.preventDefault();
      const name = encodeURIComponent(document.getElementById('name').value);
      const dob  = encodeURIComponent(document.getElementById('dob').value);
      const email= encodeURIComponent(document.getElementById('email').value);
      const subject = 'Add to Custom Vision Lung Image Checkers List';
      const body = `Name: ${name}%0D%0ADOB: ${dob}%0D%0AEmail: ${email}`;
      window.location.href = `mailto:opejeremiah@gmail.com?subject=${subject}&body=${body}`;
      document.getElementById('add-form').style.display = 'none';
      document.getElementById('thankyou').style.display = 'block';
    });
  </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML, custom_vision_url=CUSTOM_VISION_URL)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.json
    user_msg = data.get('message', '')
    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': user_msg}
    ]
    resp = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL,
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    return jsonify({'reply': resp.choices[0].message.content})

# Serve static lung scan image: place lung_scan.jpg in ./static/
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
