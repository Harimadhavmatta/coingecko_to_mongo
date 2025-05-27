import requests
import os
from pymongo import MongoClient
from datetime import datetime, timezone

try :
    mongo_user = os.getenv('MONGO_USER') 
    mongo_pass = os.getenv('MONGO_PASS') 
except KeyError: 
    mongo_user = 'mattaharimadhav2004' 
    mongo_pass = 'chQNUDwVPr0Ov5jx'

uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.yzrkrnz.mongodb.net/"
client = MongoClient(uri)

db = client["crypto_coins"]
collections = {
    'bitcoin': db["bitcoin"],
    'ethereum': db["ethereum"],
    'solana': db["solana"],
}

# API endpoint
coin_specific_url = 'https://api.coingecko.com/api/v3/coins/markets'

# Fetch and insert data for each coin
coins = ['bitcoin', 'ethereum', 'solana']
for coin in coins:
    params = {
        "ids": coin,
        "vs_currency": "inr"
    }
    response = requests.get(coin_specific_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            coin_data = data[0]
            coin_data['fetched_at'] = datetime.now(timezone.utc)
            collections[coin].insert_one(coin_data)
            print(f"{coin.capitalize()} data inserted successfully.")
        else:
            print(f"No data returned for {coin}.")
    else:
        print(f"Failed to fetch data for {coin}, status code: {response.status_code}")
