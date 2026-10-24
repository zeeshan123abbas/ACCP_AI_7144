// interfaces-and-classes.ts - describe the shape of data, then build objects
export {};

// An interface describes what properties an object must have
interface Student {
  id: number;
  name: string;
  email?: string;      // optional property
  readonly city: string; // cannot be changed after creation
}

const s1: Student = { id: 1, name: "Zara", city: "Karachi" };
console.log(s1.name, "from", s1.city);

// A class can "implement" an interface (promise to follow its shape)
interface Printable {
  print(): void;
}

class Course implements Printable {
  // "public" in the constructor creates and fills the property automatically
  constructor(public title: string, private fee: number) {}

  print(): void {
    console.log(`${this.title} - Rs ${this.fee}`);
  }
}

const c1 = new Course("Angular", 15000);
c1.print();
// c1.fee  <- error: fee is private
