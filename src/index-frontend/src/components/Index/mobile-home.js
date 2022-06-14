import React, { Component } from "react";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Flashcards from '../../images/home/hand-flashcards.png';
import Fitnessing from '../../images/home/hand-fitnessing.png';

class MobileHome extends Component {
    render() {
        return (
            <Container fluid className="screen-size home-background">
                {/* <Row className="h-100">
                    <Col className="header-offset"></Col>
                    <Col className="px-0 align-self-start">
                        <img
                            id="flashcards"
                            src={Flashcards}
                        />
                    </Col>
                    <Col className="px-0 mx-0 align-self-end">
                        <img
                            id="fitnessing"
                            src={Fitnessing}
                        />
                    </Col>
                </Row> */}
            </Container>
        );
    }
}

export default MobileHome;