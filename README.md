# GenAI Academy

A personal-branded educational website for learning **AI, Generative AI, RAG, and Prompt
Engineering** — structured as Basics → Intermediate → Pro, across 4 topics and 48 lessons,
taught by Praneeth Dodedu (AI Engineering Lead, 12+ years shipping production GenAI/RAG systems).

- **Frontend:** React (Vite) + React Router, plain CSS (no framework), `react-markdown` for lesson content.
- **Backend:** Python (FastAPI) serving a small read-only content API.
- **Progress tracking:** stored in the browser's `localStorage` (no accounts, no database).
- **Personal branding:** an "About the instructor" page (`/about`) built from a real profile, plus
  "From the field" callouts on select lessons connecting the theory to projects actually shipped
  (Claire AI, enterprise chatbots, RAG with Azure AI Search, multi-agent systems).

## Project structure

```
genai-academy/
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI app + routes
│   │   ├── data.py         # All course content (topics, levels, lessons)
│   │   └── instructor.py   # Instructor profile + "field notes" for select lessons
│   ├── requirements.txt
│   ├── Dockerfile          # optional, for VPS/Docker deployment
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── pages/          # Home, TopicPage, LessonPage, InstructorPage, NotFound
│   │   ├── components/     # Navbar, TopicCard, LessonRow, FieldNote, etc.
│   │   ├── context/        # ProgressContext (localStorage progress)
│   │   └── lib/api.js      # fetch wrapper for the backend API
│   ├── Dockerfile           # optional, for VPS/Docker deployment
│   └── .env.example
├── render.yaml              # one-click backend deploy config for Render
├── docker-compose.yml       # optional, for self-hosting on a VPS
└── DEPLOYMENT.md            # step-by-step deployment guide
```

## Running locally

You need Node.js 18+ and Python 3.10+.

**1. Backend**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API is now at `http://localhost:8000` — try `http://localhost:8000/api/health`
or the interactive docs at `http://localhost:8000/docs`.

**2. Frontend** (in a new terminal)

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The dev server proxies `/api` calls to the backend
automatically (see `frontend/vite.config.js`), so no extra setup is needed.

## Adding or editing lessons

All course content lives in one place: `backend/app/data.py`. Each lesson is a
plain dict with `id`, `title`, `minutes`, `summary`, `content` (Markdown), and
`takeaways`. Add a new lesson to the relevant topic/level list and it will
automatically show up in the frontend — no frontend changes needed.

## Editing the instructor profile or field notes

`backend/app/instructor.py` holds two things:

- `INSTRUCTOR` — the profile shown on `/about` (bio, achievements, skills, experience).
  Update this if your bio, role, or projects change.
- `FIELD_NOTES` — a dict mapping a lesson `id` (from `data.py`) to a short "from the field"
  callout shown at the bottom of that lesson. Only add one where the connection to a real
  project is genuine — add a new entry to expand coverage, or remove one if it starts to feel
  forced.

## Deployment

See **[DEPLOYMENT.md](./DEPLOYMENT.md)** for step-by-step instructions covering:

- **Option A (recommended):** Vercel (frontend) + Render (backend) — free, no server management.
- **Option B:** Railway (backend) + Netlify (frontend).
- **Option C:** Self-hosted on your own VPS with Docker Compose.
