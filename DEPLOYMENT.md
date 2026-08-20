# Deployment Guide

This app has two parts that deploy separately:

- **Frontend** (`frontend/`) — a static React site (after `npm run build`, it's just HTML/CSS/JS).
- **Backend** (`backend/`) — a Python FastAPI process that needs to keep running.

You can't put a Python backend on something like GitHub Pages, which only serves static
files — so the two pieces go to different hosts. The good news: several hosts have
generous free tiers, so you can have this fully live at a real URL for $0/month.

If you're not sure which option to use, start with **Option A** — it's the simplest and
free.

---

## Before you start: push this project to GitHub

Both recommended options deploy directly from a GitHub repo.

```bash
cd genai-academy
git init
git add .
git commit -m "Initial commit: GenAI Academy"
```

Then create a new empty repository on [github.com/new](https://github.com/new) and follow
the "push an existing repository" instructions it shows you (something like):

```bash
git remote add origin https://github.com/<your-username>/genai-academy.git
git branch -M main
git push -u origin main
```

---

## Option A (recommended): Vercel + Render — both free

### Step 1 — Deploy the backend to Render

1. Go to [render.com](https://render.com) and sign up / log in (you can use your GitHub account).
2. Click **New +** → **Blueprint**.
3. Connect your GitHub account if prompted, then select your `genai-academy` repo.
4. Render will detect the `render.yaml` file in this project and pre-fill a web service
   called `genai-academy-api`. Click **Apply** / **Create**.
5. Wait for the first deploy to finish (a few minutes). You'll get a URL like:
   `https://genai-academy-api.onrender.com`
6. Visit `https://genai-academy-api.onrender.com/api/health` — you should see `{"status":"ok"}`.
   Keep this URL handy for Step 2.

> **Free tier note:** Render's free web services "spin down" after periods of inactivity
> and take ~30-60 seconds to wake back up on the next request. That's fine for a personal
> learning site; if that delay bothers you, Render's cheapest paid plan keeps it always-on.

### Step 2 — Deploy the frontend to Vercel

1. Go to [vercel.com](https://vercel.com) and sign up / log in with GitHub.
2. Click **Add New...** → **Project**, and import your `genai-academy` repo.
3. Vercel will ask for the project settings:
   - **Root Directory:** click "Edit" and set it to `frontend`
   - **Framework Preset:** Vercel should auto-detect "Vite" — leave it
4. Expand **Environment Variables** and add:
   - **Name:** `VITE_API_URL`
   - **Value:** the Render URL from Step 1, e.g. `https://genai-academy-api.onrender.com`
     (no trailing slash)
5. Click **Deploy**. After a minute or two, you'll get a URL like
   `https://genai-academy.vercel.app` — that's your live site.

### Step 3 — Allow the frontend to actually call the backend (CORS)

Right now the backend only allows requests from `localhost`. Update it to allow your real
Vercel URL:

1. Back in Render, open your `genai-academy-api` service → **Environment**.
2. Edit the `ALLOWED_ORIGINS` variable to your Vercel URL, e.g.:
   `https://genai-academy.vercel.app`
   (You can comma-separate multiple URLs if you later add a custom domain too.)
3. Save — Render will automatically redeploy.
4. Reload your Vercel site. Lessons should now load. If they don't, see **Troubleshooting**
   below.

### Step 4 (optional) — Connect your own domain

If you already own a domain (or bought one for this project):

- **In Vercel:** Project → **Settings** → **Domains** → add your domain, then add the DNS
  records Vercel shows you (usually a `CNAME` or `A` record) at your domain registrar.
- **Update CORS again:** add your custom domain (e.g. `https://yourdomain.com`) to the
  `ALLOWED_ORIGINS` variable on Render, comma-separated with the Vercel URL.

Vercel issues a free HTTPS certificate automatically once DNS is pointed at it.

---

## Option B: Railway (backend) + Netlify (frontend)

Same idea as Option A, different hosts — useful if you'd rather have both frontend and
backend easily manageable from Railway/Netlify's dashboards.

**Backend on Railway:**
1. [railway.app](https://railway.app) → New Project → Deploy from GitHub repo → select this repo.
2. Set the **Root Directory** to `backend`.
3. Railway auto-detects Python; set the **Start Command** to:
   `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add an environment variable `ALLOWED_ORIGINS` (set it after Step 2, once you have your Netlify URL).
5. Deploy, then copy the generated public URL.

**Frontend on Netlify:**
1. [netlify.com](https://netlify.com) → Add new site → Import an existing project → select this repo.
2. **Base directory:** `frontend`, **Build command:** `npm run build`, **Publish directory:** `frontend/dist`.
3. Add environment variable `VITE_API_URL` = your Railway backend URL.
4. Deploy, then go back to Railway and set `ALLOWED_ORIGINS` to your Netlify URL.

---

## Option C: Self-hosted on your own VPS (e.g. a Hostinger/DigitalOcean/Linode server)

Use this if you already have a VPS or bought hosting that gives you full server access
(not shared/managed web hosting — this needs the ability to run Docker or Python
processes).

### Prerequisites

- A VPS running Linux with [Docker](https://docs.docker.com/engine/install/) and the
  Docker Compose plugin installed.
- A domain with its DNS **A record** pointed at your VPS's IP address.

### Steps

1. SSH into your VPS and clone your repo:
   ```bash
   git clone https://github.com/<your-username>/genai-academy.git
   cd genai-academy
   ```
2. Start both services with Docker Compose (this builds and runs the frontend on port 80
   and the backend on port 8000, with the frontend's nginx proxying `/api` to the backend
   — see `frontend/nginx.conf`):
   ```bash
   docker compose up -d --build
   ```
3. Visit `http://<your-vps-ip>` — the site should load and lessons should work (no CORS
   setup needed here, since the frontend proxies API calls through itself on the same origin).
4. **Add HTTPS with a real domain.** The simplest option is putting
   [Caddy](https://caddyserver.com/) in front as a reverse proxy — it gets you free,
   auto-renewing HTTPS with about 5 lines of config. Install Caddy on the VPS (outside
   Docker, or as another container) with a Caddyfile like:
   ```
   yourdomain.com {
       reverse_proxy localhost:80
   }
   ```
   Then reload Caddy. Your site is now live at `https://yourdomain.com`.

### Updating the site later

```bash
cd genai-academy
git pull
docker compose up -d --build
```

---

## Troubleshooting

**Lessons won't load / blank white page after deploying:**
Open your browser's dev tools console (F12) on the deployed site. A CORS error
(`has been blocked by CORS policy`) means the backend's `ALLOWED_ORIGINS` doesn't include
your frontend's exact URL — double-check for typos, `http` vs `https`, and trailing
slashes (there shouldn't be one).

**Refreshing a lesson page (e.g. `/topics/rag/basics/rag-b-1`) gives a 404:**
This is a single-page app — the server needs to serve `index.html` for any unknown path
and let React Router handle routing client-side. Vercel and Netlify do this automatically
for Vite projects. If self-hosting with your own nginx (not the provided
`frontend/nginx.conf`), make sure it has a `try_files $uri /index.html;` fallback.

**Backend works locally but not after deploying:**
Check your host's build/runtime logs (Render: the "Logs" tab; Railway: "Deployments").
The most common issue is a missing environment variable or the start command not matching
`uvicorn app.main:app --host 0.0.0.0 --port $PORT` (the `$PORT` part matters — most hosts
assign a random port and expect your app to read it from that environment variable).

**Want a custom domain but haven't bought one yet:**
You can buy one from any registrar (Namecheap, Google Domains successor Squarespace
Domains, Porkbun, etc.) — then follow Step 4 in Option A (or the VPS steps in Option C)
to point it at your deployment.
