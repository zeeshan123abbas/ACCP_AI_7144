// user.js
export class User {
  #password; // private field

  constructor(name, email, password) {
    this.name = name;
    this.email = email;
    this.#password = password;
    this.loggedIn = false;
  }

  login(password) {
    this.loggedIn = password === this.#password;
    return this.loggedIn ? `${this.name} logged in` : "Wrong password";
  }

  logout() {
    this.loggedIn = false;
    return `${this.name} logged out`;
  }

  get role() {
    return "user";
  }

  toString() {
    return `${this.name} <${this.email}> (${this.role})`;
  }
}

export class Student extends User {
  constructor(name, email, password, batch) {
    super(name, email, password); // must come before using `this`
    this.batch = batch;
    this.submissions = [];
  }

  get role() {
    return "student";
  }

  submit(title) {
    if (!this.loggedIn) return "Please log in first";
    this.submissions.push({ title, at: new Date().toISOString() });
    return `Submitted: ${title}`;
  }
}
