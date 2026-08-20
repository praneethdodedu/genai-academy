import { createContext, useContext, useEffect, useMemo, useState } from "react";

const STORAGE_KEY = "genai-academy-progress-v1";
const ProgressContext = createContext(null);

function loadCompleted() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw);
    return new Set(Array.isArray(arr) ? arr : []);
  } catch {
    return new Set();
  }
}

export function ProgressProvider({ children }) {
  const [completed, setCompleted] = useState(loadCompleted);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify([...completed]));
    } catch {
      // localStorage may be unavailable (private browsing, etc.) — fail silently
    }
  }, [completed]);

  const value = useMemo(
    () => ({
      isCompleted: (lessonId) => completed.has(lessonId),
      toggleCompleted: (lessonId) =>
        setCompleted((prev) => {
          const next = new Set(prev);
          if (next.has(lessonId)) {
            next.delete(lessonId);
          } else {
            next.add(lessonId);
          }
          return next;
        }),
      markCompleted: (lessonId) =>
        setCompleted((prev) => {
          if (prev.has(lessonId)) return prev;
          const next = new Set(prev);
          next.add(lessonId);
          return next;
        }),
      completedCount: (lessonIds) => lessonIds.filter((id) => completed.has(id)).length,
      totalCompleted: completed.size,
    }),
    [completed]
  );

  return <ProgressContext.Provider value={value}>{children}</ProgressContext.Provider>;
}

export function useProgress() {
  const ctx = useContext(ProgressContext);
  if (!ctx) throw new Error("useProgress must be used within a ProgressProvider");
  return ctx;
}
