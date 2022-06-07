import logo from './logo.svg';
import './App.css';
import Header from "./components/header"
import Project from "./components/project";
import React, { Component, Fragment } from "react";

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Project />
      </Fragment>
    );
  }
}

export default App;
