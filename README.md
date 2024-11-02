# Crypto Trading Simulation

## Project Overview

The Crypto Trading Simulation project aims to create an interactive platform where users can simulate trading various cryptocurrencies. This application is designed to help users practice trading strategies without financial risk while providing real-time market data and performance analytics.

### Key Features

- **User Registration & Authentication**: Users can create accounts and securely log in to the platform.
- **Real-Time Market Data**: Access real-time cryptocurrency market data through an integrated API.
- **Trade Execution**: Users can execute buy and sell orders, managing their virtual portfolios.
- **Portfolio Management**: View portfolio performance and analyze trading strategies.
- **Analytics Dashboard**: Visualize trading metrics and historical performance.

## Technologies Used

- **Backend**: FastAPI, MongoDB
- **Frontend**: React.js
- **Real-Time Data**: WebSocket API for live cryptocurrency data
- **Deployment**: To be determined (consider options like Docker, Heroku, etc.)

## Getting Started

To run the project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/crypto-trading-simulation.git
   ```

2. **Set Up the Backend**:

   - Navigate to the backend directory:
     ```bash
     cd crypto-trading-simulation/backend
     ```
   - Install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the FastAPI server:
     ```bash
     uvicorn app.main:app --reload
     ```

3. **Set Up the Frontend**:

   - Navigate to the frontend directory:
     ```bash
     cd ../frontend
     ```
   - Install the dependencies:
     ```bash
     npm install
     ```
   - Start the React application:
     ```bash
     npm start
     ```

## License

This project is licensed under the [MIT License](/LICENSE).
