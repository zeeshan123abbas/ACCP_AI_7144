// Session 13 - Example 2c: Product list (GET) + add button (POST)
// lib/ needs: main.dart, product.dart, api_service.dart
import 'package:flutter/material.dart';
import 'api_service.dart';
import 'product.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: ProductsPage()));
}

class ProductsPage extends StatefulWidget {
  const ProductsPage({super.key});

  @override
  State<ProductsPage> createState() => _ProductsPageState();
}

class _ProductsPageState extends State<ProductsPage> {
  late Future<List<Product>> productsFuture = ApiService.getProducts();

  // Send a POST request and show the server's answer in a SnackBar.
  Future<void> addDemoProduct() async {
    try {
      final created = await ApiService.addProduct('Aptech Notebook', 4.5);
      if (!mounted) return; // the screen may have closed while waiting
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Server created id ${created.id}: ${created.title}')),
      );
    } catch (error) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('$error')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Products (dummyjson)')),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: addDemoProduct,
        icon: const Icon(Icons.add),
        label: const Text('POST'),
      ),
      body: FutureBuilder<List<Product>>(
        future: productsFuture,
        builder: (context, snapshot) {
          // 1) still loading
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          // 2) something went wrong (no internet, server down...)
          if (snapshot.hasError) {
            return Center(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text('Error: ${snapshot.error}'),
                  TextButton(
                    onPressed: () => setState(() => productsFuture = ApiService.getProducts()),
                    child: const Text('Try again'),
                  ),
                ],
              ),
            );
          }
          // 3) success: draw the list
          final products = snapshot.data!;
          return ListView.builder(
            itemCount: products.length,
            itemBuilder: (context, index) {
              final product = products[index];
              return ListTile(
                leading: Image.network(product.thumbnail, width: 56),
                title: Text(product.title),
                subtitle: Text('\$${product.price.toStringAsFixed(2)}'),
              );
            },
          );
        },
      ),
    );
  }
}
