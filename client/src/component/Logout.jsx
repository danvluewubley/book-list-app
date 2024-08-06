import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

function Logout() {
  const navigate = useNavigate();

  useEffect(() => {
    const logout = async () => {
      try {
        const response = await axios.post("http://localhost:8080/logout");
        navigate("/");
      } catch (error) {
        if (error.response) {
          console.error(error.response.data.error);
        } else {
          console.error("An error occurred.");
        }
      }
    };

    logout();
  }, [navigate]);

  return null;
}

export default Logout;