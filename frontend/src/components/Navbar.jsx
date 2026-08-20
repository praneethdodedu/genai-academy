import { useEffect, useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { search as searchApi } from '../lib/api.js'

export default function Navbar() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [open, setOpen] = useState(false)
  const boxRef = useRef(null)
  const navigate = useNavigate()

  useEffect(() => {
    function onClickOutside(e) {
      if (boxRef.current && !boxRef.current.contains(e.target)) {
        setOpen(false)
      }
    }
    document.addEventListener('mousedown', onClickOutside)
    return () => document.removeEventListener('mousedown', onClickOutside)
  }, [])

  useEffect(() => {
    const q = query.trim()
    if (!q) {
      setResults([])
      return
    }
    const handle = setTimeout(() => {
      searchApi(q)
        .then((data) => setResults(data.results || []))
        .catch(() => setResults([]))
    }, 200)
    return () => clearTimeout(handle)
  }, [query])

  function goToResult(r) {
    setOpen(false)
    setQuery('')
    navigate(`/topics/${r.topic_id}/${r.level}/${r.id}`)
  }

  return (
    <header className="navbar">
      <div className="container navbar__inner">
        <Link to="/" className="navbar__brand">
          <span className="navbar__logo" aria-hidden="true">◆</span>
          <span>GenAI Academy</span>
        </Link>

        <div className="navbar__search" ref={boxRef}>
          <input
            type="search"
            placeholder="Search lessons…"
            value={query}
            onChange={(e) => {
              setQuery(e.target.value)
              setOpen(true)
            }}
            onFocus={() => setOpen(true)}
            aria-label="Search lessons"
          />
          {open && query.trim() && (
            <div className="navbar__search-results">
              {results.length === 0 ? (
                <div className="navbar__search-empty">No lessons found for "{query}"</div>
              ) : (
                results.map((r) => (
                  <button
                    key={`${r.topic_id}-${r.level}-${r.id}`}
                    type="button"
                    className="navbar__search-result"
                    onClick={() => goToResult(r)}
                  >
                    <span className="navbar__search-result-title">{r.title}</span>
                    <span className="navbar__search-result-meta">
                      {r.topic_name} · {r.level}
                    </span>
                  </button>
                ))
              )}
            </div>
          )}
        </div>
      </div>
    </header>
  )
}
