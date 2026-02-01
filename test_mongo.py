import pymongo
import os
from dotenv import load_dotenv

# Load variables from .env if you are using one
load_dotenv()

# Replace 'MONGODB_URL' with the exact key used in your project
mongo_url = os.getenv("MONGODB_URL") 

try:
    client = pymongo.MongoClient(mongo_url)
    # The 'ping' command is cheap and does not require specific privileges
    client.admin.command('ping')
    print("✅ Connection successful! Your credentials are correct.")
except Exception as e:
    print("❌ Connection failed.")
    print(f"Error details: {e}")