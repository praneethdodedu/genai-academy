// Base URL for the FastAPI backend.
//
// - In local dev, Vite proxies /api to http://localhost:8000 (see vite.config.js),
//   so this can stay empty.
// - In production, set VITE_API_URL to your deployed backend's URL, e.g.
//   VITE_API_URL=https://your-backend.onrender.com
const API_BASE_URL = import.meta.env.VITE_API_URL || "";

async function request(path) {
  const res = await fetch(`${API_BASE_URL}${path}`);
  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = await res.json();
      detail = body.detail || detail;
    } catch {
      // ignore — body wasn't JSON
    }
    const error = new Error(detail || `Request failed: ${res.status}`);
    error.status = res.status;
    throw error;
  }
  return res.json();
}

export function getTopics() {
  return request("/api/topics");
}

export function getNav() {
  return request("/api/nav");
}

export function getTopic(topicId) {
  return request(`/api/topics/${encodeURIComponent(topicId)}`);
}

export function getLessonsForLevel(topicId, level) {
  return request(`/api/topics/${encodeURIComponent(topicId)}/${encodeURIComponent(level)}`);
}

export function getLesson(topicId, level, lessonId) {
  return request(
    `/api/lessons/${encodeURIComponent(topicId)}/${encodeURIComponent(level)}/${encodeURIComponent(lessonId)}`
  );
}

export function search(query) {
  if (!query || !query.trim()) return Promise.resolve({ results: [] });
  return request(`/api/search?q=${encodeURIComponent(query)}`);
}

export function getInstructor() {
  return request("/api/instructor");
}
