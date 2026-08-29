import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getTopics } from '../lib/api.js'
import TopicCard from '../components/TopicCard.jsx'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import { useProgress } from '../context/ProgressContext.jsx'
import instructorPhoto from '../assets/instructor-photo.jpg'

export default function Home() {
  const [topics, setTopics] = useState(null)
  const [error, setError] = useState(null)
  const { totalCompleted } = useProgress()

  function load() {
    setError(null)
    setTopics(null)
    getTopics()
      .then((data) => setTopics(data.topics))
      .catch((err) => setError(err.message))
  }

  useEffect(load, [])

  const totalLessons = topics
    ? topics.reduce(
        (sum, t) => sum + Object.values(t.levels).reduce((s, l) => s + l.lesson_count, 0),
        0
      )
    : null

  return (
    <>
      <section className="hero hero--profile">
        <div className="container hero__inner">
          <div className="hero__content">
            <span className="eyebrow eyebrow--dark">Basics → Intermediate → Pro</span>
            <p className="hero__hello">Hi, I'm</p>
            <h1 className="hero__name">Praneeth Dodedu</h1>
            <p className="hero__role">
              AI Engineering Lead building <span className="hero__role-highlight">GenAI, RAG &amp; agentic systems<span className="hero__cursor" aria-hidden="true" /></span>
            </p>
            <p className="hero__subtitle hero__subtitle--dark">
              This course is the structured, self-paced path I wish I'd had — from first
              principles to production-grade skills, taught through real lessons from systems
              I've actually shipped.
            </p>

            <div className="hero__cta-row">
              <a href="#choose-topic" className="btn btn--accent">
                Start learning
              </a>
              <Link to="/about" className="btn btn--outline-light">
                About the instructor →
              </Link>
            </div>

            {totalLessons !== null && (
              <div className="hero__stats hero__stats--dark">
                <div className="stat">
                  <span className="stat__value">{totalLessons}</span>
                  <span className="stat__label">lessons</span>
                </div>
                <div className="stat">
                  <span className="stat__value">4</span>
                  <span className="stat__label">topics</span>
                </div>
                <div className="stat">
                  <span className="stat__value">{totalCompleted}</span>
                  <span className="stat__label">completed</span>
                </div>
              </div>
            )}
          </div>

          <div className="hero__portrait">
            <span className="hero__portrait-ring" aria-hidden="true" />
            <span className="hero__portrait-dot hero__portrait-dot--1" aria-hidden="true" />
            <span className="hero__portrait-dot hero__portrait-dot--2" aria-hidden="true" />
            <img src={instructorPhoto} alt="Praneeth Dodedu" className="hero__portrait-img" />
            <span className="hero__portrait-vignette" aria-hidden="true" />
            {totalLessons !== null && (
              <div className="hero__floating-card">
                <span className="hero__floating-card-value">{totalLessons}</span>
                <span className="hero__floating-card-label">
                  Lessons across 4 topics
                  <br />
                  Basics to Pro
                </span>
              </div>
            )}
          </div>
        </div>
      </section>

      <section className="container section" id="choose-topic" style={{ scrollMarginTop: '80px' }}>
        <div className="section__header">
          <h2>Choose a topic</h2>
          <p>
            Each topic is organized into three levels so you can start wherever you are. Look for
            the <span className="field-note-hint">◆ From the field</span> callouts — real notes
            from production systems Praneeth has actually shipped.
          </p>
        </div>

        {error && <ErrorState message={`Couldn't load topics: ${error}`} onRetry={load} />}
        {!error && !topics && <Loader label="Loading topics…" />}

        {topics && (
          <div className="topic-grid">
            {topics.map((topic) => (
              <TopicCard key={topic.id} topic={topic} />
            ))}
          </div>
        )}
      </section>

      <section className="container section section--levels">
        <div className="section__header">
          <h2>How the levels work</h2>
        </div>
        <div className="level-explainer-grid">
          <div className="level-explainer" data-level="basics">
            <span className="level-pill" data-level="basics">Basics</span>
            <p>No prior AI knowledge needed. Build a solid mental model from first principles.</p>
          </div>
          <div className="level-explainer" data-level="intermediate">
            <span className="level-pill" data-level="intermediate">Intermediate</span>
            <p>You understand the fundamentals — go deeper into mechanisms and trade-offs.</p>
          </div>
          <div className="level-explainer" data-level="pro">
            <span className="level-pill" data-level="pro">Pro</span>
            <p>Advanced, production-grade concepts for building and evaluating real systems.</p>
          </div>
        </div>
      </section>
    </>
  )
}
