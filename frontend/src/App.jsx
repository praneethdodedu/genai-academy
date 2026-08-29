import { useEffect, useState } from 'react'
import { Route, Routes, useLocation } from 'react-router-dom'
import Navbar from './components/Navbar.jsx'
import Sidebar from './components/Sidebar.jsx'
import Footer from './components/Footer.jsx'
import Home from './pages/Home.jsx'
import TopicPage from './pages/TopicPage.jsx'
import LessonPage from './pages/LessonPage.jsx'
import InstructorPage from './pages/InstructorPage.jsx'
import NotFound from './pages/NotFound.jsx'

function App() {
  const location = useLocation()
  const [drawerOpen, setDrawerOpen] = useState(false)

  // Close the mobile drawer whenever the route changes.
  useEffect(() => {
    setDrawerOpen(false)
  }, [location.pathname])

  // Lock body scroll while the mobile drawer is open so the page behind it
  // doesn't scroll along with the drawer's own content.
  useEffect(() => {
    document.body.style.overflow = drawerOpen ? 'hidden' : ''
    return () => {
      document.body.style.overflow = ''
    }
  }, [drawerOpen])

  return (
    <>
      <Navbar drawerOpen={drawerOpen} onMenuClick={() => setDrawerOpen((v) => !v)} />

      <div className="app-shell">
        <Sidebar open={drawerOpen} onNavigate={() => setDrawerOpen(false)} />

        {drawerOpen && (
          <button
            type="button"
            className="sidebar__backdrop"
            aria-label="Close navigation"
            onClick={() => setDrawerOpen(false)}
          />
        )}

        <div className="app-shell__main">
          <main className="page-enter" key={location.pathname}>
            <Routes location={location}>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<InstructorPage />} />
              <Route path="/topics/:topicId" element={<TopicPage />} />
              <Route path="/topics/:topicId/:level/:lessonId" element={<LessonPage />} />
              <Route path="*" element={<NotFound />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </div>
    </>
  )
}

export default App
