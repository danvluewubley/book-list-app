import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignupForm from "./component/SignupForm";
import LoginForm from "./component/LoginForm";
import Dashboard from "./component/Dashboard";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Welcome to the Signup Page</h1>
        </header>
        <SignupForm />
        <LoginForm />
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
