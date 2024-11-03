import React, { useState } from 'react';
import { useAPI } from '../hooks/useAPI';

function TradeForm() {
    const [tradeData, setTradeData] = useState({ symbol: '', amount: '' });
    const api = useAPI();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTradeData({ ...tradeData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.post('/api/trades', tradeData);
            alert('Trade executed successfully!');
        } catch (error) {
            console.error('Trade execution failed:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="symbol"
                value={tradeData.symbol}
                onChange={handleChange}
                placeholder="Symbol (e.g., BTC)"
            />
            <input
                type="number"
                name="amount"
                value={tradeData.amount}
                onChange={handleChange}
                placeholder="Amount"
            />
            <button type="submit">Execute Trade</button>
        </form>
    );
}

export default TradeForm;
