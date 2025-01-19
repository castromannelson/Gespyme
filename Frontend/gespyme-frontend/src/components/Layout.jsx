import React from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import "../css/Layout.css";

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Navbar />
      <Sidebar />
      <main className="content">{children}</main>
    </div>
  );
};

export default Layout;
