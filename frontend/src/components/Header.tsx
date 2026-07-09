import { NavLink } from "react-router-dom";

import "./Header.css";

export default function Header() {
  return (
    <header className="header">

      <div className="brand">

        <h1>AI-First CRM</h1>

        <p>
          Healthcare Professional Interaction Module
        </p>

      </div>

      <nav className="nav-links">

        <NavLink
          to="/"
          end
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/action-items"
        >
          Action Items
        </NavLink>

      </nav>

    </header>
  );
}