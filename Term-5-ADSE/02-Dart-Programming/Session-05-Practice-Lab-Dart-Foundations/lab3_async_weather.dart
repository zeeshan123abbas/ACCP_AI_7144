// lab3_async_weather.dart
// Practice: Future, async/await, Map and exception handling.

// Fake "server" data: city -> temperature in Celsius.
Map<String, int> fakeServer = {
  'Karachi': 33,
  'Lahore': 28,
  'Islamabad': 22,
};

// Simulates a slow network call that can fail.
Future<int> getTemperature(String city) async {
  await Future.delayed(Duration(milliseconds: 400));

  int? temperature = fakeServer[city]; // null if the city is unknown
  if (temperature == null) {
    throw Exception('No weather data for $city');
  }
  return temperature;
}

Future<void> main() async {
  List<String> cities = ['Karachi', 'Lahore', 'Gilgit', 'Islamabad'];

  for (String city in cities) {
    try {
      int temperature = await getTemperature(city);
      String feeling = temperature >= 30 ? 'hot' : 'pleasant';
      print('$city: $temperature°C ($feeling)');
    } catch (e) {
      print('$city: could not load -> $e');
    }
  }
  print('Weather check complete.');
}
