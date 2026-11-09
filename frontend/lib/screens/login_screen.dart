import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/widgets/text_field_input.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  void dispose() {
    super.dispose();
    _emailController.dispose();
    _passwordController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Container(
          padding: EdgeInsets.symmetric(horizontal: 32),
          width: double.infinity,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Flexible(flex: 1, child: Container()),
              SvgPicture.asset(
                "assets/instagram-text-icon.svg",
                colorFilter: ColorFilter.mode(Colors.white, BlendMode.srcIn),
                height: 54,
              ),
              const SizedBox(height: 34),
              TextFieldInput(
                textEditingController: _emailController,
                textHint: "Username or email address",
                textInputType: TextInputType.emailAddress,
              ),
              const SizedBox(height: 14),
              TextFieldInput(
                textEditingController: _passwordController,
                textHint: "Password",
                textInputType: TextInputType.visiblePassword,
                isPass: true,
                suffixIcon: Icon(Icons.visibility_off),
              ),
              Container(
                padding: EdgeInsets.symmetric(vertical: 5),
                alignment: Alignment(1, 0),
                child: Text(
                  "Forgetted password?",
                  style: TextStyle(
                    fontWeight: FontWeight(500),
                    color: Colors.lightBlueAccent,
                  ),
                ),
              ),
              const SizedBox(height: 34),
              Container(
                width: double.infinity,
                alignment: Alignment.center,
                padding: EdgeInsets.symmetric(vertical: 13),
                decoration: ShapeDecoration(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10)),
                  ),
                  color: const Color.fromARGB(255, 44, 141, 220),
                ),
                child: Text(
                  "Log In",
                  style: TextStyle(fontWeight: FontWeight(800), fontSize: 15),
                ),
              ),
              const SizedBox(height: 12),
              Flexible(flex: 2, child: Container()),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 8),
                    child: Text("Don't you have an account? "),
                  ),
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 8),
                    child: Text(
                      "Sign Up.",
                      style: TextStyle(fontWeight: FontWeight(800)),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
