// Capstone - File 4: Product detail screen
import 'package:flutter/material.dart';
import 'product.dart';

class DetailScreen extends StatelessWidget {
  final Product product;
  final bool isFavorite;
  final VoidCallback onToggleFavorite;

  const DetailScreen({
    super.key,
    required this.product,
    required this.isFavorite,
    required this.onToggleFavorite,
  });

  @override
  Widget build(BuildContext context) {
    final textStyles = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(title: Text(product.title)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Image.network(product.thumbnail, height: 240),
          const SizedBox(height: 16),
          Text(product.title, style: textStyles.headlineSmall),
          Text('${product.category} · ⭐ ${product.rating}', style: textStyles.bodyMedium),
          const SizedBox(height: 8),
          Text('\$${product.price.toStringAsFixed(2)}', style: textStyles.titleLarge),
          const SizedBox(height: 16),
          Text(product.description, style: textStyles.bodyLarge),
          const SizedBox(height: 24),
          FilledButton.icon(
            onPressed: () {
              onToggleFavorite();      // update the list screen's state
              Navigator.pop(context);  // go back to see the change
            },
            icon: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
            label: Text(isFavorite ? 'Remove from favourites' : 'Add to favourites'),
          ),
        ],
      ),
    );
  }
}
