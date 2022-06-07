import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class Project extends Component {
  state = {
    projects: []
  };
  
  getProjects = () => {
    axios.get(API_URL).then(res => this.setState({ projects: res.data }));
  };

  // resetState = () => {
  //   this.getProjects();
  // };

  render() {
    return(
      <p>Hello world</p>
    );
  }
}

export default Project;