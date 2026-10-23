// Run against a mongos router of a sharded cluster (e.g. created with Atlas or a lab setup)
sh.enableSharding("campus");
db.getSiblingDB("campus").events.createIndex({ userId: "hashed" });
sh.shardCollection("campus.events", { userId: "hashed" });
sh.status();
db.getSiblingDB("campus").events.getShardDistribution();
