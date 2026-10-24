// lab1_electricity_bill.dart
// Practice: variables, if/else, functions and null safety.
// Slab rates below are made-up practice numbers, not real tariffs.

// Calculates the bill for a number of units using simple slabs.
double calculateBill(int units) {
  double bill;
  if (units <= 100) {
    bill = units * 10; // first slab: Rs. 10 per unit
  } else if (units <= 300) {
    bill = 100 * 10 + (units - 100) * 15; // next units cost Rs. 15
  } else {
    bill = 100 * 10 + 200 * 15 + (units - 300) * 20; // above 300: Rs. 20
  }
  return bill;
}

void main() {
  // The meter reading might be missing, so the type is int?.
  int? unitsUsed = readMeter('KE-5521');

  // If the reading is missing, use 0 instead of crashing.
  int units = unitsUsed ?? 0;

  double bill = calculateBill(units);
  print('Units used: $units');
  print('Total bill: Rs. ${bill.toStringAsFixed(0)}');

  // Try a few more readings with a loop.
  for (int testUnits in [80, 250, 420]) {
    print('$testUnits units -> Rs. ${calculateBill(testUnits)}');
  }
}

// Pretend meter reader. Returns null for unknown meters.
int? readMeter(String meterId) {
  if (meterId == 'KE-5521') return 275;
  return null;
}
