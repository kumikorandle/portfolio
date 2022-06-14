import React, { Component, useEffect, useState } from "react";
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'
import logo from '../Memoji.PNG'
import github from '../images/header/Github-logo.svg'
import insta from '../images/header/Instagram-logo.svg'
import linkedin from '../images/header/Linkedin-logo.svg'


class Header extends Component {
    componentDidMount() {
        window.addEventListener("scroll", this.resizeHeaderOnScroll);
    }

    resizeHeaderOnScroll() {
        const distanceY = window.pageYOffset || document.documentElement.scrollTop,
        header = document.getElementById("header");
        var shrinkHeight = header.offsetHeight;
    
        if (distanceY > shrinkHeight) {
            header.classList.add("py-0");
            header.classList.remove("py-2");

        } else {
            header.classList.add("py-2");
            header.classList.remove("py-0");
        }
      }
    
    render() {
        return (
            <Navbar expand='lg' variant="dark" id="header" className="py-2">
                <Container fluid>
                    <Navbar.Brand href="#home" className="ms-2">
                        <img
                            id = "logo"
                            src={logo}
                            alt="Kumiko Randle Memoji logo"
                        />
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav"/>
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mx-auto" >
                            <Nav.Link href="#home" className="px-3">Home</Nav.Link>
                            <Nav.Link href="#projects" className="px-3">Projects</Nav.Link>
                            <Nav.Link href="#about" className="px-3">About me</Nav.Link>
                            <Nav.Link href="#skills" className="px-3">Skills</Nav.Link>
                            <Nav.Link href="#contact" className="px-3">Contact me</Nav.Link>
                        </Nav>

                        <Nav className="ml-auto my-auto inline-links">
                            <Nav.Link href="https://www.instagram.com/kumikorandle/" className="px-3 inline-links">
                                <img
                                    src={insta}
                                    alt="Instagram logo"
                                />
                            </Nav.Link>
                            <Nav.Link href="https://github.com/kumikorandle" className="px-3 inline-links">
                                <img
                                    src={github}
                                    alt="Github logo"
                                />
                            </Nav.Link>
                            <Nav.Link href="https://www.linkedin.com/in/kumikorandle/" className="px-3 inline-links">
                                <img
                                    src={linkedin}
                                    alt="Linkedin logo"
                                />
                            </Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                    
                </Container>
            </Navbar>
        );
    }
}

export default Header;