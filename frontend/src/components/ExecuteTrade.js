import React from 'react';

const ExecuteTrade = () => {
  return (
    <div className="execute-trade">
      <input type="text" placeholder="Amount" />
      <input type="text" placeholder="Price" />
      <button>Buy</button>
      <button>Sell</button>
    </div>
  );
};

export default ExecuteTrade;
