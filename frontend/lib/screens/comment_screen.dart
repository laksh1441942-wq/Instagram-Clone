import 'package:flutter/material.dart';
import 'package:frontend/utils/colors.dart';
import 'package:frontend/widgets/comment_card.dart';

class CommentScreen extends StatelessWidget {
  const CommentScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: AppColors.mobileBackgroundColor,
        title: const Text("Comments"),
        centerTitle: true,
      ),
      body: CommentCard(),
      bottomNavigationBar: SafeArea(
        child: Container(
          height: kToolbarHeight,
          margin: EdgeInsets.only(
            bottom: MediaQuery.of(context).viewInsets.bottom,
          ),
          padding: EdgeInsets.only(right: 8, left: 16),
          child: Row(
            children: [
              CircleAvatar(
                backgroundImage: NetworkImage(
                  'https://imgs.search.brave.com/1zN7rj-nZAGX01kzGc3h_je8NKm-7kWjd5tY3xVaRc0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tcGhv/dG8vaGVhZC1zaG90/LWNvbmZpZGVudC1o/YW5kc29tZS1iZWFy/ZGVkLW1hbi1sb29r/aW5nLWNhbWVyYS1w/b3NpbmctcHJvZmls/ZS1waWN0dXJlLXN0/YW5kaW5nLWhvbWUt/c2VyaW91cy1mb2N1/c2VkLW1hbGUtbWFr/aW5nLXZpZGVvLWNh/bGwtdXNpbmctd2Vi/Y2FtLWRpc3RhbmNl/LWpvYi1pbnRlcnZp/ZXctb25saW5lLXN0/dWR5XzY1MDM2Ni03/ODcwLmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDAmcT04MA',
                ),
              ),
              Expanded(
                child: Padding(
                  padding: EdgeInsetsGeometry.only(left: 16, right: 8),
                  child: TextField(
                    decoration: InputDecoration(
                      hintText: "Comment as Alex_Meri_Jaan",
                      border: InputBorder.none,
                    ),
                  ),
                ),
              ),
              IconButton(
                onPressed: () {},
                icon: Icon(Icons.emoji_emotions),
                iconSize: 28,
                color: AppColors.primaryTextColor,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
