import 'package:flutter/material.dart';
import 'package:frontend/responsive/mobile_screen_layout.dart';
// import 'package:frontend/screens/login_screen.dart';
// import 'package:frontend/screens/signup_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Instagram Clone',
      theme: ThemeData.dark(),
      home: MobileScreenLayout(),
    );
  }
}
