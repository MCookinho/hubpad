import os
import json
import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'data/messages.json'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx', 'zip', 'mp3', 'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_messages(messages):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

def filter_message_for_public(msg):
    if msg.get('is_private'):
        return {
            'id': msg['id'],
            'title': msg['title'],
            'lang': msg.get('lang', 'pt'),
            'timestamp': msg['timestamp'],
            'date': msg['date'],
            'is_private': True
        }
    return msg.copy()

@app.route('/')
def index():
    messages = load_messages()
    messages.sort(key=lambda x: x['timestamp'], reverse=True)
    public_messages = [filter_message_for_public(m) for m in messages]
    return render_template('index.html', messages=public_messages)

@app.route('/post', methods=['POST'])
def post_message():
    title = request.form.get('title', '').strip()
    text = request.form.get('text', '').strip()
    lang = request.form.get('lang', 'pt')
    files = request.files.getlist('files')
    is_private = request.form.get('is_private') == 'on'
    password = request.form.get('password', '').strip()
    
    if not text and not files:
        return redirect(url_for('index'))
    
    uploaded_files = []
    for file in files:
        if file and file.filename:
            if allowed_file(file.filename):
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
                original_filename = secure_filename(file.filename)
                filename = f"{timestamp}_{original_filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                uploaded_files.append({
                    'filename': filename,
                    'original': original_filename
                })
    
    messages = load_messages()
    
    message = {
        'id': len(messages) + 1,
        'title': title,
        'text': text,
        'lang': lang,
        'files': uploaded_files,
        'timestamp': datetime.now().isoformat(),
        'date': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'is_private': is_private,
        'password_hash': generate_password_hash(password) if (is_private and password) else None
    }
    messages.append(message)
    save_messages(messages)
    
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/api/random')
def api_random():
    messages = load_messages()
    if not messages:
        return jsonify({'error': 'No messages'}), 404
    message = random.choice(messages)
    return jsonify(filter_message_for_public(message))

@app.route('/api/unlock', methods=['POST'])
def api_unlock():
    data = request.get_json()
    message_id = data.get('id')
    password = data.get('password', '')
    
    if not message_id or password is None:
        return jsonify({'success': False, 'error': 'Invalid request'}), 400
    
    messages = load_messages()
    message = next((m for m in messages if m['id'] == int(message_id)), None)
    
    if not message:
        return jsonify({'success': False, 'error': 'Message not found'}), 404
    
    if not message.get('is_private'):
        return jsonify({'success': True, 'text': message.get('text', ''), 'files': message.get('files', [])})
    
    if not message.get('password_hash'):
        return jsonify({'success': True, 'text': message.get('text', ''), 'files': message.get('files', [])})
    
    if check_password_hash(message['password_hash'], password):
        return jsonify({
            'success': True,
            'text': message.get('text', ''),
            'files': message.get('files', [])
        })
    else:
        return jsonify({'success': False, 'error': 'Wrong password'})

@app.route('/health')
def health_check():
    return jsonify({'status': 'ok', 'message': 'Hubpad is running'})

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

def initialize_data():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        save_messages([])

initialize_data()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)
