import 'package:flutter/material.dart';

class TextFieldInput extends StatelessWidget {
  final TextEditingController textEditingController;
  final bool isPass;
  final String textHint;
  final TextInputType textInputType;
  final Icon prefixIcon;
  final Icon suffixIcon;
  const TextFieldInput({
    super.key,
    required this.textEditingController,
    this.isPass = false,
    required this.textHint,
    required this.textInputType,
    this.suffixIcon = const Icon(null),
    this.prefixIcon = const Icon(null),
  });

  @override
  Widget build(BuildContext context) {
    final inputBorder = OutlineInputBorder(
      borderSide: Divider.createBorderSide(context),
    );
    return TextField(
      controller: textEditingController,
      decoration: InputDecoration(
        suffixIcon: suffixIcon,
        hintText: textHint,
        border: inputBorder,
        focusedBorder: inputBorder,
        enabledBorder: inputBorder,
        filled: true,
        contentPadding: EdgeInsets.all(8),
      ),
      keyboardType: textInputType,
      obscureText: isPass,
    );
  }
}
