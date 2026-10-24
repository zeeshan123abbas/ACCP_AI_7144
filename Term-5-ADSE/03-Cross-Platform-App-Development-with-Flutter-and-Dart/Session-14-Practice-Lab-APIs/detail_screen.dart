// Session 14 - Step 3: Detail screen (receives a Recipe, no new request needed)
import 'package:flutter/material.dart';
import 'recipe.dart';

class DetailScreen extends StatelessWidget {
  final Recipe recipe;
  const DetailScreen({super.key, required this.recipe});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(recipe.name)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // Hero animates the picture from the list to this page.
          Hero(
            tag: 'recipe-${recipe.id}',
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.network(recipe.image, height: 220, fit: BoxFit.cover),
            ),
          ),
          const SizedBox(height: 12),
          Text('${recipe.cuisine} · ⭐ ${recipe.rating}',
              style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 16),
          Text('Ingredients', style: Theme.of(context).textTheme.titleLarge),
          // Spread operator (...) adds one Text per ingredient.
          ...recipe.ingredients.map((item) => Text('• $item')),
          const SizedBox(height: 16),
          Text('Steps', style: Theme.of(context).textTheme.titleLarge),
          // asMap().entries gives us the index for numbering.
          ...recipe.instructions.asMap().entries.map(
                (entry) => Padding(
                  padding: const EdgeInsets.symmetric(vertical: 4),
                  child: Text('${entry.key + 1}. ${entry.value}'),
                ),
              ),
        ],
      ),
    );
  }
}
