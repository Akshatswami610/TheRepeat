# TheRepeat

**Discover music for every mood, moment and activity.**

A category-based music discovery platform featuring playlists for Gym, Party, Travel, Relaxing, Trucks, Buses and much more.

---

## ✨ Features

- 🎧 Explore music across different categories
- 🎵 YouTube playlist integration
- ⏯️ Music playback controls
- 📂 Dynamic category management
- 💬 User feedback system
- 📱 Responsive design

## 🛠️ Tech Stack

| Frontend | Backend | Database |
|:---:|:---:|:---:|
| HTML, CSS, JavaScript | Django, DRF | PostgreSQL |

**Music Integration:** YouTube IFrame Player API

## 📁 Project Structure

```text
TheRepeat/
├── backend/
│   ├── categories/
│   ├── config/
│   ├── feedback/
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── Base
│   ├── Home
│   └── Feedback
├── env/
├── .gitignore
└── .gitattributes
```

## 🚀 Getting Started

```bash
# Clone repository
git clone YOUR_REPOSITORY_URL
cd TheRepeat

# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/**

## 🌐 Deployment

Deployment preparation is in progress.

---

**Note:** Music playback is powered by YouTube's embedded player and is subject to YouTube's availability and embedding policies.

---

<p align="center">
  Made with ❤️
</p>
