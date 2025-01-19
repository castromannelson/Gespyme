import React from "react";
import "../css/Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <ul className="sidebar-menu">
        <li><a href="/">Dashboard</a></li>
        <li><a href="/productos">Productos</a></li>
        <li><a href="/usuarios">Usuarios</a></li>
        <li><a href="/reportes">Reportes</a></li>
      </ul>
    </aside>
  );
};

export default Sidebar;
