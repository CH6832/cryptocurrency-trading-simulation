import React from 'react';
import { Navbar, Container, Nav, Button } from 'react-bootstrap';

// Header Component with modern style
const Header = () => {
  return (
    <header>
      {/* Navbar with modern Bootstrap design */}
      <Navbar bg="primary" variant="dark" expand="lg" className="shadow-lg">
        <Container>

          {/* Navbar Toggle for smaller screens */}
          <Navbar.Toggle aria-controls="navbar-nav" />

          {/* Navbar Items */}
          <Navbar.Collapse id="navbar-nav">
            <Nav className="ml-auto">
              <Nav.Link href="/market" className="text-white">Market</Nav.Link>
              <Nav.Link href="#trades" className="text-white">Trades</Nav.Link>
              <Nav.Link href="#portfolio" className="text-white">Portfolio</Nav.Link>
              <Nav.Link href="#help" className="text-white">Help</Nav.Link>
              <Nav.Item>
                <Button variant="outline-light" className="btn-sm">Sign in</Button>
              </Nav.Item>
              <Nav.Item>
                <Button variant="outline-light" className="btn-sm">Login</Button>
              </Nav.Item>
              <Nav.Item>
                <Button variant="outline-light" className="btn-sm">Logout</Button>
              </Nav.Item>
              <Nav.Item>
                <Button variant="outline-light" className="btn-sm">Change Password</Button>
              </Nav.Item>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
};

// UserManagement Component with modern styling
// const UserManagement = () => (
//   <div className="user-management d-flex justify-content-between flex-wrap my-4">
//     <button className="btn btn-outline-success btn-lg">Sign In</button>
//     <button className="btn btn-outline-info btn-lg">Sign Up</button>
//     <button className="btn btn-outline-warning btn-lg">My Profile</button>
//     <button className="btn btn-outline-danger btn-lg">Change Password</button>
//   </div>
// );

// Navigation Component with modern styling
const Navigation = () => (
  <div className="navigation d-flex justify-content-center my-4">
    <button className="btn btn-outline-secondary btn-lg mx-3">Home</button>
    <button className="btn btn-outline-secondary btn-lg mx-3">Market</button>
    <button className="btn btn-outline-secondary btn-lg mx-3">Trades</button>
    <button className="btn btn-outline-secondary btn-lg mx-3">Portfolio</button>
    <button className="btn btn-outline-secondary btn-lg mx-3">Help</button>
  </div>
);

// Combined Dashboard Component
const Dashboard = () => (
  <div>
    {/* Header */}
    <Header />
    
    {/* User Management and Navigation Section */}
    <section className="container">
      {/* <UserManagement /> */}
      {/* <Navigation /> */}
    </section>
  </div>
);

export default Dashboard;
