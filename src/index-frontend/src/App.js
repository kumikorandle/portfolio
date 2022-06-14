import logo from './logo.svg';
import './App.css';
import Header from "./components/header"
import Home from "./components/Index/home"
import Project from "./components/Project/index";
import React, { Component, Fragment } from "react";
import {ViewportProvider} from './utils/viewport-provider'
import { BrowserRouter as Router, Route, Link, Routes, BrowserRouter} from "react-router-dom";



class App extends Component {
  render() {
    return (
      <Fragment>
          <Header />
          <ViewportProvider>
            <Home />
          </ViewportProvider>
          <Project/>
      </Fragment>
      // <BrowserRouter>
      //   <Routes>
      //     <Route path="/" element={<Project />} />
      //   </Routes>
      // </BrowserRouter>
    );
  }
}

export default App;
