import 'package:flutter/material.dart';

class LikeAnimation extends StatefulWidget {
  final Widget child;
  final Duration duration;
  final bool isAnimating;
  final bool smallLike;
  final VoidCallback? onEnd;

  const LikeAnimation({
    required this.child,
    super.key,
    required this.onEnd,
    required this.isAnimating,
    this.smallLike = false,
    this.duration = const Duration(milliseconds: 150),
  });

  @override
  State<LikeAnimation> createState() => _LikeAnimationState();
}

class _LikeAnimationState extends State<LikeAnimation>
    with SingleTickerProviderStateMixin {
  late final AnimationController controller;
  late Animation<double> scale;

  @override
  void initState() {
    super.initState();
    controller = AnimationController(vsync: this, duration: widget.duration);
    scale = Tween<double>(begin: widget.smallLike ? 1 : 0.5, end: 1.2).animate(
      CurvedAnimation(
        parent: controller,
        curve: Curves.easeOutBack,
        reverseCurve: Curves.easeIn,
      ),
    );
    if (widget.isAnimating) {
      _playAnimation();
    }
  }

  @override
  void didUpdateWidget(covariant LikeAnimation oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (widget.duration != oldWidget.duration) {
      controller.duration = widget.duration;
    }
    if (widget.isAnimating && !oldWidget.isAnimating) {
      _playAnimation();
    }
  }

  Future<void> _playAnimation() async {
    await controller.forward(from: 0);
    await controller.reverse();
    if (mounted) {
      widget.onEnd?.call();
    }
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: controller,
      child: ScaleTransition(scale: scale, child: widget.child),
    );
  }
}
