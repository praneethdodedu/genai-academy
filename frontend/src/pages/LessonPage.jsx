import { useEffect, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import { getLesson } from '../lib/api.js'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import { useProgress } from '../context/ProgressContext.jsx'

export default function LessonPage() {
  const { topicId, level, lessonId } = useParams()
  const navigate = useNavigate()
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)
  const { isCompleted, toggleCompleted } = useProgress()

  function load() {
    setError(null)
    setData(null)
    getLesson(topicId, level, lessonId)
      .then(setData)
      .catch((err) => setError(err.message))
  }

  useEffect(() => {
    load()
    window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [topicId, level, lessonId])

  if (error) {
    return (
      <div className="container section">
        <ErrorState message={`Couldn't load this lesson: ${error}`} onRetry={load} />
      </div>
    )
  }

  if (!data) {
    return (
      <div className="container section">
        <Loader label="Loading lesson…" />
      </div>
    )
  }

  const { topic, lesson, prev, next, position } = data
  const done = isCompleted(lesson.id)

  function goTo(target) {
    if (!target) return
    navigate(`/topics/${topic.id}/${level}/${target.id}`)
  }

  return (
    <div className="container section lesson-page">
      <div className="lesson-page__breadcrumbs">
        <Link to="/">Home</Link>
        <span>/</span>
        <Link to={`/topics/${topic.id}`}>{topic.name}</Link>
        <span>/</span>
        <span className="level-pill" data-level={level}>
          {level}
        </span>
      </div>

      <div className="lesson-page__layout">
        <article className="lesson-article">
          <p className="lesson-article__position">
            Lesson {position.index} of {position.total}
          </p>
          <h1>{lesson.title}</h1>
          <p className="lesson-article__summary">{lesson.summary}</p>
          <p className="lesson-article__minutes">{lesson.minutes} min read</p>

          <div className="lesson-article__body">
            <ReactMarkdown>{lesson.content}</ReactMarkdown>
          </div>

          {lesson.takeaways && lesson.takeaways.length > 0 && (
            <div className="takeaways" style={{ '--topic-color': topic.color }}>
              <h3>Key takeaways</h3>
              <ul>
                {lesson.takeaways.map((t, i) => (
                  <li key={i}>{t}</li>
                ))}
              </ul>
            </div>
          )}

          <button
            type="button"
            className={`btn ${done ? 'btn--success' : 'btn--primary'} lesson-article__complete`}
            onClick={() => toggleCompleted(lesson.id)}
          >
            {done ? '✓ Completed' : 'Mark as complete'}
          </button>

          <nav className="lesson-nav">
            <button
              type="button"
              className="lesson-nav__btn"
              onClick={() => goTo(prev)}
              disabled={!prev}
            >
              <span className="lesson-nav__label">← Previous</span>
              {prev && <span className="lesson-nav__title">{prev.title}</span>}
            </button>
            <button
              type="button"
              className="lesson-nav__btn lesson-nav__btn--next"
              onClick={() => goTo(next)}
              disabled={!next}
            >
              <span className="lesson-nav__label">Next →</span>
              {next && <span className="lesson-nav__title">{next.title}</span>}
            </button>
          </nav>
        </article>
      </div>
    </div>
  )
}
