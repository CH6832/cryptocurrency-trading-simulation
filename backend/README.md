# Crypto Trading Simulation Backend

This is the backend service for the Crypto Trading Simulation application. It is built with FastAPI and provides RESTful APIs for user management, trading, portfolio management, and other core functionalities. The backend connects to a MongoDB database and serves data and operations to the frontend application.

## Features

- **User Authentication**: User registration and login with JWT-based authentication.
- **Trading Simulation**: Simulate crypto trades and manage a virtual portfolio.
- **Real-Time Market Data**: Retrieve and simulate real-time market data for virtual trading.
- **Portfolio Analytics**: Track performance and analytics for a user's portfolio.
- **Notifications**: Send notifications about portfolio updates and price changes.

## Technologies

- **Python 3.x**
- **FastAPI**: The main web framework for the API.
- **MongoDB**: Database to store user, trade, and portfolio data.
- **Pymongo**: MongoDB connector for Python.

## Setup and Installation

### Prerequisites

- **Python 3.x** installed on your machine.
- **MongoDB** database setup (local or cloud-based).

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/crypto-trading-simulation.git
    cd crypto-trading-simulation/backend
    ```

2. **Install dependencies**:

    Install all necessary Python packages using `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Configuration**:

    Create a `.env` file in `backend/app` and add your MongoDB connection string and any other required configurations.

    ```env
    MONGO_URI="your_mongo_connection_string"
    SECRET_KEY="your_jwt_secret_key"
    ```

4. **Run the Application**:

    Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
    ```

5. **API Documentation**:

    Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Testing

Run tests with pytest:

```bash
pytest app/tests
```

This will execute the tests in the `tests` directory, checking for any issues in the backend functionalities.

## Deployment

To deploy this application, ensure MongoDB is properly configured in a production environment, and use a production-ready server, such as Gunicorn or Uvicorn with ASGI.

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```
