// src/api/auth.js

import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Cambia la URL según sea necesario

export const login = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}/login`, credentials);
        return response.data;
    } catch (error) {
        console.error('Error de autenticación', error);
        throw error;
    }
};

export const register = async (userData) => {
    try {
        const response = await axios.post(`${API_URL}/register`, userData);
        return response.data;
    } catch (error) {
        console.error('Error al registrar usuario', error);
        throw error;
    }
};
