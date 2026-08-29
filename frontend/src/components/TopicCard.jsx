import { Link } from 'react-router-dom'
import { TOPIC_ICONS, IconArrowRight } from './icons.jsx'

// Note: the /api/topics list endpoint only returns lesson counts (not full
// lesson ids) to keep the payload small, so this card shows lesson counts
// per level rather than a completion percentage. Per-lesson progress is
// shown once you're inside a topic (TopicPage), where full lesson lists
// (including ids) are loaded.
export default function TopicCard({ topic }) {
  const totalLessons = Object.values(topic.levels || {}).reduce(
    (sum, lvl) => sum + (lvl.lesson_count ?? 0),
    0
  )
  const Icon = TOPIC_ICONS[topic.id]

  return (
    <Link to={`/topics/${topic.id}`} className="topic-card" style={{ '--topic-color': topic.color }}>
      <div className="topic-card__top">
        <span className="topic-card__icon">{Icon && <Icon width={20} height={20} />}</span>
        <h3>{topic.name}</h3>
      </div>
      <p className="topic-card__tagline">{topic.tagline}</p>
      <div className="topic-card__levels">
        {Object.entries(topic.levels || {}).map(([key, lvl]) => (
          <span key={key} className="level-pill" data-level={key}>
            {lvl.label}
          </span>
        ))}
      </div>
      <div className="topic-card__footer">
        <span>{totalLessons} lessons</span>
        <span className="topic-card__arrow" aria-hidden="true">
          <IconArrowRight width={15} height={15} />
        </span>
      </div>
    </Link>
  )
}
