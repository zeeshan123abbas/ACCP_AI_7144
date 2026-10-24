// Unit tests for the package. Run with:  dart test
import 'package:grade_calculator/grade_calculator.dart';
import 'package:test/test.dart';

void main() {
  // group() keeps related tests together.
  group('gradeFor', () {
    test('gives A for 80 and above', () {
      expect(gradeFor(80), equals('A'));
      expect(gradeFor(100), equals('A'));
    });

    test('gives F below 50', () {
      expect(gradeFor(49), equals('F'));
    });

    test('throws for marks outside 0-100', () {
      expect(() => gradeFor(120), throwsArgumentError);
    });
  });

  group('averageOf', () {
    test('calculates the average', () {
      expect(averageOf([60, 70, 80]), equals(70));
    });

    test('returns 0 for an empty list', () {
      expect(averageOf([]), equals(0));
    });
  });

  test('isPass checks the 50 mark boundary', () {
    expect(isPass(50), isTrue);
    expect(isPass(49), isFalse);
  });
}
