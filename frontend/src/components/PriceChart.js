import React, { useState, useEffect } from 'react';

const PriceChart = () => {
  const [cryptoPrices, setCryptoPrices] = useState(null);
  const [selectedCrypto, setSelectedCrypto] = useState('bitcoin');
  const [cryptoPrice, setCryptoPrice] = useState(null);

  // Fetch all cryptocurrency prices on component mount
  useEffect(() => {
    const fetchAllCryptoPrices = async () => {
      try {
        // Fetch prices for all cryptocurrencies
        const response = await fetch('http://127.0.0.1:8000/crypto/all');
        
        if (!response.ok) {
          throw new Error('Failed to fetch the data');
        }
        
        const data = await response.json();
        
        // Set all the prices to state
        setCryptoPrices(data);
        
        // Set the price for the selected cryptocurrency
        setCryptoPrice(data[selectedCrypto]?.usd || null);
      } catch (error) {
        console.error('Error fetching crypto prices:', error);
      }
    };

    fetchAllCryptoPrices();
  }, []); // Run only once when the component mounts

  // Fetch the selected cryptocurrency price when it changes
  useEffect(() => {
    if (cryptoPrices) {
      setCryptoPrice(cryptoPrices[selectedCrypto]?.usd || null);
    }
  }, [selectedCrypto, cryptoPrices]); // Re-fetch when selectedCrypto or cryptoPrices changes

  return (
    <div className="price-chart">
      <h2>Select Cryptocurrency:</h2>
      <br />
      <select
        value={selectedCrypto}
        onChange={(e) => setSelectedCrypto(e.target.value)}
      >
        <option value="bitcoin">Bitcoin (BTC)</option>
        <option value="ethereum">Ethereum (ETH)</option>
        <option value="litecoin">Litecoin (LTC)</option>
      </select>
      <br /><br /><br />
      
      <div className="chart-container">
        {/* Display price of selected cryptocurrency */}
        {cryptoPrice !== null ? (
          <div>
            <h3>{selectedCrypto.charAt(0).toUpperCase() + selectedCrypto.slice(1)} Price:</h3>
            <p>${cryptoPrice}</p>
          </div>
        ) : (
          <p>Loading...</p>
        )}

        {/* Show prices for all cryptocurrencies */}
        {cryptoPrices && (
          <div>
             {/* <h4>All Cryptocurrency Prices:</h4>
             <ul>
               <li>Bitcoin (BTC): ${cryptoPrices.bitcoin?.usd}</li>
               <li>Ethereum (ETH): ${cryptoPrices.ethereum?.usd}</li>
               <li>Litecoin (LTC): ${cryptoPrices.litecoin?.usd}</li>
             </ul> */}
          </div>
        )}
      </div>
    </div>
  );
};

export default PriceChart;
