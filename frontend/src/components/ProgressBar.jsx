export default function ProgressBar({ value, total, color }) {
  const pct = total > 0 ? Math.round((value / total) * 100) : 0
  return (
    <div className="progress-bar" role="progressbar" aria-valuenow={pct} aria-valuemin={0} aria-valuemax={100}>
      <div
        className="progress-bar__fill"
        style={{ width: `${pct}%`, background: color || 'var(--color-primary)' }}
      />
    </div>
  )
}
