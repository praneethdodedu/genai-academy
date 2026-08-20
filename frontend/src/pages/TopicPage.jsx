import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { getTopic } from '../lib/api.js'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import ProgressBar from '../components/ProgressBar.jsx'
import LessonRow from '../components/LessonRow.jsx'
import { useProgress } from '../context/ProgressContext.jsx'

const LEVEL_ORDER = ['basics', 'intermediate', 'pro']

export default function TopicPage() {
  const { topicId } = useParams()
  const [topic, setTopic] = useState(null)
  const [error, setError] = useState(null)
  const [activeLevel, setActiveLevel] = useState('basics')
  const { completedCount } = useProgress()

  function load() {
    setError(null)
    setTopic(null)
    getTopic(topicId)
      .then(setTopic)
      .catch((err) => setError(err.message))
  }

  useEffect(load, [topicId])

  if (error) {
    return (
      <div className="container section">
        <ErrorState message={`Couldn't load this topic: ${error}`} onRetry={load} />
      </div>
    )
  }

  if (!topic) {
    return (
      <div className="container section">
        <Loader label="Loading topic…" />
      </div>
    )
  }

  const level = topic.levels[activeLevel]
  const lessonIds = level.lessons.map((l) => l.id)
  const done = completedCount(lessonIds)

  return (
    <div className="container section">
      <Link to="/" className="back-link">← All topics</Link>

      <div className="topic-header" style={{ '--topic-color': topic.color }}>
        <span className="topic-header__dot" />
        <div>
          <h1>{topic.name}</h1>
          <p className="topic-header__tagline">{topic.tagline}</p>
        </div>
      </div>

      <div className="level-tabs" role="tablist">
        {LEVEL_ORDER.map((key) => (
          <button
            key={key}
            type="button"
            role="tab"
            aria-selected={activeLevel === key}
            className={`level-tab ${activeLevel === key ? 'level-tab--active' : ''}`}
            onClick={() => setActiveLevel(key)}
          >
            {topic.levels[key].label}
            <span className="level-tab__count">{topic.levels[key].lessons.length}</span>
          </button>
        ))}
      </div>

      <div className="level-panel">
        <p className="level-panel__description">{level.description}</p>

        <div className="level-panel__progress">
          <span>
            {done}/{lessonIds.length} complete
          </span>
          <ProgressBar value={done} total={lessonIds.length} color={topic.color} />
        </div>

        <div className="lesson-list">
          {level.lessons.map((lesson) => (
            <LessonRow key={lesson.id} topicId={topic.id} level={activeLevel} lesson={lesson} />
          ))}
        </div>
      </div>
    </div>
  )
}
