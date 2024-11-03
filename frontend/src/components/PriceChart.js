import React from 'react';

const PriceChart = () => {
  return (
    <div className="price-chart">
      <h2>Select Cryptocurrency:</h2>
      <select>
        <option>Bitcoin (BTC)</option>
        <option>Ethereum (ETH)</option>
        <option>Litecoin (LTC)</option>
      </select>
      <div className="chart-container">
        <h3>Bitcoin (BTC)</h3>
        {/* Replace with actual chart rendering logic */}
        <div className="chart">Chart goes here</div>
      </div>
    </div>
  );
};

export default PriceChart;
