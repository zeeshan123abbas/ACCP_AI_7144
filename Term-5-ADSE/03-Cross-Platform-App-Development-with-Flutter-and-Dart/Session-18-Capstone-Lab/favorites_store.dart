// Capstone - File 3: Save favourite product ids and the theme on the device
import 'package:shared_preferences/shared_preferences.dart';

class FavoritesStore {
  static const String favoritesKey = 'favoriteIds';
  static const String darkModeKey = 'darkMode';

  // shared_preferences stores a List<String>, so we convert ids to text.
  static Future<Set<int>> loadFavorites() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getStringList(favoritesKey) ?? [];
    return saved.map(int.parse).toSet();
  }

  static Future<void> saveFavorites(Set<int> ids) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList(favoritesKey, ids.map((id) => '$id').toList());
  }

  static Future<bool> loadDarkMode() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool(darkModeKey) ?? false;
  }

  static Future<void> saveDarkMode(bool isDark) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(darkModeKey, isDark);
  }
}
