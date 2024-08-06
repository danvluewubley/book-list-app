import React, { createContext, useContext, useState } from "react";

// Create an AuthContext
const AuthContext = createContext();

// Custom provider component
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false); // Track authentication state

  const login = () => setIsAuthenticated(true); // Function to log in
  const logout = () => setIsAuthenticated(false); // Function to log out

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use auth context
export const useAuth = () => useContext(AuthContext);