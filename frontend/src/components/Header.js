import React from 'react';
import { Navbar, Container, Nav, Button } from 'react-bootstrap';

const Header = () => {
    return (
        <header>
            {/* Navbar Component */}
            <Navbar bg="light" expand="lg" className="shadow-sm">
                <Container>
                    {/* Brand Logo/Title */}
                    <Navbar.Brand href="#home" className="font-weight-bold text-primary">
                        Crypto Trading Dashboard
                    </Navbar.Brand>

                    {/* Toggle button for mobile */}
                    <Navbar.Toggle aria-controls="navbar-nav" />

                    {/* Navbar items */}
                    <Navbar.Collapse id="navbar-nav">
                        <Nav className="ml-auto">
                            <Nav.Link href="#home" className="nav-link">Home</Nav.Link>
                            <Nav.Link href="#features" className="nav-link">Features</Nav.Link>
                            <Nav.Link href="#about" className="nav-link">About</Nav.Link>
                            <Nav.Link href="#contact" className="nav-link">Contact</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    );
};

export default Header;
