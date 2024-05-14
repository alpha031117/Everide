import 'dart:convert';

import 'package:everide_test/user.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;
import 'package:http/http.dart';
import 'package:everide_test/Constant/api.dart';  

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Client client = http.Client();
  List <User> users = [];

  @override
  void initState() {
    _retrieveUser();
    super.initState();
  }

  void _retrieveUser() async{
    try {
      users = [];

      List response = json.decode((await client.get(Uri.parse(api + '/user/'))).body);
      response.forEach((element) { 
        users.add(User.fromMap(element));
      });
      setState(() {});
    } catch (e) {
      print("Error is $e");
    }
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      body:
        Center(
          child: ListView.builder(
          itemCount: users.length, 
          itemBuilder: (BuildContext context, int index){
            return ListTile(
              title: Text(users[index].username),
              subtitle: Text(users[index].email),
            );
          }
        )
      ) // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
