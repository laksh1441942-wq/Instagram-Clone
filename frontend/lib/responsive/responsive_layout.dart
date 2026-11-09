import 'package:flutter/material.dart';
import 'package:frontend/utils/dimensions.dart';

class ResponsiveLayout extends StatelessWidget {
  final Widget webScreenLayout;
  final Widget mobileScreenLayout;
  const ResponsiveLayout({super.key, required this.mobileScreenLayout, required this.webScreenLayout});
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(builder: (context, constraints){
      if(constraints.maxWidth > webScreenSize){
        //web screen
        return webScreenLayout;
      }
      //mobile screen
      return mobileScreenLayout;
    });
  }
}