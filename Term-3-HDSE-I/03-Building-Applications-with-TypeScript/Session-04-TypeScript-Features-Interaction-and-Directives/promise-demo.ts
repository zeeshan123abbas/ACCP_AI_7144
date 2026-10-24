// promise-demo.ts - a Promise is a value that arrives later
export {};

// This function pretends to load data from a server (takes 1 second)
function loadStudentName(id: number): Promise<string> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve("Student #" + id); // success
      } else {
        reject("Invalid id");       // failure
      }
    }, 1000);
  });
}

// async/await lets us write waiting code that reads top-to-bottom
async function main(): Promise<void> {
  try {
    const name = await loadStudentName(5);
    console.log("Loaded:", name);
    await loadStudentName(0); // this one fails
  } catch (error) {
    console.log("Error:", error);
  }
}

main();
