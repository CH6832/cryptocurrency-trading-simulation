# Cryptocurrency Trading Simulation - UI/UX Documentation

## Table of Contents
1. **Introduction**
2. **Application Layout**
3. **Navigation Structure**
4. **Screens and Components**
    - Header
    - Navigation
    - User Management
    - All Prices
    - Price Chart
    - Execute Trade
    - Portfolio Overview
    - Market
    - Footer
5. **Interactions and Flow**
6. **Design Principles**
7. **ASCII Layout Drawings**

---

## 1. Introduction

The Cryptocurrency Trading Simulation project provides a platform for users to simulate trading cryptocurrencies with live market data. The UI/UX design focuses on simplicity, usability, and responsiveness. This document outlines the structure and interactions of the application.

---

## 2. Application Layout

The application has a dashboard layout divided into several components:
- **Header**: Displays the application title and branding.
- **Navigation**: Links to different pages (e.g., Home, Market).
- **Main Content**: Displays the core components (e.g., prices, charts, trades).
- **Footer**: Shows supplementary information like copyright.

---

## 3. Navigation Structure

### Navigation Links:
- **Home**: Redirects to the main dashboard.
- **Market**: Displays all available cryptocurrencies and their details.

### ASCII Representation:

```
+-------------------------------+
|       Cryptocurrency          |
|          Dashboard            |
+-------------------------------+
| Home | Market | ...           |
+-------------------------------+
|                               |
|        Main Content           |
|                               |
+-------------------------------+
|         Footer Info           |
+-------------------------------+
```

---

## 4. Screens and Components

### 4.1 Header
- **Purpose**: Display the application's name and a search bar for quick access.
- **Features**:
  - Application logo
  - Search input field

**ASCII Layout**:
```
+--------------------------------------------------+
| Cryptocurrency Trading Simulation   [ Search ]  |
+--------------------------------------------------+
```

---

### 4.2 Navigation
- **Purpose**: Navigate between key sections of the app.
- **Links**:
  - Home
  - Market
  - Portfolio

**ASCII Layout**:
```
+-------------------+
| Home | Market ... |
+-------------------+
```

---

### 4.3 User Management
- **Purpose**: Manage user information like username and account balance.

**ASCII Layout**:
```
+--------------------------+
| User: JohnDoe            |
| Balance: $10,000         |
+--------------------------+
```

---

### 4.4 All Prices
- **Purpose**: Display real-time cryptocurrency prices.

**ASCII Layout**:
```
+----------------------------------+
| Crypto         Price (USD)       |
| Bitcoin (BTC)  $99888.00         |
| Ethereum (ETH) $4010.86          |
| Litecoin (LTC) $137.09           |
+----------------------------------+
```

---

### 4.5 Price Chart
- **Purpose**: Visualize historical price trends.
- **Interaction**: Hovering over points shows detailed data.

**ASCII Layout**:
```
+--------------------------------+
|          Price Chart           |
|   o        o    o             |
|      o     o      o           |
+--------------------------------+
```

---

### 4.6 Execute Trade
- **Purpose**: Allow users to buy or sell cryptocurrencies.
- **Inputs**:
  - Quantity
  - Price per unit
- **Buttons**:
  - Buy
  - Sell

**ASCII Layout**:
```
+-----------------------------+
| Amount [ 1 ]  Price [99988] |
| [ Buy ]       [ Sell ]      |
+-----------------------------+
```

---

### 4.7 Portfolio Overview
- **Purpose**: Summarize the user's cryptocurrency holdings.
- **Table**:
  - Asset
  - Quantity
  - Value (USD)

**ASCII Layout**:
```
+--------------------------------------+
| Asset           Qty   Value (USD)    |
| Bitcoin (BTC)   0.5   $49,944.00     |
| Ethereum (ETH)  2.0   $8,021.72      |
| Litecoin (LTC)  5.0   $685.45        |
+--------------------------------------+
| Total Value: $58,651.17              |
+--------------------------------------+
```

---

### 4.8 Market
- **Purpose**: Display all cryptocurrencies available in the market.

**ASCII Layout**:
```
+------------------------------------+
| Market                            |
+------------------------------------+
| Crypto         Price (USD)         |
| Bitcoin (BTC)  $99888.00           |
| Ethereum (ETH) $4010.86            |
| Litecoin (LTC) $137.09             |
| ...                                |
+------------------------------------+
```

---

### 4.9 Footer
- **Purpose**: Display supplementary information.
- **Content**:
  - © 2024 Cryptocurrency Trading Simulation

**ASCII Layout**:
```
+-------------------------------------+
| © 2024 Cryptocurrency Trading Sim. |
+-------------------------------------+
```

---

## 5. Interactions and Flow
- **Navigation**:
  - Clicking "Market" takes the user to the market page.
  - Clicking "Home" returns to the dashboard.
- **Trades**:
  - Input the quantity and price for a trade, then press "Buy" or "Sell".
- **Portfolio**:
  - Updates dynamically based on trades and price changes.

---

## 6. Design Principles
1. **Clarity**: Use simple, self-explanatory labels.
2. **Consistency**: Uniform color schemes and button styles.
3. **Responsiveness**: Adapt to different screen sizes.
4. **Accessibility**: Ensure keyboard navigation and screen reader support.

---

## 7. ASCII Layout Drawings

### Main Dashboard
```
+----------------------------------------------------------+
| Cryptocurrency Trading Simulation   [ Search ]           |
+----------------------------------------------------------+
| Home | Market | Portfolio ...                            |
+----------------------------------------------------------+
| User: JohnDoe  | Balance: $10,000                        |
+----------------------------------------------------------+
| Crypto         Price (USD)                               |
| Bitcoin (BTC)  $99888.00                                 |
| Ethereum (ETH) $4010.86                                  |
| Litecoin (LTC) $137.09                                   |
+----------------------------------------------------------+
|          Price Chart                                      |
|    o       o     o      o                                |
+----------------------------------------------------------+
| Amount [ 1 ]  Price [99888]                              |
| [ Buy ]       [ Sell ]                                   |
+----------------------------------------------------------+
| Portfolio Overview                                        |
| Asset           Qty   Value (USD)                        |
| Bitcoin (BTC)   0.5   $49,944.00                         |
| Ethereum (ETH)  2.0   $8,021.72                          |
| Litecoin (LTC)  5.0   $685.45                            |
+----------------------------------------------------------+
| © 2024 Cryptocurrency Trading Simulation                 |
+----------------------------------------------------------+
```

---
