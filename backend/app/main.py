"""
GenAI Academy — backend API.

A minimal, read-only content API that serves the curriculum (topics, levels,
and lessons) defined in app/data.py to the React frontend.

Run locally:
    uvicorn app.main:app --reload --port 8000

Endpoints:
    GET /api/health
    GET /api/topics
    GET /api/topics/{topic_id}
    GET /api/topics/{topic_id}/{level}
    GET /api/lessons/{topic_id}/{level}/{lesson_id}
    GET /api/search?q=...
"""

import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .data import TOPICS, LESSONS, LEVELS, LEVEL_META

app = FastAPI(
    title="GenAI Academy API",
    description="Content API powering an educational site about AI, GenAI, RAG, and Prompt Engineering.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# CORS
#
# In production, set the ALLOWED_ORIGINS environment variable to a comma
# separated list of the exact frontend origin(s), e.g.:
#   ALLOWED_ORIGINS=https://your-site.vercel.app,https://yourdomain.com
# During local development we fall back to permissive localhost origins.
# ---------------------------------------------------------------------------
_default_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
_env_origins = os.environ.get("ALLOWED_ORIGINS", "")
allowed_origins = [o.strip() for o in _env_origins.split(",") if o.strip()] or _default_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def _topic_or_404(topic_id: str) -> dict:
    topic = next((t for t in TOPICS if t["id"] == topic_id), None)
    if topic is None:
        raise HTTPException(status_code=404, detail=f"Unknown topic '{topic_id}'")
    return topic


def _level_or_404(level: str) -> None:
    if level not in LEVELS:
        raise HTTPException(status_code=404, detail=f"Unknown level '{level}'. Must be one of {LEVELS}.")


def _lesson_summary(lesson: dict) -> dict:
    """Strip the full lesson content out for list views, keeping payloads small."""
    return {
        "id": lesson["id"],
        "title": lesson["title"],
        "minutes": lesson["minutes"],
        "summary": lesson["summary"],
    }


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/topics")
def get_topics():
    """List every topic, with lesson counts per level, for building nav/home views."""
    result = []
    for topic in TOPICS:
        levels = {
            level: {
                "label": LEVEL_META[level]["label"],
                "description": LEVEL_META[level]["description"],
                "lesson_count": len(LESSONS[topic["id"]][level]),
            }
            for level in LEVELS
        }
        result.append({**topic, "levels": levels})
    return {"topics": result}


@app.get("/api/topics/{topic_id}")
def get_topic(topic_id: str):
    """Full detail for one topic: metadata plus lesson summaries for every level."""
    topic = _topic_or_404(topic_id)
    levels = {
        level: {
            "label": LEVEL_META[level]["label"],
            "description": LEVEL_META[level]["description"],
            "lessons": [_lesson_summary(l) for l in LESSONS[topic_id][level]],
        }
        for level in LEVELS
    }
    return {**topic, "levels": levels}


@app.get("/api/topics/{topic_id}/{level}")
def get_lessons_for_level(topic_id: str, level: str):
    """Lesson summaries for one topic + level (used by the level/lesson-list view)."""
    topic = _topic_or_404(topic_id)
    _level_or_404(level)
    lessons = LESSONS[topic_id][level]
    return {
        "topic": {"id": topic["id"], "name": topic["name"], "color": topic["color"]},
        "level": {"id": level, **LEVEL_META[level]},
        "lessons": [_lesson_summary(l) for l in lessons],
    }


@app.get("/api/lessons/{topic_id}/{level}/{lesson_id}")
def get_lesson(topic_id: str, level: str, lesson_id: str):
    """Full lesson content, plus previous/next lesson ids for in-lesson navigation."""
    topic = _topic_or_404(topic_id)
    _level_or_404(level)
    lessons = LESSONS[topic_id][level]
    index = next((i for i, l in enumerate(lessons) if l["id"] == lesson_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail=f"Unknown lesson '{lesson_id}'")

    lesson = lessons[index]
    prev_lesson = lessons[index - 1] if index > 0 else None
    next_lesson = lessons[index + 1] if index < len(lessons) - 1 else None

    return {
        "topic": {"id": topic["id"], "name": topic["name"], "color": topic["color"]},
        "level": {"id": level, **LEVEL_META[level]},
        "lesson": lesson,
        "prev": _lesson_summary(prev_lesson) if prev_lesson else None,
        "next": _lesson_summary(next_lesson) if next_lesson else None,
        "position": {"index": index + 1, "total": len(lessons)},
    }


@app.get("/api/search")
def search(q: str = ""):
    """Simple in-memory keyword search across lesson titles and summaries."""
    q = q.strip().lower()
    if not q:
        return {"results": []}

    results = []
    for topic in TOPICS:
        for level in LEVELS:
            for lesson in LESSONS[topic["id"]][level]:
                haystack = f"{lesson['title']} {lesson['summary']}".lower()
                if q in haystack:
                    results.append(
                        {
                            "topic_id": topic["id"],
                            "topic_name": topic["name"],
                            "level": level,
                            **_lesson_summary(lesson),
                        }
                    )
    return {"results": results[:25]}
