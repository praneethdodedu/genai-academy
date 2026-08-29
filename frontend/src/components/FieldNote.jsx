import { IconSpark } from './icons.jsx'

export default function FieldNote({ note }) {
  if (!note) return null

  return (
    <div className="field-note">
      <div className="field-note__header">
        <span className="field-note__icon" aria-hidden="true">
          <IconSpark width={13} height={13} />
        </span>
        <span className="field-note__label">From the field — {note.project}</span>
      </div>
      <p>{note.text}</p>
    </div>
  )
}
