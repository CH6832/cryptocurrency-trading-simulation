// Run the app:
// 
// set NODE_OPTIONS=--openssl-legacy-provider
// npm start
// npm list react-scripts
// npm install react-scripts
// npm cache clean --force
// npm update
// npm start
// import logo from './logo.svg';

import React from 'react';
import Header from './components/Header';
import Navigation from './components/Navigation';
import UserManagement from './components/UserManagement';
import PriceChart from './components/PriceChart';
import ExecuteTrade from './components/ExecuteTrade';
import PortfolioOverview from './components/PortfolioOverview';
import Footer from './components/Footer';
import './App.css';

function App() {
    return (
        <div className="dashboard">
            <UserManagement />
            <Header />
            <Navigation />
            <PriceChart />
            <ExecuteTrade />
            <PortfolioOverview />
            <button>Logout</button>
            <Footer />
        </div>
    );
}

export default App;