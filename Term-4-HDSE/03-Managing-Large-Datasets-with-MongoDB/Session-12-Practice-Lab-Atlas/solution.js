// mongosh "mongodb+srv://<cluster>/" --username <user> --file solution.js
const mflix = db.getSiblingDB("sample_mflix");
printjson(mflix.movies.find(
  { year: { $gt: 2010 }, "imdb.rating": { $type: "number" }, "imdb.votes": { $gt: 10000 } },
  { _id: 0, title: 1, year: 1, "imdb.rating": 1 }
).sort({ "imdb.rating": -1 }).limit(5).toArray());

const airbnb = db.getSiblingDB("sample_airbnb");
printjson(airbnb.listingsAndReviews.aggregate([
  { $group: { _id: "$address.country", listings: { $sum: 1 }, avgPrice: { $avg: { $toDouble: "$price" } } } },
  { $project: { listings: 1, avgPrice: { $round: ["$avgPrice", 0] } } },
  { $sort: { listings: -1 } }
]).toArray());
// Task 3 is done in the Atlas UI: Database Access -> Add New Database User -> Built-in role "read" on sample_mflix
