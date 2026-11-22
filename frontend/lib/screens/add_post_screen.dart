import 'package:camera/camera.dart';
import 'package:flutter/material.dart';

class AddPostScreen extends StatefulWidget {
  final List<CameraDescription> cameras;

  const AddPostScreen({super.key, required this.cameras});

  @override
  State<AddPostScreen> createState() => _AddPostScreenState();
}

class _AddPostScreenState extends State<AddPostScreen> {
  CameraController? _controller;
  String? _error;

  @override
  void initState() {
    super.initState();
    _initializeCamera();
  }

  Future<void> _initializeCamera() async {
    if (widget.cameras.isEmpty) {
      if (!mounted) return;
      setState(() {
        _error = "No camera is available";
      });
      return;
    }

    final controller = CameraController(
      widget.cameras.first,
      ResolutionPreset.high,
    );

    try {
      await controller.initialize();
      if (!mounted) {
        await controller.dispose();
        return;
      }
      setState(() {
        _controller = controller;
      });
    } catch (error) {
      await controller.dispose();
      if (!mounted) return;
      setState(() {
        _error = "Unable to initialize camera: $error";
      });
    }
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_error != null) {
      return Center(child: Text(_error!, textAlign: TextAlign.center));
    }

    final controller = _controller;
    if (controller == null || !controller.value.isInitialized) {
      return const Center(child: CircularProgressIndicator());
    }

    return CameraPreview(controller);
  }
}
