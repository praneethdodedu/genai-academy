import { Link } from 'react-router-dom'
import { useProgress } from '../context/ProgressContext.jsx'

export default function LessonRow({ topicId, level, lesson }) {
  const { isCompleted } = useProgress()
  const done = isCompleted(lesson.id)

  return (
    <Link to={`/topics/${topicId}/${level}/${lesson.id}`} className="lesson-row">
      <span className={`lesson-row__check ${done ? 'lesson-row__check--done' : ''}`} aria-hidden="true">
        {done ? '✓' : ''}
      </span>
      <span className="lesson-row__body">
        <span className="lesson-row__title">{lesson.title}</span>
        <span className="lesson-row__summary">{lesson.summary}</span>
      </span>
      <span className="lesson-row__minutes">{lesson.minutes} min</span>
    </Link>
  )
}
