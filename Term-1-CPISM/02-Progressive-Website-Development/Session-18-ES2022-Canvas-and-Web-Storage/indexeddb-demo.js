// indexeddb-demo.js - paste into the console on any page served over http(s)
const request = indexedDB.open("schoolDB", 1);

request.onupgradeneeded = () => {               // runs first time / on version change
  const db = request.result;
  const store = db.createObjectStore("students", { keyPath: "roll" });
  store.createIndex("byBatch", "batch");
};

request.onsuccess = () => {
  const db = request.result;
  const tx = db.transaction("students", "readwrite");
  const store = tx.objectStore("students");
  store.put({ roll: "S001", name: "Ayesha", batch: "2601A" });
  store.put({ roll: "S002", name: "Hamza", batch: "2601B" });

  tx.oncomplete = () => {
    const read = db.transaction("students").objectStore("students").get("S001");
    read.onsuccess = () => console.log("Found:", read.result);
  };
};
request.onerror = () => console.error("DB error", request.error);
