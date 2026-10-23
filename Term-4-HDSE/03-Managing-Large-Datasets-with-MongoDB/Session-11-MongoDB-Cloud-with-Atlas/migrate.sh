# Set your Atlas URI once (replace user, password and cluster)
ATLAS="mongodb+srv://student:<password>@cluster0.xxxxx.mongodb.net"

# 1) Local -> Atlas, exact copy of the campus database
mongodump --db campus --out ./dump
mongorestore --uri "$ATLAS" --nsInclude "campus.*" ./dump

# 2) JSON route for one collection
mongoexport --db campus --collection students --out students.json --jsonArray
mongoimport --uri "$ATLAS/campus" --collection students_json --file students.json --jsonArray

# 3) Atlas -> local backup
mongodump --uri "$ATLAS/campus" --out ./atlas-backup
mongorestore --nsFrom "campus.*" --nsTo "campus_from_atlas.*" ./atlas-backup

# 4) Connect with the shell
mongosh "$ATLAS/campus" --username student
