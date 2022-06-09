import React, { Component } from "react";
import axios from "axios";

export default class Project extends Component {
    constructor(props) {
        super(props);
        this.state = {
            projects:[],
        };
        this.loadProjects = this.loadProjects.bind(this);
    }

    componentDidMount() {
        this.loadProjects();
    }

    async loadProjects() {
        const promise = await axios.get("http://127.0.0.1:8000/projects");
        const status = promise.status;
        if (status === 200) {
            const data = promise.data.projects;
            this.setState({projects:data});
        }
    }

    render() {
        return (
            <div>
                <p>Projects</p>
                {this.state.projects.map((project) => (
                <h4 key={project.pk}>{project.title}</h4>))}
            </div>
        )
    }
}
