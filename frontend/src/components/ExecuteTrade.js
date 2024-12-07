import React, { useState, useEffect } from 'react';

const ExecuteTrade = ({ selectedCrypto, price }) => {
  const [amount, setAmount] = useState(1); // Prefill with 1 unit
  const [tradePrice, setTradePrice] = useState(price);

  // Update trade price whenever the selected cryptocurrency changes
  useEffect(() => {
    setTradePrice(price);
  }, [price]);

  const handleAmountChange = (event) => {
    setAmount(event.target.value);
  };

  const handlePriceChange = (event) => {
    setTradePrice(event.target.value);
  };

  return (
    <div className="execute-trade" style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
      <input
        type="number"
        placeholder="Amount"
        value={amount}
        onChange={handleAmountChange}
        style={{ padding: '8px', width: '150px' }}
      />
      <input
        type="text"
        placeholder="Price"
        value={tradePrice}  // Prefilled with the selected price
        onChange={handlePriceChange}
        style={{ padding: '8px', width: '150px' }}
      />
      <button style={{ padding: '8px 16px' }}>Buy</button>
      <button style={{ padding: '8px 16px' }}>Sell</button>
    </div>
  );
};

export default ExecuteTrade;
