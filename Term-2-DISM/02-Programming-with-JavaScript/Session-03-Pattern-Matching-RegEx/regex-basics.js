// Run: node regex-basics.js
const patterns = {
  email: /^[\w.+-]+@[\w-]+\.[\w.-]+$/,
  mobile: /^03\d{2}-?\d{7}$/,
  cnic: /^\d{5}-\d{7}-\d$/,
  strongPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$/,
  postalCode: /^\d{5}$/
};

const samples = {
  email: ["ali@example.com", "ali@com", "sara.k+news@mail.co.uk"],
  mobile: ["0300-1234567", "03001234567", "0213-1234567"],
  cnic: ["42101-1234567-1", "4210112345671"],
  strongPassword: ["Passw0rd!", "password", "Abc12345"],
  postalCode: ["74600", "7460"]
};

for (const [name, regex] of Object.entries(patterns)) {
  for (const value of samples[name]) {
    console.log(`${name.padEnd(15)} ${value.padEnd(25)} ${regex.test(value) ? "✔ valid" : "✘ invalid"}`);
  }
}
