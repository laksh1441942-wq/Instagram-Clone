import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/utils/colors.dart';
import 'package:frontend/widgets/like_animation.dart';

class PostCard extends StatefulWidget {
  const PostCard({super.key});

  @override
  State<PostCard> createState() => _PostCardState();
}

class _PostCardState extends State<PostCard> {
  bool isLikeAnimating = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppColors.mobileBackgroundColor,
      padding: EdgeInsets.symmetric(vertical: 10),
      child: Column(
        children: [
          // HEADER SECTION
          Container(
            padding: EdgeInsets.symmetric(
              vertical: 4,
              horizontal: 16,
            ).copyWith(right: 0),
            child: Row(
              children: [
                CircleAvatar(
                  radius: 16,
                  backgroundImage: NetworkImage(
                    "https://imgs.search.brave.com/1zN7rj-nZAGX01kzGc3h_je8NKm-7kWjd5tY3xVaRc0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tcGhv/dG8vaGVhZC1zaG90/LWNvbmZpZGVudC1o/YW5kc29tZS1iZWFy/ZGVkLW1hbi1sb29r/aW5nLWNhbWVyYS1w/b3NpbmctcHJvZmls/ZS1waWN0dXJlLXN0/YW5kaW5nLWhvbWUt/c2VyaW91cy1mb2N1/c2VkLW1hbGUtbWFr/aW5nLXZpZGVvLWNh/bGwtdXNpbmctd2Vi/Y2FtLWRpc3RhbmNl/LWpvYi1pbnRlcnZp/ZXctb25saW5lLXN0/dWR5XzY1MDM2Ni03/ODcwLmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDAmcT04MA",
                  ),
                ),
                Expanded(
                  child: Padding(
                    padding: EdgeInsetsGeometry.only(left: 10),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          "Alex_Meri_Jaan",
                          style: TextStyle(fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                ),
                IconButton(
                  onPressed: () {
                    showDialog(
                      context: context,
                      builder: (context) => Dialog(
                        child: ListView(
                          padding: EdgeInsets.symmetric(
                            vertical: 16,
                            horizontal: 10,
                          ),
                          shrinkWrap: true,
                          children: ["Not interested", "Report"]
                              .map(
                                (e) => InkWell(
                                  onTap: () {},
                                  child: Container(
                                    padding: EdgeInsets.symmetric(
                                      vertical: 16,
                                      horizontal: 10,
                                    ),
                                    child: Text(e),
                                  ),
                                ),
                              )
                              .toList(),
                        ),
                      ),
                    );
                  },
                  icon: Icon(Icons.more_vert),
                ),
              ],
            ),
            // IMAGE SECTION
          ),
          GestureDetector(
            onDoubleTap: () {
              if (!isLikeAnimating) {
                setState(() {
                  isLikeAnimating = true;
                });
              }
            },
            child: Stack(
              children: [
                SizedBox(
                  height: MediaQuery.of(context).size.height * 0.35,
                  width: double.infinity,
                  child: Image.network(
                    "https://imgs.search.brave.com/PPkuhriUbI-hRlJjTIPNXmJVkzGMSRBVwR7KNte9wZM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyNi8x/MC8yNS8yMC80OC9z/dWp1LWZvdG8td2F0/ZXJmYWxsLTEwNTQx/OTc0XzY0MC5qcGc",
                  ),
                ),
                Positioned.fill(
                  child: IgnorePointer(
                    child: LikeAnimation(
                      onEnd: () {
                        if (mounted) {
                          setState(() {
                            isLikeAnimating = false;
                          });
                        }
                      },
                      isAnimating: isLikeAnimating,
                      child: Icon(
                        Icons.favorite,
                        color: Colors.white,
                        size: 100,
                        shadows: [
                          Shadow(color: Colors.black54, blurRadius: 12),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Row(
            children: [
              SizedBox(width: 14),
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  SvgPicture.asset(
                    "assets/instagram-heart-icon.svg",
                    height: 20,

                    colorFilter: ColorFilter.mode(
                      AppColors.primaryTextColor,
                      BlendMode.srcIn,
                    ),
                  ),
                  SizedBox(width: 4),
                  Text("2.5K", style: TextStyle(fontWeight: FontWeight.bold)),
                ],
              ),
              SizedBox(width: 8),
              Row(
                children: [
                  GestureDetector(
                    onTap: () {},
                    child: SvgPicture.asset(
                      "assets/instagram-comment-icon.svg",
                      height: 20,
                      colorFilter: ColorFilter.mode(
                        AppColors.primaryTextColor,
                        BlendMode.srcIn,
                      ),
                    ),
                  ),
                  SizedBox(width: 4),
                  Text("500", style: TextStyle(fontWeight: FontWeight.bold)),
                ],
              ),
              SizedBox(width: 8),
              Row(
                children: [
                  GestureDetector(
                    onTap: () {},
                    child: SvgPicture.asset(
                      "assets/instagram-share-icon.svg",
                      height: 20,
                      colorFilter: ColorFilter.mode(
                        AppColors.primaryTextColor,
                        BlendMode.srcIn,
                      ),
                    ),
                  ),
                  SizedBox(width: 4),
                  Text("1K", style: TextStyle(fontWeight: FontWeight.bold)),
                ],
              ),
              Expanded(
                child: Align(
                  alignment: AlignmentGeometry.centerRight,
                  child: IconButton(
                    onPressed: () {},
                    icon: SvgPicture.asset(
                      "assets/instagram-save-icon.svg",
                      height: 20,
                      colorFilter: ColorFilter.mode(
                        AppColors.primaryTextColor,
                        BlendMode.srcIn,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
          Container(
            padding: EdgeInsets.symmetric(horizontal: 8),
            child: RichText(
              text: TextSpan(
                style: TextStyle(color: AppColors.primaryTextColor),
                children: [
                  TextSpan(
                    text: "Alex_Meri_Jaan",
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                  TextSpan(
                    text:
                        "  The photo is AI Generated but the prompt is human made so enjoys the view and share it with your friends",
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
