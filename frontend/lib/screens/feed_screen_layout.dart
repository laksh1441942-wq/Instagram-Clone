import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/screens/add_post_screen.dart';
import 'package:frontend/utils/colors.dart';
import 'package:frontend/widgets/post_card.dart';

class FeedScreenLayout extends StatefulWidget {
  final List<CameraDescription> cameras;

  const FeedScreenLayout({super.key, required this.cameras});

  @override
  State<FeedScreenLayout> createState() => _FeedScreenLayoutState();
}

class _FeedScreenLayoutState extends State<FeedScreenLayout> {
  int _page = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            IconButton(
              onPressed: () {
                setState(() {
                  _page = 1;
                  AddPostScreen(cameras: widget.cameras);
                });
              },
              icon: Icon(
                Icons.add,
                size: 32,
                color: _page == 1
                    ? AppColors.primaryTextColor
                    : AppColors.secondaryTextColor,
              ),
            ),
            SvgPicture.asset(
              "assets/instagram-text-icon.svg",
              height: 32,
              colorFilter: ColorFilter.mode(
                AppColors.primaryTextColor,
                BlendMode.srcIn,
              ),
            ),
            IconButton(
              onPressed: () {
                setState(() {
                  _page = 2;
                  const Center(child: Text("Activity"));
                });
              },
              icon: Icon(
                Icons.favorite_border_outlined,
                size: 32,
                color: _page == 2
                    ? AppColors.primaryTextColor
                    : AppColors.secondaryTextColor,
              ),
            ),
          ],
        ),
      ),
      body: PostCard(),
    );
  }
}
