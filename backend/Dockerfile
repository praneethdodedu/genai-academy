# Optional Dockerfile — only needed if you're deploying the backend to a
# VPS, Railway, Fly.io, or any platform that runs containers directly,
# rather than Render's native Python runtime (see render.yaml) or a
# platform that builds from requirements.txt automatically.
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
