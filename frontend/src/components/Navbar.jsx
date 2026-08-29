import { useEffect, useRef, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { search as searchApi } from '../lib/api.js'
import { IconMenu, IconClose } from './icons.jsx'

export default function Navbar({ drawerOpen, onMenuClick }) {
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
      <div className="navbar__inner">
        <button
          type="button"
          className="navbar__menu-btn"
          aria-label={drawerOpen ? 'Close navigation' : 'Open navigation'}
          aria-expanded={drawerOpen}
          onClick={onMenuClick}
        >
          {drawerOpen ? <IconClose width={20} height={20} /> : <IconMenu width={20} height={20} />}
        </button>

        <Link to="/" className="navbar__brand">
          <span className="navbar__logo" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none">
              <path
                d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z"
                fill="#fff"
              />
            </svg>
          </span>
          <span>GenAI Academy</span>
        </Link>

        <div className="navbar__search" ref={boxRef}>
          <svg className="navbar__search-icon" viewBox="0 0 24 24" width="15" height="15" fill="none" aria-hidden="true">
            <circle cx="11" cy="11" r="7" stroke="currentColor" strokeWidth="1.75" />
            <path d="M21 21l-4.3-4.3" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" />
          </svg>
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

        <Link to="/about" className="navbar__link">
          About
        </Link>
      </div>
    </header>
  )
}
