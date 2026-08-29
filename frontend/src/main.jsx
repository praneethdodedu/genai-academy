import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import './styles.css'
import App from './App.jsx'
import { ProgressProvider } from './context/ProgressContext.jsx'
import { NavProvider } from './context/NavContext.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <ProgressProvider>
        <NavProvider>
          <App />
        </NavProvider>
      </ProgressProvider>
    </BrowserRouter>
  </StrictMode>,
)
