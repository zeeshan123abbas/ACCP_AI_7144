// Session 14 - Step 4: Recipe Finder (search + list + navigation)
// lib/ needs: main.dart, recipe.dart, recipe_service.dart, detail_screen.dart
import 'package:flutter/material.dart';
import 'detail_screen.dart';
import 'recipe.dart';
import 'recipe_service.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    theme: ThemeData(colorSchemeSeed: Colors.orange),
    home: const SearchScreen(),
  ));
}

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final searchController = TextEditingController();

  // Three simple state variables instead of FutureBuilder.
  List<Recipe> recipes = [];
  bool isLoading = false;
  String? errorMessage;

  @override
  void initState() {
    super.initState();
    runSearch(); // show all recipes at start
  }

  Future<void> runSearch() async {
    setState(() {
      isLoading = true;
      errorMessage = null;
    });
    try {
      final results = await RecipeService.search(searchController.text);
      if (!mounted) return; // screen closed while we were waiting
      setState(() {
        recipes = results;
        isLoading = false;
      });
    } catch (error) {
      if (!mounted) return;
      setState(() {
        errorMessage = 'Could not load recipes. Check your internet.';
        isLoading = false;
      });
    }
  }

  // Decide what to show in the body.
  Widget buildBody() {
    if (isLoading) return const Center(child: CircularProgressIndicator());
    if (errorMessage != null) return Center(child: Text(errorMessage!));
    if (recipes.isEmpty) return const Center(child: Text('No recipes found.'));

    return ListView.builder(
      itemCount: recipes.length,
      itemBuilder: (context, index) {
        final recipe = recipes[index];
        return ListTile(
          leading: Hero(
            tag: 'recipe-${recipe.id}',
            child: CircleAvatar(backgroundImage: NetworkImage(recipe.image)),
          ),
          title: Text(recipe.name),
          subtitle: Text('${recipe.cuisine} · ⭐ ${recipe.rating}'),
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => DetailScreen(recipe: recipe)),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recipe Finder')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: TextField(
              controller: searchController,
              textInputAction: TextInputAction.search,
              onSubmitted: (_) => runSearch(),
              decoration: InputDecoration(
                hintText: 'Search e.g. pizza, chicken, salad',
                border: const OutlineInputBorder(),
                suffixIcon: IconButton(icon: const Icon(Icons.search), onPressed: runSearch),
              ),
            ),
          ),
          Expanded(child: RefreshIndicator(onRefresh: runSearch, child: buildBody())),
        ],
      ),
    );
  }
}
