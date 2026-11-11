import 'package:flutter/cupertino.dart';
import 'package:frontend/utils/colors.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';

class MobileScreenLayout extends StatefulWidget {
  const MobileScreenLayout({super.key});

  @override
  State<MobileScreenLayout> createState() => _MobileScreenLayoutState();
}

class _MobileScreenLayoutState extends State<MobileScreenLayout> {
  int _page = 0;
  late PageController pageController;
  @override
  void initState() {
    super.initState();
    pageController = PageController();
  }

  void navigationTapped(int page) {
    pageController.jumpToPage(page);
  }

  void onPageChanged(int page) {
    setState(() {
      _page = page;
    });
  }

  @override
  void dispose() {
    super.dispose();
    pageController.dispose();
  }

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
                  _page = 6;
                });
              },
              icon: Icon(
                Icons.add,
                size: 32,
                color: _page == 6
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
              onPressed: () {},
              icon: Icon(Icons.favorite_border_outlined, size: 32),
            ),
          ],
        ),
      ),
      body: PageView(
        controller: pageController,
        onPageChanged: onPageChanged,
        physics: NeverScrollableScrollPhysics(),
        children: [
          Center(child: Text("Home")),
          Center(child: Text("Reels")),
          Center(child: Text("Notif")),
          Center(child: Text("Explore")),
          Center(child: Text("profile")),
        ],
      ),

      bottomNavigationBar: CupertinoTabBar(
        items: [
          BottomNavigationBarItem(
            icon: Icon(
              Icons.home,
              size: 30,
              color: _page == 0
                  ? AppColors.primaryTextColor
                  : AppColors.secondaryTextColor,
            ),
          ),
          BottomNavigationBarItem(
            icon: SvgPicture.asset(
              "assets/instagram-reels-icon.svg",
              height: 24,
              colorFilter: ColorFilter.mode(
                _page == 1
                    ? AppColors.primaryTextColor
                    : AppColors.secondaryTextColor,
                BlendMode.srcIn,
              ),
            ),
          ),
          BottomNavigationBarItem(
            icon: SvgPicture.asset(
              "assets/instagram-message-icon.svg",
              height: 32,
              colorFilter: ColorFilter.mode(
                _page == 2
                    ? AppColors.primaryTextColor
                    : AppColors.secondaryTextColor,
                BlendMode.srcIn,
              ),
            ),
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.search,
              size: 32,
              color: _page == 3
                  ? AppColors.primaryTextColor
                  : AppColors.secondaryTextColor,
            ),
          ),
          BottomNavigationBarItem(
            icon: CircleAvatar(
              radius: 15,
              backgroundImage: NetworkImage(
                "https://imgs.search.brave.com/1zN7rj-nZAGX01kzGc3h_je8NKm-7kWjd5tY3xVaRc0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tcGhv/dG8vaGVhZC1zaG90/LWNvbmZpZGVudC1o/YW5kc29tZS1iZWFy/ZGVkLW1hbi1sb29r/aW5nLWNhbWVyYS1w/b3NpbmctcHJvZmls/ZS1waWN0dXJlLXN0/YW5kaW5nLWhvbWUt/c2VyaW91cy1mb2N1/c2VkLW1hbGUtbWFr/aW5nLXZpZGVvLWNh/bGwtdXNpbmctd2Vi/Y2FtLWRpc3RhbmNl/LWpvYi1pbnRlcnZp/ZXctb25saW5lLXN0/dWR5XzY1MDM2Ni03/ODcwLmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDAmcT04MA",
              ),
            ),
          ),
        ],
        onTap: navigationTapped,
      ),
    );
  }
}
