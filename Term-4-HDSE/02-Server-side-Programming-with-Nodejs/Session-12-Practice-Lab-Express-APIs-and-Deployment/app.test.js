// Run: node --test   (needs local MongoDB running)
import { test, before, after } from "node:test";
import assert from "node:assert/strict";
import mongoose from "mongoose";
import { app } from "./app.js";

let server, base;

before(async () => {
  await mongoose.connect("mongodb://127.0.0.1:27017/events_test");
  await mongoose.connection.dropDatabase();
  server = app.listen(0);
  base = `http://localhost:${server.address().port}`;
});

after(async () => {
  server.close();
  await mongoose.disconnect();
});

const post = (url, body) =>
  fetch(base + url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });

test("rejects events in the past", async () => {
  const res = await post("/api/events", { title: "Old", date: "2020-01-01", capacity: 5 });
  assert.equal(res.status, 422);
});

test("prevents overbooking", async () => {
  const future = new Date(Date.now() + 86400000).toISOString();
  const ev = await (await post("/api/events", { title: "Workshop", date: future, capacity: 2 })).json();
  const results = await Promise.all([1, 2, 3].map(() => post(`/api/events/${ev._id}/book`, {})));
  const codes = results.map((r) => r.status).sort();
  assert.deepEqual(codes, [200, 200, 409]);
});
