// provider_cart.dart
// Provider: a Cart shared by the AppBar badge and the product list.

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// STEP 1: the state class. It extends ChangeNotifier.
class Cart extends ChangeNotifier {
  final List<String> items = [];

  int get count => items.length;

  void add(String item) {
    items.add(item);
    notifyListeners(); // tell all watching widgets to rebuild
  }

  void clear() {
    items.clear();
    notifyListeners();
  }
}

void main() {
  runApp(
    // STEP 2: put the Cart above the whole app.
    ChangeNotifierProvider(
      create: (context) => Cart(),
      child: const MaterialApp(home: ShopPage()),
    ),
  );
}

class ShopPage extends StatelessWidget {
  const ShopPage({super.key});

  @override
  Widget build(BuildContext context) {
    final List<String> products = ['Notebook', 'Pen', 'USB Drive', 'Headphones'];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Mini Shop'),
        actions: const [CartBadge()], // the badge reads the Cart on its own
      ),
      body: ListView.builder(
        itemCount: products.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(products[index]),
            trailing: IconButton(
              icon: const Icon(Icons.add_shopping_cart),
              // STEP 3a: read = get the Cart without listening (inside callbacks).
              onPressed: () => context.read<Cart>().add(products[index]),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => context.read<Cart>().clear(),
        child: const Icon(Icons.delete),
      ),
    );
  }
}

class CartBadge extends StatelessWidget {
  const CartBadge({super.key});

  @override
  Widget build(BuildContext context) {
    // STEP 3b: watch = get the Cart AND rebuild when it changes.
    final int count = context.watch<Cart>().count;

    return Padding(
      padding: const EdgeInsets.only(right: 16),
      // Badge is a Material 3 widget that shows a small label on an icon.
      child: Badge(
        label: Text('$count'),
        child: const Icon(Icons.shopping_cart),
      ),
    );
  }
}
