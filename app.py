from flask import Flask, redirect, render_template, request, render_template_string, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os
from openai import OpenAI

# ─── CONFIG ───────────────────────────────────────────────────────
PERPLEXITY_API_KEY = "INSERT_API_KEY_HERE"
CUSTOM_VISION_URL  = "https://www.customvision.ai/home"
SYSTEM_PROMPT = "You are a friendly lung health AI assistant."

# Initialize Flask and Perplexity client
app = Flask(__name__)
client = OpenAI(
    api_key=PERPLEXITY_API_KEY,
    base_url="https://api.perplexity.ai"
)

# Load models
t_ct = load_model('ctscan_densenet121.keras')
t_hist = load_model('histo_densenet121_model.keras')

CT_CLASSES = ['Squamous Cell Carcinoma','large.cell.carcinoma', 'Benign', 'Adenocarcinoma', 'MalignantCases', 'normal']
HIST_CLASSES = ['Adenocarcinoma','Benign','Squamous Cell Carcinoma']

def preprocess(path):
    img = Image.open(path).convert('RGB').resize((224,224))
    arr = np.expand_dims(np.array(img)/255.0,0)
    return arr

@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html', CUSTOM_VISION_URL=CUSTOM_VISION_URL)

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html',  CUSTOM_VISION_URL=CUSTOM_VISION_URL)


@app.route('/classify', methods=['POST'])
def classify():
    mod = request.form['modality']
    f = request.files['file']
    os.makedirs('static',exist_ok=True)
    fp = os.path.join('static',f.filename)
    f.save(fp)
    img = preprocess(fp)
    if mod=='ct':
        idx = np.argmax(t_ct.predict(img))
        result = CT_CLASSES[idx]
    else:
        idx = np.argmax(t_hist.predict(img))
        result = HIST_CLASSES[idx]
    return render_template('index.html', prediction=result, selected=mod, image_path=fp, CUSTOM_VISION_URL=CUSTOM_VISION_URL)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    msg = request.json.get('message','')
    msgs=[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':msg}]
    resp=client.chat.completions.create(model="sonar-pro", messages=msgs, max_tokens=500, temperature=0.7)
    return jsonify({'reply':resp.choices[0].message.content})

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        subject = "Registration Request"
        body = f"Name: {name}%0D%0ADOB: {dob}%0D%0AEmail: {email}"
        mailto = f"mailto:opejeremiah@gmail.com?subject={subject}&body={body}"
        return redirect(mailto)
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True, port=5000)
