import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getInstructor } from '../lib/api.js'
import Loader from '../components/Loader.jsx'
import ErrorState from '../components/ErrorState.jsx'
import instructorPhoto from '../assets/instructor-photo.jpg'

export default function InstructorPage() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  function load() {
    setError(null)
    setData(null)
    getInstructor()
      .then(setData)
      .catch((err) => setError(err.message))
  }

  useEffect(load, [])

  if (error) {
    return (
      <div className="container section">
        <ErrorState message={`Couldn't load instructor profile: ${error}`} onRetry={load} />
      </div>
    )
  }

  if (!data) {
    return (
      <div className="container section">
        <Loader label="Loading profile…" />
      </div>
    )
  }

  return (
    <>
      <section className="hero hero--profile hero--compact">
        <div className="container hero__inner">
          <div className="hero__content">
            <span className="eyebrow eyebrow--dark">Your instructor</span>
            <h1 className="hero__name hero__name--compact">{data.name}</h1>
            <p className="hero__role">{data.title}</p>
            <p className="hero__subtitle hero__subtitle--dark hero__location">{data.location}</p>
            <p className="hero__subtitle hero__subtitle--dark">{data.summary}</p>

            <div className="hero__cta-row">
              <a className="btn btn--accent" href={`mailto:${data.email}`}>
                Email {data.name.split(' ')[0]}
              </a>
              <a className="btn btn--outline-light" href={data.linkedin} target="_blank" rel="noreferrer">
                Connect on LinkedIn ↗
              </a>
            </div>
          </div>

          <div className="hero__portrait hero__portrait--compact">
            <span className="hero__portrait-ring" aria-hidden="true" />
            <span className="hero__portrait-dot hero__portrait-dot--1" aria-hidden="true" />
            <span className="hero__portrait-dot hero__portrait-dot--2" aria-hidden="true" />
            <img src={instructorPhoto} alt={data.name} className="hero__portrait-img" />
            <span className="hero__portrait-vignette" aria-hidden="true" />
          </div>
        </div>
      </section>

      <div className="container section instructor-page">
        <Link to="/" className="back-link">← Back to course</Link>

        <div className="instructor-stats">
          {data.stats.map((s) => (
            <div key={s.label} className="stat">
              <span className="stat__value">{s.value}</span>
              <span className="stat__label">{s.label}</span>
            </div>
          ))}
        </div>

        <section className="instructor-section">
        <h2>What I do</h2>
        <ul className="instructor-list">
          {data.what_i_do.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>
      </section>

      <section className="instructor-section">
        <h2>Selected work</h2>
        <div className="achievement-grid">
          {data.achievements.map((a) => (
            <div key={a.title} className="achievement-card">
              <h3>{a.title}</h3>
              <p>{a.detail}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="instructor-section">
        <h2>Skills</h2>
        <div className="skills-grid">
          {Object.entries(data.skills).map(([category, items]) => (
            <div key={category} className="skills-group">
              <h4>{category}</h4>
              <div className="skills-tags">
                {items.map((item) => (
                  <span key={item} className="skill-tag">
                    {item}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="instructor-section">
        <h2>Experience</h2>
        <div className="timeline">
          {data.experience.map((e, i) => (
            <div key={i} className="timeline-item">
              <div className="timeline-item__dot" aria-hidden="true" />
              <div className="timeline-item__body">
                <div className="timeline-item__header">
                  <h4>
                    {e.role} · {e.company}
                  </h4>
                  <span className="timeline-item__period">{e.period}</span>
                </div>
                {e.detail && <p>{e.detail}</p>}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="instructor-section">
        <h2>Domains</h2>
        <div className="skills-tags">
          {data.domains.map((d) => (
            <span key={d} className="skill-tag">
              {d}
            </span>
          ))}
        </div>
      </section>
      </div>
    </>
  )
}
