import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:frontend/responsive/mobile_screen_layout.dart';
import 'package:frontend/screens/feed_screen_layout.dart';
import 'package:frontend/screens/login_screen.dart';
import 'package:frontend/screens/signup_screen.dart';
import 'package:frontend/screens/comment_screen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  List<CameraDescription> cameras = [];
  try {
    cameras = await availableCameras();
  } catch (error) {
    debugPrint("Unable to access cameras: $error");
  }

  runApp(MyApp(cameras: cameras));
}

class MyApp extends StatelessWidget {
  final List<CameraDescription> cameras;

  const MyApp({super.key, required this.cameras});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Instagram Clone',
      theme: ThemeData.dark(),
      home: CommentScreen(),
    );
  }
}
