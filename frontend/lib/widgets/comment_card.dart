import 'package:flutter/material.dart';

class CommentCard extends StatelessWidget {
  const CommentCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 8, horizontal: 16),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          CircleAvatar(
            backgroundImage: NetworkImage(
              'https://imgs.search.brave.com/PPkuhriUbI-hRlJjTIPNXmJVkzGMSRBVwR7KNte9wZM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyNi8x/MC8yNS8yMC80OC9z/dWp1LWZvdG8td2F0/ZXJmYWxsLTEwNTQx/OTc0XzY0MC5qcGc',
            ),
            radius: 18,
          ),
          Expanded(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                RichText(
                  text: TextSpan(
                    children: [
                      TextSpan(
                        text: "  Username",
                        style: TextStyle(fontWeight: FontWeight.bold),
                      ),
                      TextSpan(text: " 2W"),
                    ],
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(left: 8, top: 4),
                  child: Text(
                    "This is a beautiful scenery and i have made it my dp, wish i could visit it one day, and i am typing this to make my comment longer and longer to test it's postion",
                  ),
                ),
              ],
            ),
          ),
          IconButton(onPressed: () {}, icon: Icon(Icons.favorite)),
        ],
      ),
    );
  }
}
