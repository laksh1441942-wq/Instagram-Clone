import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:frontend/widgets/like_animation.dart';

void main() {
  testWidgets('plays once and calls onEnd after the animation', (tester) async {
    var isAnimating = false;
    var endCalls = 0;

    await tester.pumpWidget(
      MaterialApp(
        home: StatefulBuilder(
          builder: (context, setState) => Center(
            child: TextButton(
              onPressed: () => setState(() => isAnimating = true),
              child: LikeAnimation(
                duration: const Duration(milliseconds: 100),
                isAnimating: isAnimating,
                onEnd: () {
                  endCalls++;
                  setState(() => isAnimating = false);
                },
                child: const Icon(Icons.favorite),
              ),
            ),
          ),
        ),
      ),
    );

    await tester.tap(find.byType(TextButton));
    await tester.pumpAndSettle();

    expect(endCalls, 1);
    expect(isAnimating, isFalse);
  });
}
