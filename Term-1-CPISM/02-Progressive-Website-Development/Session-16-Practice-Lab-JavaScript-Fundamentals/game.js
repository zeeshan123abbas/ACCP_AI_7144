const MAX_TRIES = 7;
let secret, triesLeft, guesses;

const form = document.querySelector("#guessForm");
const input = document.querySelector("#guess");
const msg = document.querySelector("#msg");
const left = document.querySelector("#left");
const historyEl = document.querySelector("#history");
const restart = document.querySelector("#restart");

function newGame() {
  secret = Math.floor(Math.random() * 100) + 1;   // 1..100
  triesLeft = MAX_TRIES;
  guesses = [];
  msg.textContent = "";
  left.textContent = triesLeft;
  historyEl.textContent = "-";
  input.disabled = false;
  restart.hidden = true;
  input.focus();
}

function endGame(text) {
  msg.textContent = text;
  input.disabled = true;
  restart.hidden = false;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();                 // stop page reload
  const guess = Number(input.value);
  if (!Number.isInteger(guess) || guess < 1 || guess > 100) {
    msg.textContent = "Enter a whole number from 1 to 100.";
    return;
  }
  if (guesses.includes(guess)) {
    msg.textContent = `You already tried ${guess}.`;
    return;
  }

  guesses.push(guess);
  triesLeft--;
  left.textContent = triesLeft;
  historyEl.textContent = [...guesses].sort((a, b) => a - b).join(", ");

  if (guess === secret) {
    endGame(`🎉 Correct! ${secret} in ${guesses.length} tries.`);
  } else if (triesLeft === 0) {
    endGame(`Game over. The number was ${secret}.`);
  } else {
    const diff = Math.abs(secret - guess);
    const hint = diff <= 5 ? "very close" : diff <= 15 ? "close" : "far";
    msg.textContent = `${guess > secret ? "Too high" : "Too low"} (${hint}).`;
  }
  input.value = "";
  input.focus();
});

restart.addEventListener("click", newGame);
newGame();

// ---- Extra practice: array methods in the console ----
const marks = [72, 45, 90, 66, 38, 81];
console.table(marks.map((m, i) => ({ student: i + 1, marks: m, pass: m >= 50 })));
console.log("Total:", marks.reduce((sum, m) => sum + m, 0));
console.log("First above 85:", marks.find(m => m > 85));
console.log("All above 30?", marks.every(m => m > 30));
