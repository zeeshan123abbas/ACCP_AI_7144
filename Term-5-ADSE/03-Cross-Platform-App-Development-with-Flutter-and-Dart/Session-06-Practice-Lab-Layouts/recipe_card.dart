// recipe_card.dart
// Lab Task 3: an image card with a title over the picture and info below.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: Scaffold(body: Center(child: RecipeCard()))));
}

class RecipeCard extends StatelessWidget {
  const RecipeCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      clipBehavior: Clip.antiAlias, // cut the image to the card's round corners
      margin: const EdgeInsets.all(16),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Stack: picture at the bottom, title on top of it.
          Stack(
            children: [
              Image.network(
                'https://picsum.photos/id/292/600/300',
                height: 180,
                width: double.infinity,
                fit: BoxFit.cover,
              ),
              Positioned(
                left: 12,
                bottom: 12,
                child: Container(
                  padding: const EdgeInsets.all(6),
                  color: Colors.black54,
                  child: const Text('Chicken Biryani', style: TextStyle(color: Colors.white, fontSize: 20)),
                ),
              ),
            ],
          ),
          // Info row: three icon + text pairs spread evenly.
          const Padding(
            padding: EdgeInsets.all(12),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Row(children: [Icon(Icons.timer, size: 18), SizedBox(width: 4), Text('45 min')]),
                Row(children: [Icon(Icons.people, size: 18), SizedBox(width: 4), Text('4 people')]),
                Row(children: [Icon(Icons.local_fire_department, size: 18), SizedBox(width: 4), Text('Spicy')]),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
