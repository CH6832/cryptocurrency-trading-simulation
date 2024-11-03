import React, { useEffect, useState } from 'react';
import { useAPI } from '../hooks/useAPI';

function PortfolioView() {
    const [portfolio, setPortfolio] = useState([]);
    const api = useAPI();

    useEffect(() => {
        async function fetchPortfolio() {
            try {
                const response = await api.get('/api/portfolio');
                setPortfolio(response.data);
            } catch (error) {
                console.error('Failed to fetch portfolio:', error);
            }
        }
        fetchPortfolio();
    }, [api]);

    return (
        <div>
            <h2>Your Portfolio</h2>
            <ul>
                {portfolio.map((item) => (
                    <li key={item.symbol}>{item.symbol}: {item.amount}</li>
                ))}
            </ul>
        </div>
    );
}

export default PortfolioView;
