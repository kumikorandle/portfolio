import logo from './logo.svg';
import './App.css';
import Header from "./components/header"
import Project from "./components/Project/index";
import React, { Component, Fragment } from "react";
import { BrowserRouter as Router, Route, Link, Routes, BrowserRouter} from "react-router-dom";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Project />} />
        </Routes>
      </BrowserRouter>
    );
  }
}

export default App;
