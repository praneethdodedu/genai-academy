import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <footer className="footer">
      <div className="container footer__inner">
        <div>
          <p>GenAI Academy — learn AI, GenAI, RAG, and Prompt Engineering, from basics to pro.</p>
          <p className="footer__muted">
            A course by Praneeth Dodedu, AI Engineering Lead. Built with React + FastAPI.
          </p>
        </div>
        <div className="footer__links">
          <Link to="/about">About the instructor</Link>
          <a href="https://www.linkedin.com/in/praneethdodedu" target="_blank" rel="noreferrer">
            LinkedIn ↗
          </a>
          <a href="mailto:praneeth.dodedu@gmail.com">Email</a>
        </div>
      </div>
    </footer>
  )
}
