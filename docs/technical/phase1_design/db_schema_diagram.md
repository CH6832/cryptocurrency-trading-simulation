# Database Schema Diagram

```

   +----------------+                +--------------------+
   |     Users      |                |     Transactions    |
   +----------------+                +--------------------+
   | _id            |                | _id                |
   | username       |                | user_id            |
   | email          |                | crypto_symbol       |
   | password_hash  |                | trade_type         |
   | created_at     |                | amount             |
   +----------------+                | price              |
                                      | timestamp          |
                                      +--------------------+
                                              |
                                              |
                                              |
                     +------------------------+
                     |
                     |
                     |
               +------------------+
               |     Portfolio    |
               +------------------+
               | _id              |
               | user_id          |
               | crypto_symbol     |
               | quantity         |
               | avg_buy_price    |
               +------------------+

```

## Explanation:

- Users: Collection storing user profiles including their unique ID, username, email, and hashed password.
- Transactions: Collection recording all trade activities for each user, including the type of trade (buy/sell), the cryptocurrency - traded, amount, price at the time of trade, and the timestamp.
- Portfolio: Collection holding the user's crypto holdings, including the amount of each cryptocurrency owned and the average buy price.

