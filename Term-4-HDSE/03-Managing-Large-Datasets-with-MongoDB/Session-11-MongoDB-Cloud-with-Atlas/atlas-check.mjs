// npm install mongodb   then: ATLAS_URI="mongodb+srv://..." node atlas-check.mjs
import { MongoClient, ServerApiVersion } from "mongodb";

const client = new MongoClient(process.env.ATLAS_URI, { serverApi: { version: ServerApiVersion.v1, strict: true } });
try {
  await client.connect();
  await client.db("admin").command({ ping: 1 });
  console.log("Connected to Atlas");
  const db = client.db("campus");
  console.log("Collections:", (await db.listCollections().toArray()).map((c) => c.name));
  const top = await db.collection("students").find({}, { projection: { _id: 0, name: 1, city: 1 } }).limit(3).toArray();
  console.table(top);
} finally {
  await client.close();
}
