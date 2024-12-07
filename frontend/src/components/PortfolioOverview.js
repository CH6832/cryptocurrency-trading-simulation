import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PortfolioOverview = () => {
  // Expanded portfolio data with 10 different cryptocurrencies
  const [portfolioData, setPortfolioData] = useState([
    { asset: 'Bitcoin (BTC)', quantity: 0.5, value: 0 },
    { asset: 'Ethereum (ETH)', quantity: 2.0, value: 0 },
    { asset: 'Litecoin (LTC)', quantity: 5.0, value: 0 },
    { asset: 'Ripple (XRP)', quantity: 1000, value: 0 },
    { asset: 'Bitcoin Cash (BCH)', quantity: 1.5, value: 0 },
    { asset: 'Cardano (ADA)', quantity: 3000, value: 0 },
    { asset: 'Polkadot (DOT)', quantity: 50, value: 0 },
    { asset: 'Chainlink (LINK)', quantity: 20, value: 0 },
    { asset: 'Dogecoin (DOGE)', quantity: 15000, value: 0 },
    { asset: 'Stellar (XLM)', quantity: 2000, value: 0 },
  ]);

  // Example prices (USD) for 10 coins
  const [prices, setPrices] = useState({
    bitcoin: 99888,     // Example price for Bitcoin
    ethereum: 4010.86,  // Example price for Ethereum
    litecoin: 137.09,   // Example price for Litecoin
    ripple: 0.50,       // Example price for Ripple
    bitcoinCash: 550.0, // Example price for Bitcoin Cash
    cardano: 1.25,      // Example price for Cardano
    polkadot: 5.0,      // Example price for Polkadot
    chainlink: 25.0,    // Example price for Chainlink
    dogecoin: 0.06,     // Example price for Dogecoin
    stellar: 0.12,      // Example price for Stellar
  });

  // Fetch live price data (from backend or directly from API)
  useEffect(() => {
    const fetchPrices = async () => {
      try {
        // Example API response simulation
        // Replace with the actual API URL to fetch live data
        const response = await axios.get('http://localhost:8000/api/portfolio');

        // Assuming the response has the same structure as the example data
        const { bitcoin, ethereum, litecoin, ripple, bitcoinCash, cardano, polkadot, chainlink, dogecoin, stellar } = response.data;

        setPrices({
          bitcoin: bitcoin.usd,
          ethereum: ethereum.usd,
          litecoin: litecoin.usd,
          ripple: ripple.usd,
          bitcoinCash: bitcoinCash.usd,
          cardano: cardano.usd,
          polkadot: polkadot.usd,
          chainlink: chainlink.usd,
          dogecoin: dogecoin.usd,
          stellar: stellar.usd,
        });
      } catch (error) {
        console.error('Error fetching price data', error);
      }
    };

    // Fetch prices every 10 seconds (or use a more appropriate interval)
    const interval = setInterval(fetchPrices, 10000);

    // Initial fetch
    fetchPrices();

    // Clean up the interval when the component is unmounted
    return () => clearInterval(interval);
  }, []);

  // Update portfolio values based on live prices
  const updatePortfolioValues = () => {
    return portfolioData.map(item => {
      let price = 0;
      if (item.asset.includes('Bitcoin')) {
        price = prices.bitcoin;
      } else if (item.asset.includes('Ethereum')) {
        price = prices.ethereum;
      } else if (item.asset.includes('Litecoin')) {
        price = prices.litecoin;
      } else if (item.asset.includes('Ripple')) {
        price = prices.ripple;
      } else if (item.asset.includes('Bitcoin Cash')) {
        price = prices.bitcoinCash;
      } else if (item.asset.includes('Cardano')) {
        price = prices.cardano;
      } else if (item.asset.includes('Polkadot')) {
        price = prices.polkadot;
      } else if (item.asset.includes('Chainlink')) {
        price = prices.chainlink;
      } else if (item.asset.includes('Dogecoin')) {
        price = prices.dogecoin;
      } else if (item.asset.includes('Stellar')) {
        price = prices.stellar;
      }
      return { ...item, value: (item.quantity * price).toFixed(2) };
    });
  };

  // Get the updated portfolio with calculated values
  const updatedPortfolio = updatePortfolioValues();

  // Calculate the total portfolio value
  const totalValue = updatedPortfolio.reduce((total, item) => total + parseFloat(item.value), 0);

  return (
    <div className="portfolio-overview container mt-4">
      <h2 className="text-center mb-4">Portfolio Overview</h2>
      <table className="table table-bordered table-hover">
        <thead className="thead-dark">
          <tr>
            <th>Asset</th>
            <th>Quantity</th>
            <th>Value (USD)</th>
          </tr>
        </thead>
        <tbody>
          {updatedPortfolio.map((item, index) => (
            <tr key={index}>
              <td>{item.asset}</td>
              <td>{item.quantity}</td>
              <td>${item.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="total-value mt-3 text-right">
        <h4><strong>Total Value: ${totalValue.toLocaleString()}</strong></h4>
      </div>
    </div>
  );
};

export default PortfolioOverview;
