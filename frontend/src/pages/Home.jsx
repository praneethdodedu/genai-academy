import { useEffect, useState } from 'react'
import { getTopics } from '../lib/api.js'
import TopicCard from '../components/TopicCard.jsx'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import { useProgress } from '../context/ProgressContext.jsx'

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
      <section className="hero">
        <div className="container hero__inner">
          <span className="eyebrow">Basics → Intermediate → Pro</span>
          <h1>Learn AI, GenAI, RAG &amp; Prompt Engineering</h1>
          <p className="hero__subtitle">
            A structured, self-paced path from first principles to production-grade skills —
            covering how AI actually works, how generative models create content, how to ground
            them in real data with RAG, and how to prompt them effectively.
          </p>
          {totalLessons !== null && (
            <div className="hero__stats">
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
      </section>

      <section className="container section">
        <div className="section__header">
          <h2>Choose a topic</h2>
          <p>Each topic is organized into three levels so you can start wherever you are.</p>
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
