// Session 13 - Example 2b: All network calls in one class
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'product.dart';

class ApiService {
  static const String baseUrl = 'https://dummyjson.com';

  // GET /products?limit=20  -> list of products
  static Future<List<Product>> getProducts() async {
    final url = Uri.parse('$baseUrl/products?limit=20&select=title,price,thumbnail');
    final response = await http.get(url);

    if (response.statusCode != 200) {
      throw Exception('Could not load products (${response.statusCode})');
    }

    final body = jsonDecode(response.body) as Map<String, dynamic>;
    final list = body['products'] as List;               // the array inside
    return list.map((item) => Product.fromJson(item)).toList();
  }

  // POST /products/add  -> the server echoes the new product with an id
  // (dummyjson only simulates saving; nothing is really stored)
  static Future<Product> addProduct(String title, double price) async {
    final url = Uri.parse('$baseUrl/products/add');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'title': title, 'price': price}), // Map -> JSON text
    );

    if (response.statusCode != 200 && response.statusCode != 201) {
      throw Exception('Could not add product (${response.statusCode})');
    }
    return Product.fromJson(jsonDecode(response.body));
  }
}
