import React, { useState, useEffect } from 'react';

const AllPrices = () => {
  const [cryptoPrices, setCryptoPrices] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch the prices from the backend API
    const fetchPrices = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/crypto/all');
        const data = await response.json();
        
        if (response.ok) {
          setCryptoPrices(data);
        } else {
          setError('Failed to fetch cryptocurrency prices');
        }
      } catch (error) {
        setError('Error fetching data');
      }
    };

    fetchPrices();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!cryptoPrices) {
    return <div>Loading prices...</div>;
  }

  return (
    <div className="price-chart">
      <h3>Current Cryptocurrency - All Prices</h3>
      <ul>
        <li>Bitcoin: ${cryptoPrices.bitcoin?.usd}</li>
        <li>Ethereum: ${cryptoPrices.ethereum?.usd}</li>
        <li>Litecoin: ${cryptoPrices.litecoin?.usd}</li>
      </ul>
    </div>
  );
};

export default AllPrices;
