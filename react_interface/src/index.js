import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Plan from './Pages/Plan';
import Plans from './Pages/Plans';
import Suite from './Pages/Suite';
import Case from './Pages/Case';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <>
    <Router>
      <Routes>
        <Route path="/" element={<App />}/>
        <Route path="/plans" element={<Plans />}/>
        <Route path="/plan" element={<Plan />}/>
        <Route path="/suite" element={<Suite />}/>
        <Route path="/case" element={<Case />}/>
      </Routes>
    </Router>

  </>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
