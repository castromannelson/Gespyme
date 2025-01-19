import React from "react";
import "../css/LoginPage.css";

const LoginPage = () => {
  const onSubmit = (e) => {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
    console.log("Datos de login:", { username, password });
    // Aquí puedes agregar la lógica para redirigir al Dashboard
    window.location.href = "/dashboard"; 
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">Iniciar Sesión</h2>
        <form onSubmit={onSubmit}>
          <div className="form-group">
            <label htmlFor="username">Usuario</label>
            <input type="text" id="username" name="username" placeholder="Introduce tu usuario" required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Contraseña</label>
            <input type="password" id="password" name="password" placeholder="Introduce tu contraseña" required />
          </div>
          <button type="submit" className="login-button">Iniciar Sesión</button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
