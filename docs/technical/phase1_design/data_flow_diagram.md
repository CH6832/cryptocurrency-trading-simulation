# Data Flow Diagram (Real-Time Updates)

A data flow diagram helps visualize the flow of information throughout the application during real-time interactions.

```

+-----------+             +---------------------+             +--------------+
|   User    |             |  WebSocket Server    |             | Crypto Data  |
|  Interface|<----------->|  (Real-Time Updates) |<----------->|     API      |
|           |             |                     |             |              |
+-----------+             +---------------------+             +--------------+
                                   |
                                   |
                                   |
                     +-------------+-------------+
                     |                           |
                     |   Notification Service     |
                     |                           |
                     +-------------+-------------+
                                   |
                                   |
                       +-----------+-----------+
                       |     Application Layer   |
                       |      (FastAPI)        |
                       +-----------+-----------+
                                   |
                                   |
                               +---+---+
                               |MongoDB|
                               +-------+

```

### Diagram Explanation

1. **User Interface**:
   - This represents the front-end application where users interact with the crypto trading simulation. Users can perform actions such as logging in, viewing price charts, executing trades, and managing their portfolios.

2. **WebSocket Server (Real-Time Updates)**:
   - The WebSocket server facilitates real-time communication between the user interface and the server. This allows for instantaneous updates, ensuring that users see the latest market data without needing to refresh the page. The WebSocket server listens for incoming requests from the user interface and pushes real-time updates from the API.

3. **Crypto Data API**:
   - This is an external service that provides real-time market data for cryptocurrencies. The WebSocket server queries this API for price updates, trade data, and other relevant information about the selected cryptocurrencies. The data fetched is then relayed to the user interface via the WebSocket connection.

4. **Notification Service**:
   - This service sends notifications to users based on specific events, such as significant market changes, trade confirmations, or alerts set by users. It helps keep users informed about their trades and portfolio performance in real time.

5. **Application Layer (FastAPI)**:
   - The application layer handles the business logic of the application. FastAPI acts as the backend framework, processing user requests, interacting with the database, and communicating with the WebSocket server and the Crypto Data API. It also ensures that any user actions (like trades or portfolio queries) are correctly executed and responses sent back to the user interface.

6. **MongoDB**:
   - This is the database used to store user accounts, trade history, portfolio data, and other necessary information. It allows for efficient data retrieval and storage, ensuring that users can access their historical data and account information quickly. The application layer interacts with MongoDB to fetch or update data as needed.
