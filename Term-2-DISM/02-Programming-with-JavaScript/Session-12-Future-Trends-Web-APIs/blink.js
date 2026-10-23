// blink.js — needs an Arduino with StandardFirmata uploaded (Arduino IDE → Examples → Firmata)
// Setup: npm init -y && npm install johnny-five
// Run:   node blink.js
const { Board, Led, Sensor } = require("johnny-five");

const board = new Board(); // auto-detects the Arduino on a USB port

board.on("ready", () => {
  console.log("Board ready");

  const led = new Led(13);
  led.blink(500); // toggle every 500 ms

  // Analog temperature sensor (e.g. LM35) on pin A0, read every second
  const sensor = new Sensor({ pin: "A0", freq: 1000 });
  sensor.on("data", function () {
    const celsius = (this.value * 5 * 100) / 1024; // LM35: 10 mV per °C
    console.log(`Temperature: ${celsius.toFixed(1)} °C`);
    if (celsius > 35) led.on(); // solid light as an alert
  });

  board.on("exit", () => led.off());
});
