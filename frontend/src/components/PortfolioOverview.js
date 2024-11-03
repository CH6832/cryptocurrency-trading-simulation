// components/PortfolioOverview.js

import React from 'react';

const PortfolioOverview = () => {
    // Example portfolio data; this could come from props, context, or an API call.
    const portfolioData = [
        { asset: 'Bitcoin (BTC)', quantity: 0.5, value: '$25,000' },
        { asset: 'Ethereum (ETH)', quantity: 2.0, value: '$4,000' },
        { asset: 'Litecoin (LTC)', quantity: 5.0, value: '$750' },
    ];

    const totalValue = portfolioData.reduce((total, item) => {
        const value = parseFloat(item.value.replace(/[$,]/g, ''));
        return total + value;
    }, 0);

    return (
        <div className="portfolio-overview">
            <h2>Portfolio Overview</h2>
            <table>
                <thead>
                    <tr>
                        <th>Asset</th>
                        <th>Quantity</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {portfolioData.map((item, index) => (
                        <tr key={index}>
                            <td>{item.asset}</td>
                            <td>{item.quantity}</td>
                            <td>{item.value}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <div className="total-value">
                <strong>Total Value: ${totalValue.toLocaleString()}</strong>
            </div>
        </div>
    );
};

export default PortfolioOverview;
