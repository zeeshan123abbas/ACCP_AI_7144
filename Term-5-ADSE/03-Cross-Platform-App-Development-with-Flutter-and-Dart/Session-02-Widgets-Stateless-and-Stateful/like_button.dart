// like_button.dart
// A small stateful toggle: tap the heart to like / unlike.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: Scaffold(body: Center(child: LikeButton()))));
}

class LikeButton extends StatefulWidget {
  const LikeButton({super.key});

  @override
  State<LikeButton> createState() => _LikeButtonState();
}

class _LikeButtonState extends State<LikeButton> {
  bool isLiked = false; // state: liked or not

  @override
  Widget build(BuildContext context) {
    return IconButton(
      iconSize: 64,
      // Choose icon and colour based on the state.
      icon: Icon(isLiked ? Icons.favorite : Icons.favorite_border),
      color: isLiked ? Colors.red : Colors.grey,
      onPressed: () {
        setState(() {
          isLiked = !isLiked; // flip true <-> false
        });
      },
    );
  }
}
