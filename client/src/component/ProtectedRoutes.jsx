import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext"; // Adjust the import path as necessary

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth(); // Use the auth context

  return isAuthenticated ? children : <Navigate to="/login" />; // Redirect to login if not authenticated
};

export default ProtectedRoute;