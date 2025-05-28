# coingecko_to_mongo


### 🔁 Hourly Data Ingestion Script

To maintain up-to-date market data for the Streamlit dashboard, a Python script is scheduled to run **hourly** using a task scheduler (e.g., GitHub Actions or cron). This script performs the following key tasks:

#### ✅ Features:

* **Data Source**: Fetches real-time market data for **Bitcoin**, **Ethereum**, and **Solana** from the [CoinGecko API](https://www.coingecko.com/en/api).
* **Time-Stamped Ingestion**: Each fetched data point is annotated with the exact UTC timestamp of retrieval.
* **MongoDB Integration**: Inserts the data into the corresponding collections (`bitcoin`, `ethereum`, `solana`) within a **MongoDB Atlas** database.
* **Recent Fetch Tracker**: Also updates a separate `recent_fetched_at` collection to log the most recent fetch time for each cryptocurrency, enabling freshness tracking on the front end.

#### 📦 Tech Stack:

* **Language**: Python
* **Database**: MongoDB Atlas (Cloud NoSQL)
* **API**: CoinGecko
* **Libraries**: `requests`, `pymongo`, `datetime`, `os`, `bson`, `json`

#### 🔐 Secure Access:

MongoDB credentials (`MONGO_USER`, `MONGO_PASS`) are securely accessed via **environment variables**, ensuring sensitive information is not hard-coded.

