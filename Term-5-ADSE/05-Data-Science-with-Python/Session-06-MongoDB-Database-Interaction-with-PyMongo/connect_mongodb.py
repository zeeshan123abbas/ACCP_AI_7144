# connect_mongodb.py - connect Python to a MongoDB server with PyMongo
# Install the driver first:  pip install pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# The connection string: a local server on the default port 27017
# For MongoDB Atlas (cloud) paste your own string, e.g.
# "mongodb+srv://<user>:<password>@cluster0.xxxxx.mongodb.net/"
CONNECTION_STRING = "mongodb://localhost:27017/"

# Wait at most 3 seconds for the server to answer
client = MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=3000)

try:
    client.admin.command("ping")          # a tiny "are you there?" request
    print("Connected to MongoDB!")
    print("Databases:", client.list_database_names())
except ServerSelectionTimeoutError:
    print("Could not reach MongoDB. Is the server running on port 27017?")
    print("Tip: start MongoDB Community Server or use a free Atlas cluster.")
finally:
    client.close()                        # always close the connection
