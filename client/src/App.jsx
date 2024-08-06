import React, { Suspense, lazy } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./component/Navbar";
import "./index.css";

const Home = lazy(() => import("./component/Home"));
const Signup = lazy(() => import("./component/Signup"));

function App() {
  return (
    <Router>
      <Navbar />
      <main>
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </Suspense>
      </main>
    </Router>
  );
}

export default App;