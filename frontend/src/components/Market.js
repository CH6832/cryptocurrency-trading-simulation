// Market.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Market = () => {
  const [cryptos, setCryptos] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch all coins data
  useEffect(() => {
    const fetchCoins = async () => {
      try {
        const response = await axios.get('https://api.coingecko.com/api/v3/coins/markets', {
          params: {
            vs_currency: 'usd',
            order: 'market_cap_desc', // You can change the order
            per_page: 50, // Number of coins to display
            page: 1,
          },
        });

        setCryptos(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching coin data:', error);
        setLoading(false);
      }
    };

    fetchCoins();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="market-page container mt-4">
      <h2 className="text-center mb-4">Cryptocurrency Market</h2>
      <table className="table table-bordered table-hover">
        <thead className="thead-dark">
          <tr>
            <th>Rank</th>
            <th>Coin</th>
            <th>Price (USD)</th>
            <th>Market Cap</th>
            <th>24h Change</th>
          </tr>
        </thead>
        <tbody>
          {cryptos.map((crypto) => (
            <tr key={crypto.id}>
              <td>{crypto.market_cap_rank}</td>
              <td>
                <img src={crypto.image} alt={crypto.name} width="30" height="30" />
                {crypto.name}
              </td>
              <td>${crypto.current_price.toLocaleString()}</td>
              <td>${crypto.market_cap.toLocaleString()}</td>
              <td
                className={crypto.price_change_percentage_24h < 0 ? 'text-danger' : 'text-success'}
              >
                {crypto.price_change_percentage_24h.toFixed(2)}%
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Market;
