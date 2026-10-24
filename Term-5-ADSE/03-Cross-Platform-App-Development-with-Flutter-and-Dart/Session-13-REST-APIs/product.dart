// Session 13 - Example 2a: Model for one product from dummyjson.com
class Product {
  final int id;
  final String title;
  final double price;
  final String thumbnail;

  Product({
    required this.id,
    required this.title,
    required this.price,
    required this.thumbnail,
  });

  // JSON Map -> Product object
  factory Product.fromJson(Map<String, dynamic> json) {
    return Product(
      id: json['id'] as int,
      title: json['title'] as String,
      price: (json['price'] as num).toDouble(), // price can be int or double
      thumbnail: json['thumbnail'] as String? ?? '', // missing -> empty text
    );
  }
}
