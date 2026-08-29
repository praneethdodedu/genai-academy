import { useEffect, useMemo, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import { getLesson } from '../lib/api.js'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import FieldNote from '../components/FieldNote.jsx'
import { IconCheck } from '../components/icons.jsx'
import { useProgress } from '../context/ProgressContext.jsx'
import { extractHeadings } from '../lib/slug.js'

export default function LessonPage() {
  const { topicId, level, lessonId } = useParams()
  const navigate = useNavigate()
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)
  const [readPct, setReadPct] = useState(0)
  const [activeHeading, setActiveHeading] = useState(null)
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

  useEffect(() => {
    function onScroll() {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight
      const pct = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0
      setReadPct(pct)
    }
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [data])

  // Headings are extracted once from the raw markdown so the TOC can render
  // before (and independently of) react-markdown walking the tree.
  const headings = useMemo(() => (data ? extractHeadings(data.lesson.content) : []), [data])

  // Scrollspy — highlight whichever heading is currently nearest the top.
  useEffect(() => {
    if (!headings.length) return
    const elements = headings.map((h) => document.getElementById(h.slug)).filter(Boolean)
    if (!elements.length) return

    function onScroll() {
      const threshold = 120
      let current = elements[0].id
      for (const el of elements) {
        if (el.getBoundingClientRect().top - threshold <= 0) {
          current = el.id
        } else {
          break
        }
      }
      setActiveHeading(current)
    }
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [headings])

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

  function jumpTo(slug) {
    const el = document.getElementById(slug)
    if (!el) return
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    history.replaceState(null, '', `#${slug}`)
  }

  // Pairs each rendered <h2>/<h3> with the pre-extracted heading of the same
  // depth, in document order, so anchor ids line up with the TOC — reset on
  // every render since react-markdown walks the tree synchronously.
  let h2Index = 0
  let h3Index = 0
  const h2Headings = headings.filter((h) => h.depth === 2)
  const h3Headings = headings.filter((h) => h.depth === 3)
  const markdownComponents = {
    h2(props) {
      const h = h2Headings[h2Index]
      h2Index += 1
      return <h2 id={h?.slug}>{props.children}</h2>
    },
    h3(props) {
      const h = h3Headings[h3Index]
      h3Index += 1
      return <h3 id={h?.slug}>{props.children}</h3>
    },
  }

  return (
    <>
      <div className="reading-progress" aria-hidden="true">
        <div
          className="reading-progress__fill"
          style={{ width: `${readPct}%`, background: topic.color }}
        />
      </div>

      <div className="container section lesson-page">
        <div className="lesson-page__breadcrumbs">
          <Link to="/">Home</Link>
          <span className="lesson-page__crumb-sep">›</span>
          <Link to={`/topics/${topic.id}`}>{topic.name}</Link>
          <span className="lesson-page__crumb-sep">›</span>
          <span className="level-pill" data-level={level}>
            {level}
          </span>
        </div>

        <div className="lesson-page__layout">
          <article className="lesson-article">
            <p className="lesson-article__position" style={{ color: topic.color }}>
              Lesson {position.index} of {position.total}
            </p>
            <h1>{lesson.title}</h1>
            <p className="lesson-article__summary">{lesson.summary}</p>
            <p className="lesson-article__minutes">{lesson.minutes} min read</p>

            {headings.length > 0 && (
              <nav className="lesson-toc lesson-toc--inline" aria-label="On this page">
                <p className="lesson-toc__label">On this page</p>
                <ul>
                  {headings.map((h) => (
                    <li key={h.slug} className={h.depth === 3 ? 'lesson-toc__item--sub' : ''}>
                      <a
                        href={`#${h.slug}`}
                        className={activeHeading === h.slug ? 'lesson-toc__link--active' : ''}
                        onClick={(e) => {
                          e.preventDefault()
                          jumpTo(h.slug)
                        }}
                      >
                        {h.text}
                      </a>
                    </li>
                  ))}
                </ul>
              </nav>
            )}

            <div className="lesson-article__body">
              <ReactMarkdown components={markdownComponents}>{lesson.content}</ReactMarkdown>
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

            <FieldNote note={lesson.field_note} />

            <button
              type="button"
              className={`btn ${done ? 'btn--success' : 'btn--primary'} lesson-article__complete`}
              onClick={() => toggleCompleted(lesson.id)}
            >
              {done && <IconCheck width={16} height={16} />}
              {done ? 'Completed' : 'Mark as complete'}
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

          {headings.length > 0 && (
            <aside className="lesson-page__toc-rail">
              <nav className="lesson-toc lesson-toc--rail" aria-label="On this page">
                <p className="lesson-toc__label">On this page</p>
                <ul>
                  {headings.map((h) => (
                    <li key={h.slug} className={h.depth === 3 ? 'lesson-toc__item--sub' : ''}>
                      <a
                        href={`#${h.slug}`}
                        className={activeHeading === h.slug ? 'lesson-toc__link--active' : ''}
                        onClick={(e) => {
                          e.preventDefault()
                          jumpTo(h.slug)
                        }}
                      >
                        {h.text}
                      </a>
                    </li>
                  ))}
                </ul>
              </nav>
            </aside>
          )}
        </div>
      </div>
    </>
  )
}
