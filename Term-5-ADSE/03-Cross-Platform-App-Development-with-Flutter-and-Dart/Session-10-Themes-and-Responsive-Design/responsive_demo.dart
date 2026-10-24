// Session 10 - Example 2: One screen that adapts to phone, tablet and desktop
// Run: copy into lib/main.dart, run on Chrome/desktop and resize the window.
import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ResponsivePage(),
  ));
}

class ResponsivePage extends StatelessWidget {
  const ResponsivePage({super.key});

  @override
  Widget build(BuildContext context) {
    // MediaQuery tells us the full screen size.
    final screenWidth = MediaQuery.sizeOf(context).width;

    return Scaffold(
      appBar: AppBar(title: Text('Width: ${screenWidth.toInt()} px')),
      // LayoutBuilder tells us how much space THIS widget has.
      body: LayoutBuilder(
        builder: (context, constraints) {
          // Step 1: pick the number of columns from the available width.
          int columns;
          if (constraints.maxWidth < 600) {
            columns = 1; // phone
          } else if (constraints.maxWidth < 1000) {
            columns = 2; // tablet
          } else {
            columns = 4; // desktop
          }

          // Step 2: build a grid with that many columns.
          return GridView.count(
            crossAxisCount: columns,
            padding: const EdgeInsets.all(12),
            mainAxisSpacing: 12,
            crossAxisSpacing: 12,
            childAspectRatio: 3,
            children: List.generate(8, (index) {
              return Card(
                child: Center(child: Text('Course ${index + 1}')),
              );
            }),
          );
        },
      ),
    );
  }
}
