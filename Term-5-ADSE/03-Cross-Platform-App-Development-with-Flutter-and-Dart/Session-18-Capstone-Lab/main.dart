// Capstone - File 5: ShopEasy app
// Uses: REST (Session 13-14), responsive grid + themes (Session 10), saved data (Session 11-12)
// lib/ needs: main.dart, product.dart, api_service.dart, favorites_store.dart, detail_screen.dart
import 'package:flutter/material.dart';
import 'api_service.dart';
import 'detail_screen.dart';
import 'favorites_store.dart';
import 'product.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final startDark = await FavoritesStore.loadDarkMode();
  runApp(ShopEasyApp(startDark: startDark));
}

class ShopEasyApp extends StatefulWidget {
  final bool startDark;
  const ShopEasyApp({super.key, required this.startDark});

  @override
  State<ShopEasyApp> createState() => _ShopEasyAppState();
}

class _ShopEasyAppState extends State<ShopEasyApp> {
  late bool isDark = widget.startDark;

  void toggleTheme() {
    setState(() => isDark = !isDark);
    FavoritesStore.saveDarkMode(isDark);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ShopEasy',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorSchemeSeed: Colors.blue),
      darkTheme: ThemeData(colorSchemeSeed: Colors.blue, brightness: Brightness.dark),
      themeMode: isDark ? ThemeMode.dark : ThemeMode.light,
      home: HomeScreen(isDark: isDark, onToggleTheme: toggleTheme),
    );
  }
}

class HomeScreen extends StatefulWidget {
  final bool isDark;
  final VoidCallback onToggleTheme;
  const HomeScreen({super.key, required this.isDark, required this.onToggleTheme});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final searchController = TextEditingController();
  List<Product> products = [];
  Set<int> favoriteIds = {};
  bool isLoading = true;
  bool showOnlyFavorites = false;
  String? errorMessage;

  @override
  void initState() {
    super.initState();
    FavoritesStore.loadFavorites().then((ids) {
      if (mounted) setState(() => favoriteIds = ids);
    });
    loadProducts();
  }

  Future<void> loadProducts() async {
    setState(() {
      isLoading = true;
      errorMessage = null;
    });
    try {
      final result = await ApiService.fetchProducts(searchController.text);
      if (!mounted) return;
      setState(() {
        products = result;
        isLoading = false;
      });
    } catch (error) {
      if (!mounted) return;
      setState(() {
        errorMessage = 'Could not load products. Check your internet.';
        isLoading = false;
      });
    }
  }

  void toggleFavorite(int productId) {
    setState(() {
      if (favoriteIds.contains(productId)) {
        favoriteIds.remove(productId);
      } else {
        favoriteIds.add(productId);
      }
    });
    FavoritesStore.saveFavorites(favoriteIds);
  }

  // Responsive: 2 columns on phones, more on wider screens.
  int columnsFor(double width) {
    if (width < 600) return 2;
    if (width < 1000) return 3;
    return 5;
  }

  Widget buildProductCard(Product product) {
    final isFavorite = favoriteIds.contains(product.id);
    return Card(
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => DetailScreen(
              product: product,
              isFavorite: isFavorite,
              onToggleFavorite: () => toggleFavorite(product.id),
            ),
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(child: Center(child: Image.network(product.thumbnail))),
            Padding(
              padding: const EdgeInsets.all(8),
              child: Text(product.title, maxLines: 1, overflow: TextOverflow.ellipsis),
            ),
            Row(
              children: [
                const SizedBox(width: 8),
                Text('\$${product.price.toStringAsFixed(2)}'),
                const Spacer(),
                IconButton(
                  icon: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
                  onPressed: () => toggleFavorite(product.id),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget buildBody() {
    if (isLoading) return const Center(child: CircularProgressIndicator());
    if (errorMessage != null) {
      return Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(errorMessage!),
            TextButton(onPressed: loadProducts, child: const Text('Try again')),
          ],
        ),
      );
    }

    // Apply the favourites filter.
    final visible = showOnlyFavorites
        ? products.where((p) => favoriteIds.contains(p.id)).toList()
        : products;
    if (visible.isEmpty) return const Center(child: Text('Nothing to show.'));

    return LayoutBuilder(
      builder: (context, constraints) => GridView.builder(
        padding: const EdgeInsets.all(8),
        itemCount: visible.length,
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: columnsFor(constraints.maxWidth),
          childAspectRatio: 0.75,
        ),
        itemBuilder: (context, index) => buildProductCard(visible[index]),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('ShopEasy'),
        actions: [
          IconButton(
            tooltip: 'Favourites only',
            icon: Icon(showOnlyFavorites ? Icons.favorite : Icons.favorite_outline),
            onPressed: () => setState(() => showOnlyFavorites = !showOnlyFavorites),
          ),
          IconButton(
            tooltip: 'Theme',
            icon: Icon(widget.isDark ? Icons.light_mode : Icons.dark_mode),
            onPressed: widget.onToggleTheme,
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8),
            child: TextField(
              controller: searchController,
              onSubmitted: (_) => loadProducts(),
              decoration: const InputDecoration(
                hintText: 'Search products (e.g. phone, watch)',
                prefixIcon: Icon(Icons.search),
                border: OutlineInputBorder(),
              ),
            ),
          ),
          Expanded(child: buildBody()),
        ],
      ),
    );
  }
}
