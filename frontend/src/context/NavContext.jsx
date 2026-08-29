import { createContext, useContext, useEffect, useState } from 'react'
import { getNav } from '../lib/api.js'

const NavContext = createContext(null)

export function NavProvider({ children }) {
  const [nav, setNav] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    getNav()
      .then(setNav)
      .catch((err) => setError(err.message))
  }, [])

  return <NavContext.Provider value={{ nav, error }}>{children}</NavContext.Provider>
}

export function useNav() {
  const ctx = useContext(NavContext)
  if (!ctx) throw new Error('useNav must be used within a NavProvider')
  return ctx
}
