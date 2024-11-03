# Repository Structure

.
├── /backend                                       # Backend codebase for the crypto trading simulation
│   ├── /app                                       # Main FastAPI application folder
│   │   ├── __init__.py                            # Initializes the FastAPI application package
│   │   ├── main.py                                # Entry point for the FastAPI application, creating the app instance and setting up routes
│   │   ├── api                                    # Directory for API endpoint definitions
│   │   │   ├── __init__.py                        # Initializes the API module
│   │   │   ├── users.py                           # User-related API endpoints (registration, login, profile management)
│   │   │   ├── trades.py                          # Trade-related API endpoints (trade execution, trade history)
│   │   │   └── portfolio.py                       # Portfolio-related API endpoints (view and analyze portfolio)
│   │   ├── models                                 # Data models for MongoDB
│   │   │   ├── __init__.py                        # Initializes the models module
│   │   │   ├── user.py                            # User model schema (e.g., user ID, name, email)
│   │   │   ├── trade.py                           # Trade model schema (e.g., trade ID, asset type, amount, price, timestamp)
│   │   │   └── portfolio.py                       # Portfolio model schema (e.g., assets held, total value)
│   │   ├── services                               # Core business logic for the application
│   │   │   ├── __init__.py                        # Initializes the services module
│   │   │   ├── auth.py                            # Authentication services (e.g., login, registration, JWT token generation)
│   │   │   ├── trading.py                         # Trading logic services (e.g., trade execution, order validation)
│   │   │   └── notifications.py                   # Notification service logic (e.g., alerts for trade status, price movements)
│   │   ├── database                               # Database connection setup for MongoDB
│   │   │   ├── __init__.py                        # Initializes the database module
│   │   │   └── mongodb.py                         # MongoDB connection configuration and helper functions
│   │   ├── notifications                          # Real-time notifications and WebSocket integration
│   │   │   ├── __init__.py                        # Initializes the notifications module
│   │   │   └── websocket_manager.py               # Manages WebSocket connections for live updates
│   │   ├── config.py                              # Configuration settings (e.g., environment variables)
│   │   ├── middlewares                            # Middleware definitions for additional request processing
│   │   │   ├── __init__.py                        # Initializes middleware module
│   │   │   └── logging.py                         # Custom middleware for request logging and error tracking
│   │   ├── tests                                  # Unit tests for backend components
│   │   │   ├── __init__.py                        # Initializes the tests module
│   │   │   ├── test_users.py                      # Tests for user-related endpoints (registration, login)
│   │   │   ├── test_trades.py                     # Tests for trade execution functionality
│   │   │   └── test_portfolio.py                  # Tests for portfolio-related endpoints (view and manage portfolio)
│   ├── requirements.txt                           # List of Python dependencies (if not using Poetry)
│   └── README.md                                  # Backend documentation overview
│
├── /frontend                                     # Frontend codebase
│   ├── /public                                   # Public assets
│   │   └── index.html                            # Main HTML file
│   ├── /src                                      # Source files for the React app
│   │   ├── index.js                              # Entry point for the React app
│   │   ├── App.js                                # Main application component
│   │   ├── /components                           # Reusable React components
│   │   │   ├── TradeForm.js                      # Component for trade execution
│   │   │   ├── PortfolioView.js                   # Component for viewing portfolio
│   │   │   └── Analytics.js                       # Component for analytics dashboard
│   │   ├── /context                              # Context API for state management
│   │   │   └── UserContext.js                     # Context for user authentication
│   │   ├── /hooks                                # Custom hooks for React
│   │   │   └── useAPI.js                         # Hook for API calls
│   │   ├── /styles                               # CSS or styling files
│   │   ├── /tests                                # Unit tests for frontend
│   │   │   ├── App.test.js                       # Tests for main App component
│   │   │   ├── TradeForm.test.js                  # Tests for TradeForm component
│   │   │   └── PortfolioView.test.js              # Tests for PortfolioView component
│   │   └── App.css                               # Main stylesheet
│   ├── package.json                              # JavaScript dependencies and scripts
│   └── README.md                                 # Frontend documentation
│
├── /docs                                         # Additional documentation
│   └── architecture.md                           # Architectural decisions and diagrams
│
├── /scripts                                      # Utility scripts for setup or deployment
│   ├── setup_db.py                               # Script for initializing the database
│   ├── deploy.bat                                 # Deployment script
│   └── deploy.sh                                 # Deployment script
│
├── .gitignore                                    # Git ignore file
├── pyproject.toml                                # Third-party libraries
└── README.md                                     # Main project documentation
