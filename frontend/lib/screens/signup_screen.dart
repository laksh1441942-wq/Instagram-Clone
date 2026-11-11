import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:frontend/widgets/text_field_input.dart';

class SignupScreen extends StatefulWidget {
  const SignupScreen({super.key});

  @override
  State<SignupScreen> createState() => _SignupScreenState();
}

class _SignupScreenState extends State<SignupScreen> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final TextEditingController _bioController = TextEditingController();
  final TextEditingController _usernameController = TextEditingController();

  @override
  void dispose() {
    super.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    _bioController.dispose();
    _usernameController.dispose();
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
              const SizedBox(height: 14),
              Stack(
                children: [
                  CircleAvatar(
                    radius: 64,
                    backgroundImage: NetworkImage(
                      "https://imgs.search.brave.com/1zN7rj-nZAGX01kzGc3h_je8NKm-7kWjd5tY3xVaRc0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/bWFnbmlmaWMuY29t/L3ByZW1pdW0tcGhv/dG8vaGVhZC1zaG90/LWNvbmZpZGVudC1o/YW5kc29tZS1iZWFy/ZGVkLW1hbi1sb29r/aW5nLWNhbWVyYS1w/b3NpbmctcHJvZmls/ZS1waWN0dXJlLXN0/YW5kaW5nLWhvbWUt/c2VyaW91cy1mb2N1/c2VkLW1hbGUtbWFr/aW5nLXZpZGVvLWNh/bGwtdXNpbmctd2Vi/Y2FtLWRpc3RhbmNl/LWpvYi1pbnRlcnZp/ZXctb25saW5lLXN0/dWR5XzY1MDM2Ni03/ODcwLmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDAmcT04MA",
                    ),
                  ),
                  Positioned(
                    left: 90,
                    top: 85,
                    child: IconButton(
                      onPressed: () {},
                      icon: Icon(Icons.add_a_photo),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 14),
              TextFieldInput(
                textEditingController: _emailController,
                textHint: "Username",
                textInputType: TextInputType.name,
              ),
              const SizedBox(height: 14),
              TextFieldInput(
                textEditingController: _emailController,
                textHint: "Email address",
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
              const SizedBox(height: 14),
              TextFieldInput(
                textEditingController: _emailController,
                textHint: "Bio",
                textInputType: TextInputType.text,
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
                  "Sign Up",
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
                    child: Text("Already have an account? "),
                  ),
                  Container(
                    padding: EdgeInsets.symmetric(vertical: 8),
                    child: Text(
                      "Log In.",
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
