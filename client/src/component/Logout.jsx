import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { useAuth } from './AuthContext'; // Adjust the import path

function Logout() {
  const { logout } = useAuth();

  const navigate = useNavigate();

  useEffect(() => {
    const handleLogout = async () => {
      try {
        const response = await axios.post("http://localhost:8080/logout");
        logout();
        navigate("/");
      } catch (error) {
        if (error.response) {
          console.error(error.response.data.error);
        } else {
          console.error("An error occurred.");
        }
      }
    };

    handleLogout();
  }, [navigate, logout]);

  return null;
}

export default Logout;