// data-types.ts - the basic types of TypeScript
export {}; // makes this file a module, so its variables stay private to it

// 1. Primitive types
let courseName: string = "ACCP AI";
let totalSessions: number = 12;
let isActive: boolean = true;

// 2. Arrays: a list of values of the same type
let marks: number[] = [78, 85, 91];

// 3. Tuple: fixed length, each position has its own type
let student: [string, number] = ["Bilal", 19];

// 4. Union type: the value can be one type OR another
let rollNo: string | number = 101;
rollNo = "HDSE-101"; // also allowed

// 5. Enum: a set of named constants
enum Grade { A = "A", B = "B", C = "C" }
let myGrade: Grade = Grade.A;

// 6. any (avoid it) and unknown (safer)
let anything: any = 5;      // TypeScript stops checking this variable
let input: unknown = "hi";  // you must check the type before using it
if (typeof input === "string") {
  console.log(input.toUpperCase());
}

console.log(courseName, totalSessions, isActive);
console.log("Marks:", marks, "Student:", student);
console.log("Roll No:", rollNo, "Grade:", myGrade, "Any:", anything);
