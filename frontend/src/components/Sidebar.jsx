import { useEffect, useMemo, useState } from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import { useNav } from '../context/NavContext.jsx'
import { useProgress } from '../context/ProgressContext.jsx'
import { TOPIC_ICONS, IconChevronDown, IconCheck, IconHome } from './icons.jsx'

const LEVEL_ORDER = ['basics', 'intermediate', 'pro']

export default function Sidebar({ open, onNavigate }) {
  const { nav } = useNav()
  const { isCompleted } = useProgress()
  const location = useLocation()
  const [expanded, setExpanded] = useState(() => new Set())

  const activeTopicId = useMemo(() => {
    const match = /^\/topics\/([^/]+)/.exec(location.pathname)
    return match ? match[1] : null
  }, [location.pathname])

  // Auto-expand whichever topic the current route belongs to.
  useEffect(() => {
    if (!activeTopicId) return
    setExpanded((prev) => {
      if (prev.has(activeTopicId)) return prev
      const next = new Set(prev)
      next.add(activeTopicId)
      return next
    })
  }, [activeTopicId])

  function toggleTopic(topicId) {
    setExpanded((prev) => {
      const next = new Set(prev)
      if (next.has(topicId)) {
        next.delete(topicId)
      } else {
        next.add(topicId)
      }
      return next
    })
  }

  return (
    <aside className={`sidebar ${open ? 'sidebar--open' : ''}`} aria-label="Curriculum navigation">
      <div className="sidebar__scroll">
        <NavLink to="/" end className="sidebar__home" onClick={onNavigate}>
          <IconHome width={16} height={16} />
          <span>All topics</span>
        </NavLink>

        {!nav && (
          <div className="sidebar__loading">
            {[0, 1, 2, 3].map((i) => (
              <div key={i} className="sidebar__skeleton" />
            ))}
          </div>
        )}

        {nav &&
          nav.topics.map((topic) => {
            const Icon = TOPIC_ICONS[topic.id]
            const isExpanded = expanded.has(topic.id)
            const isActiveTopic = topic.id === activeTopicId
            return (
              <div
                key={topic.id}
                className={`sidebar__group ${isActiveTopic ? 'sidebar__group--active' : ''}`}
                style={{ '--topic-color': topic.color }}
              >
                <button
                  type="button"
                  className="sidebar__group-header"
                  aria-expanded={isExpanded}
                  onClick={() => toggleTopic(topic.id)}
                >
                  <span className="sidebar__group-icon">{Icon && <Icon width={16} height={16} />}</span>
                  <span className="sidebar__group-name">{topic.name}</span>
                  <IconChevronDown
                    width={14}
                    height={14}
                    className={`sidebar__chevron ${isExpanded ? 'sidebar__chevron--open' : ''}`}
                  />
                </button>

                {isExpanded && (
                  <div className="sidebar__group-body">
                    {LEVEL_ORDER.map((level) => {
                      const levelData = topic.levels[level]
                      if (!levelData || levelData.lessons.length === 0) return null
                      return (
                        <div key={level} className="sidebar__level">
                          <p className="sidebar__level-label">{levelData.label}</p>
                          <ul className="sidebar__lesson-list">
                            {levelData.lessons.map((lesson) => (
                              <li key={lesson.id}>
                                <NavLink
                                  to={`/topics/${topic.id}/${level}/${lesson.id}`}
                                  className={({ isActive }) =>
                                    `sidebar__lesson ${isActive ? 'sidebar__lesson--active' : ''}`
                                  }
                                  onClick={onNavigate}
                                >
                                  <span
                                    className={`sidebar__lesson-dot ${
                                      isCompleted(lesson.id) ? 'sidebar__lesson-dot--done' : ''
                                    }`}
                                    aria-hidden="true"
                                  >
                                    {isCompleted(lesson.id) && <IconCheck width={11} height={11} />}
                                  </span>
                                  <span className="sidebar__lesson-title">{lesson.title}</span>
                                </NavLink>
                              </li>
                            ))}
                          </ul>
                        </div>
                      )
                    })}
                  </div>
                )}
              </div>
            )
          })}
      </div>

      <div className="sidebar__footer">
        <NavLink to="/about" className="sidebar__footer-link" onClick={onNavigate}>
          About the instructor
        </NavLink>
      </div>
    </aside>
  )
}
