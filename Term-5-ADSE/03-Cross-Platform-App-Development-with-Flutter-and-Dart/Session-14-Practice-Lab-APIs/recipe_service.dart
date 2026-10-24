// Session 14 - Step 2: Network calls for recipes
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'recipe.dart';

class RecipeService {
  static const String baseUrl = 'https://dummyjson.com/recipes';

  // Empty search text -> all recipes; otherwise -> /recipes/search?q=text
  static Future<List<Recipe>> search(String text) async {
    final Uri url;
    if (text.trim().isEmpty) {
      url = Uri.parse('$baseUrl?limit=30');
    } else {
      // Uri.encodeQueryComponent makes spaces and symbols safe in a URL.
      url = Uri.parse('$baseUrl/search?q=${Uri.encodeQueryComponent(text.trim())}');
    }

    final response = await http.get(url).timeout(const Duration(seconds: 10));
    if (response.statusCode != 200) {
      throw Exception('Server returned ${response.statusCode}');
    }

    final body = jsonDecode(response.body) as Map<String, dynamic>;
    final list = body['recipes'] as List;
    return list.map((item) => Recipe.fromJson(item)).toList();
  }
}
