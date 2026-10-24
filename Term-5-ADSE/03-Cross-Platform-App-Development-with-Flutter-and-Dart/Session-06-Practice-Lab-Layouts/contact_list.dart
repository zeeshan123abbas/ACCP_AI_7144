// contact_list.dart
// Lab Task 2: a contact list that uses our own reusable ContactTile widget.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: ContactListPage()));
}

class ContactListPage extends StatelessWidget {
  const ContactListPage({super.key});

  @override
  Widget build(BuildContext context) {
    // Data: each contact is a name and a phone number.
    final List<Map<String, String>> contacts = [
      {'name': 'Ali Raza', 'phone': '0300 1111111'},
      {'name': 'Fatima Noor', 'phone': '0301 2222222'},
      {'name': 'Hassan Javed', 'phone': '0302 3333333'},
      {'name': 'Sana Tariq', 'phone': '0303 4444444'},
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Contacts')),
      body: ListView.builder(
        itemCount: contacts.length,
        itemBuilder: (context, index) {
          // Reuse the same widget for every contact.
          return ContactTile(
            name: contacts[index]['name']!,
            phone: contacts[index]['phone']!,
          );
        },
      ),
    );
  }
}

// Our own reusable widget. It receives data through its constructor.
class ContactTile extends StatelessWidget {
  final String name;
  final String phone;

  const ContactTile({super.key, required this.name, required this.phone});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Row(
        children: [
          // First letter of the name inside a circle.
          CircleAvatar(child: Text(name[0])),
          const SizedBox(width: 12),
          // Expanded so long names never overflow the row.
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(name, style: const TextStyle(fontWeight: FontWeight.bold)),
                Text(phone, style: const TextStyle(color: Colors.grey)),
              ],
            ),
          ),
          const Icon(Icons.call, color: Colors.green),
        ],
      ),
    );
  }
}
