// Session 11 - Example 3: The same notes idea, but stored in Cloud Firestore
// Before running: create a Firebase project and run `flutterfire configure`
// (it generates lib/firebase_options.dart).
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'firebase_options.dart';

Future<void> main() async {
  // Step 1: Flutter must be ready before we call native code.
  WidgetsFlutterBinding.ensureInitialized();
  // Step 2: connect the app to your Firebase project.
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: CloudNotesPage()));
}

class CloudNotesPage extends StatelessWidget {
  const CloudNotesPage({super.key});

  // A reference to the "notes" collection in Firestore.
  CollectionReference<Map<String, dynamic>> get notesCollection =>
      FirebaseFirestore.instance.collection('notes');

  // Step 3: add a document with a title and a server timestamp.
  Future<void> addNote() async {
    await notesCollection.add({
      'title': 'Note at ${DateTime.now().toLocal()}',
      'createdAt': FieldValue.serverTimestamp(),
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Cloud Notes (Firestore)')),
      floatingActionButton: FloatingActionButton(
        onPressed: addNote,
        child: const Icon(Icons.add),
      ),
      // Step 4: StreamBuilder listens for live changes in the collection.
      body: StreamBuilder<QuerySnapshot<Map<String, dynamic>>>(
        stream: notesCollection.orderBy('createdAt', descending: true).snapshots(),
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          if (!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }
          final docs = snapshot.data!.docs;
          return ListView.builder(
            itemCount: docs.length,
            itemBuilder: (context, index) {
              final doc = docs[index];
              return ListTile(
                title: Text(doc['title']),
                // Delete the document using its id.
                trailing: IconButton(
                  icon: const Icon(Icons.delete),
                  onPressed: () => notesCollection.doc(doc.id).delete(),
                ),
              );
            },
          );
        },
      ),
    );
  }
}
