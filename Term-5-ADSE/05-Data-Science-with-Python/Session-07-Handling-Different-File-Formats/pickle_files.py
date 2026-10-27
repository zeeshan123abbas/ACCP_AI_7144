# pickle_files.py - save ANY Python object to a file and load it later
# Only open pickle files you created yourself or fully trust!
import pickle
import pandas as pd

# Some objects we want to keep between runs
settings = {"theme": "dark", "max_rows": 50}
scores = pd.DataFrame({"player": ["Babar", "Rizwan"], "runs": [101, 67]})

# Save (wb = write binary)
with open("objects.pkl", "wb") as file:
    pickle.dump({"settings": settings, "scores": scores}, file)
print("Saved objects.pkl")

# Load (rb = read binary)
with open("objects.pkl", "rb") as file:
    loaded = pickle.load(file)

print("Settings:", loaded["settings"])
print(loaded["scores"])

# pandas has its own shortcut for DataFrames
scores.to_pickle("scores.pkl")
print("\nFrom to_pickle/read_pickle:\n", pd.read_pickle("scores.pkl"))
