# Cell 1 - install
# !pip install -q "pymongo[srv]" pandas matplotlib

# Cell 2 - connect using Colab Secrets (add MONGODB_URI via the key icon)
from google.colab import userdata
from pymongo import MongoClient
client = MongoClient(userdata.get("MONGODB_URI"))
db = client["sample_mflix"]

# Cell 3 - analyse
import pandas as pd
rows = db.movies.aggregate([
    {"$match": {"year": {"$gte": 2000}, "imdb.rating": {"$type": "number"}}},
    {"$group": {"_id": "$year", "avgRating": {"$avg": "$imdb.rating"}, "movies": {"$sum": 1}}},
    {"$sort": {"_id": 1}},
])
df = pd.DataFrame(list(rows)).rename(columns={"_id": "year"})
df.plot(x="year", y="avgRating", title="Average IMDb rating by year")
