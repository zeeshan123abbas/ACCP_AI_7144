// Capstone - File 2: REST calls to https://dummyjson.com
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'product.dart';

class ApiService {
  static const String baseUrl = 'https://dummyjson.com/products';
  static const String fields = 'select=title,description,category,price,rating,thumbnail';

  // Empty text -> first 30 products, otherwise search results.
  static Future<List<Product>> fetchProducts(String searchText) async {
    final query = searchText.trim();
    final url = query.isEmpty
        ? Uri.parse('$baseUrl?limit=30&$fields')
        : Uri.parse('$baseUrl/search?q=${Uri.encodeQueryComponent(query)}&$fields');

    final response = await http.get(url).timeout(const Duration(seconds: 10));
    if (response.statusCode != 200) {
      throw Exception('Server error ${response.statusCode}');
    }
    final list = jsonDecode(response.body)['products'] as List;
    return list.map((item) => Product.fromJson(item)).toList();
  }
}
