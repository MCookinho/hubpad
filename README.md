# Hubpad

The public mural of everything and everyone.

## Features

- 📝 Create posts with title, text, and attachments
- 🔒 Password-protected posts (only title is publicly visible)
- 🌐 3 languages supported: Portuguese, English, Spanish
- 📱 Mobile-responsive
- 🔍 Search by title, text, ID, or filename
- 🎲 Random mode
- 🌙 Light/Dark theme
- 📁 Attach images, videos, audio, PDFs, documents, and more

## Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: JSON files + local disk
- **Security**: Passwords hashed with Werkzeug

---

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/hubpad.git
cd hubpad

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python app.py
# or
./run.sh
```

Access at: http://localhost:5000

---

## Deployment

### ⭐ BEST OPTION: PythonAnywhere (Persistent)

PythonAnywhere keeps files permanent (posts and uploads are NOT deleted).

**Step by step:**

1. Go to https://www.pythonanywhere.com and create a free account
2. Go to **Dashboard** → **Web** → **Add a new web app**
3. Choose **Manual configuration** → **Python 3.10+**
4. Go to **Consoles** → **Start a new console: Bash**
5. Run in the console:
```bash
git clone https://github.com/YOUR_USERNAME/hubpad.git
cd hubpad
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Go back to **Web** and configure:
   - **Source code**: `/home/YOUR_USERNAME/hubpad`
   - **Working directory**: `/home/YOUR_USERNAME/hubpad`
   - **Virtualenv**: `/home/YOUR_USERNAME/hubpad/venv`

7. Click **WSGI configuration file** and edit to:
```python
import sys

path = '/home/YOUR_USERNAME/hubpad'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

8. Click **Reload**: `YOUR_USERNAME.pythonanywhere.com`

**Done!** Your app is live and data is persistent.

---

### ⚡ Quick Option: Render.com (Resettable)

**Warning**: On Render's free tier, files are reset every time the app restarts (about once per day). Use only for testing.

**Step by step:**

1. Go to https://render.com and create an account
2. Click **New** → **Web Service**
3. Connect your GitHub repository
4. Fill in:
   - **Name**: `hubpad` (or any name)
   - **Region**: São Paulo or the closest one
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --preload`
   - **Environment**: Python 3
   - **Plan**: Free

5. Click **Deploy**

After ~2 minutes, your app will be available at `https://hubpad-YOUR_CODE.onrender.com`

---

### 🚂 Railway (Trial)

Similar to Render, but with $5 credit trial.

1. https://railway.app
2. New Project → Deploy from GitHub repo
3. Configure environment variables (if needed)
4. Deploy

---

## Project Structure

```
hubpad/
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
├── Procfile               # PaaS deployment
├── runtime.txt            # Python version
├── run.sh                 # Local script
├── .gitignore             # Git ignored files
├── README.md              # This file
├── data/
│   ├── .gitkeep           # (keeps folder)
│   └── messages.json      # Posts data (git ignored)
├── static/
│   └── uploads/
│       └── .gitkeep       # Attachments (images/videos go here)
└── templates/
    └── index.html         # Entire frontend (HTML + CSS + JS)
```

---

## Persistence Considerations

This app uses **local disk storage** (JSON files). This means:

✅ **Works perfectly** on:
- Your computer
- PythonAnywhere
- VPS/Dedicated servers
- Docker with volumes

⚠️ **Data gets RESET** on:
- Render (Free tier)
- Vercel
- Netlify
- Any "serverless" platform

**For real production**, consider migrating to:
- Database: PostgreSQL, Supabase, PlanetScale
- File storage: Cloudinary, AWS S3, Supabase Storage

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Server port |
| `FLASK_DEBUG` | `false` | Debug mode |

---

## License

MIT - Use however you want.

---

## Creator

Built with ❤️ using opencode
