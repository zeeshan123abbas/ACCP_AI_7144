// src/math.js
export const add = (a, b) => a + b;
export const average = nums => nums.reduce(add, 0) / nums.length;
export const unusedHeavyHelper = () => "I am never imported, so production builds drop me";
