// Session 14 - Step 1: Recipe model (matches https://dummyjson.com/recipes)
class Recipe {
  final int id;
  final String name;
  final String image;
  final String cuisine;
  final double rating;
  final List<String> ingredients;
  final List<String> instructions;

  Recipe({
    required this.id,
    required this.name,
    required this.image,
    required this.cuisine,
    required this.rating,
    required this.ingredients,
    required this.instructions,
  });

  factory Recipe.fromJson(Map<String, dynamic> json) {
    return Recipe(
      id: json['id'] as int,
      name: json['name'] as String,
      image: json['image'] as String,
      cuisine: json['cuisine'] as String,
      rating: (json['rating'] as num).toDouble(),
      // JSON arrays arrive as List<dynamic>; convert each item to String.
      ingredients: List<String>.from(json['ingredients']),
      instructions: List<String>.from(json['instructions']),
    );
  }
}
