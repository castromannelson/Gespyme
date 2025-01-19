import React from "react";
import "../css/Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Gespyme</div>
      <ul className="navbar-menu">
        <li><a href="/">Inicio</a></li>
        <li><a href="/productos">Productos</a></li>
        <li><a href="/usuarios">Usuarios</a></li>
        <li><a href="/logout">Cerrar Sesión</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
