// quantity_selector.dart
// Lab Task 2: + and - buttons change a quantity and the total price.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: QuantityPage()));
}

class QuantityPage extends StatefulWidget {
  const QuantityPage({super.key});

  @override
  State<QuantityPage> createState() => _QuantityPageState();
}

class _QuantityPageState extends State<QuantityPage> {
  int quantity = 1;              // changing data
  final int pricePerItem = 350;  // fixed price in rupees

  void increase() {
    setState(() {
      quantity++;
    });
  }

  void decrease() {
    // Do not allow less than 1 item.
    if (quantity > 1) {
      setState(() {
        quantity--;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    int total = quantity * pricePerItem; // calculated on every build

    return Scaffold(
      appBar: AppBar(title: const Text('Zinger Burger')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                IconButton(onPressed: decrease, icon: const Icon(Icons.remove_circle)),
                Text('$quantity', style: const TextStyle(fontSize: 32)),
                IconButton(onPressed: increase, icon: const Icon(Icons.add_circle)),
              ],
            ),
            Text('Total: Rs. $total', style: const TextStyle(fontSize: 22)),
          ],
        ),
      ),
    );
  }
}
