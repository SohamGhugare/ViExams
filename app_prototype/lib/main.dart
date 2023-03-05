// import 'dart:html';
import 'dart:io' as io;
import 'dart:io';

// import 'dart:html';

import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:open_filex/open_filex.dart';
import "package:pdf/widgets.dart" as w;
import 'package:path_provider/path_provider.dart';
import 'package:simple_gradient_text/simple_gradient_text.dart';
import 'package:simple_gradient_text/simple_gradient_text.dart';


void main() {
  runApp(const MaterialApp(
    home: Home(),
    debugShowCheckedModeBanner: false,
  ));
}

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  // var options = <String> ["Option1", "Option2"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
            children: <Widget>[
          TextButton(child: Icon(Icons.search,
          color: Colors.white,),
          onPressed: () {
            Navigator.push(context, MaterialPageRoute(builder: (context){
              return const SearchPage();
            }));
          },),
            SizedBox(width: 90,),
            Expanded(child: Container(child: Text("ViExams")))]),
        centerTitle: true,
        backgroundColor: Colors.black,
      ),
      backgroundColor: Colors.black,
      endDrawer: Drawer(
        backgroundColor: Color.fromRGBO(4, 1, 26, 1),
        child: Column(
          children: <Widget>[
            SizedBox(height: 100,),
            TextButton(
              child: Row(
                children: <Widget> [
                  Icon(Icons.search,
                  color: Colors.white,
                  size: 30,),
                  SizedBox(width: 10),
                  Text("Explore",
                  style: TextStyle(color: Colors.white,
                  fontSize: 25),),
                ],
              ),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context){
                  return const SearchPage();
                }));
              },
            ),
            SizedBox(height: 20,),
            TextButton(
              child: Row(
                children: <Widget>[
                  Icon(Icons.cloud_upload_outlined,
                  color: Colors.white,
                  size: 30,),
                  SizedBox(width: 10,),
                  Text("Upload",
                  style: TextStyle(color: Colors.white,
                  fontSize: 25)),
                ],
              ),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context){
                  return const UploadPage();
                }));
              },
            ),
          SizedBox(height: 20,),
          TextButton(
            child: Row(
              children: <Widget> [
                Icon(Icons.settings,
                color: Colors.white,
                size: 30,),
                SizedBox(width: 10),
                Text("Generate",
                style: TextStyle(color: Colors.white,
                fontSize: 25),)
              ],
            ),
            onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (context){
                return const GeneratePage();
              }));
            },
          ),
            SizedBox(height: 20,),
            TextButton(
              child: Row(
                children: <Widget> [
                  Icon(Icons.help_outline,
                  color: Colors.white,
                  size: 30,),
                  SizedBox(width: 10,),
                  Text("About Us",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 25,
                  ),)
                ],
              ),
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context){
                  return const AboutUsPage();
                }));
              },
            ),
            SizedBox(height: 500,),
            Text("Made With ❤",
              style: TextStyle(
                  color: Colors.white
              ),
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget> [
            Padding(padding: EdgeInsets.fromLTRB(40, 30, 20, 20)),
            Text("EXAMS..?",
            style: TextStyle(
              fontSize: 55,
              fontFamily: "Poppins",
              fontWeight: FontWeight.bold,
              color: Colors.white,
              letterSpacing: 9,
            ),),
            SizedBox(height: 0,),
            GradientText("Don't Worry!",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 60,
                fontFamily: "Poppins"
              ),
              colors: [
                Colors.blue,
                Colors.redAccent
              ],
            ),
            SizedBox(height: 0,),
            Text("We've got you covered",
            style: TextStyle(
              color: Colors.white,
              fontSize: 40,
              fontWeight: FontWeight.bold,
              fontFamily: "Poppins",
            ),
            ),
            Image.asset("assets/pngwing.png"),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.red
                  ),
                  child: Row(
                    children: <Widget> [
                      Text("Get Started",
                      style: TextStyle(
                        fontSize: 20
                      ),),
                      Icon(Icons.play_arrow_outlined),
                    ],
                  ),
                  onPressed: () {
                    Navigator.push(context, MaterialPageRoute(builder: (context){
                      return const OptionsPage();
                    }));
                  },
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}


class UploadPage extends StatelessWidget {
  const UploadPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Upload Your Docs"),
        centerTitle: true,
        backgroundColor: Colors.black,
      ),
      backgroundColor: Colors.black,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget> [
            TextButton(
              child: Column(
                children: <Widget> [
                  Icon(Icons.cloud_upload,
                  size: 50,),
                  SizedBox(height: 10,),
                  Text("Upload",
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 30
                  ),
                  ),
                ],
              ),
              onPressed: (){
                pickFile();
              },
            )
          ],
        ),
      ),
    );
  }
}

void pickFile() async{
  final result = await FilePicker.platform.pickFiles(allowMultiple: false);

  if (result==null) return;

  var selectedFile = io.File(result.files.single.path!);

  final file = result.files.first;
  _saveFile(selectedFile);


  
  print(result.files.first.name);
  print(result.files.first.size);
  print(result.files.first.path);



}

void openFile(PlatformFile file){
  OpenFilex.open(file.path);
}

void _saveFile(var selectedFile) async {
  final directory = await getApplicationDocumentsDirectory();
  final path = directory.path;
  final fileName = selectedFile.path.split('/').last;
  new Directory(r"C:\Coding\FlutterProjects\viexams_1\mypdfs\");

  var newFile = await selectedFile.copy("$fileName");
  print("Done!");
  }
  // You can now use the newFile variable to access the saved file.
class OptionsPage extends StatelessWidget {
  const OptionsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
      ),
      backgroundColor: Colors.black,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget> [
            SizedBox(
              height: 100,
              width: 300,
              child: ElevatedButton(
                style: ButtonStyle(
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(18),
                    )
                  )
                ),
                child:Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text("Upload",
                    style: TextStyle(
                      fontSize: 40
                    ),
                    ),
                    SizedBox(width: 20,),
                    Icon(Icons.cloud_upload_outlined,
                    color: Colors.white,
                    size: 50,)
                  ],
                ),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context){
                    return const UploadPage();
                  }));
                },
              ),
            ),
            SizedBox(height: 60,),
            SizedBox(
              height: 100,
              width: 300,
              child: ElevatedButton(
                  style: ButtonStyle(
                      shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                          RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(18),
                          )
                      )
                  ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text("Get Paper",
                    style: TextStyle(
                      fontSize: 40
                    ),
                    ),
                    SizedBox(width: 20,),
                    Icon(Icons.download_for_offline,
                    color: Colors.white,
                    size: 50,)
                  ],
                ),
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context){
                    return const SearchPage();
                  }));
                },
              ),
            )
          ],
        ),
      ),
    );
  }
}



class SearchPage extends StatelessWidget {
  const SearchPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Container(
          width: double.infinity,
          height: 40,
          decoration: BoxDecoration(
            color: Colors.white,borderRadius: BorderRadius.circular(5)
          ),
          child: Center(
            child: TextField(
              decoration: InputDecoration(
                prefixIcon: const Icon(Icons.search),
                suffixIcon: IconButton(
                  icon: const Icon(Icons.clear),
                  onPressed: (){},
                ),
                hintText: "Search Your Course Here",
                border: InputBorder.none
              ),
            ),
          ),
        ),
      ),
      backgroundColor: Colors.black,
    );
  }
}

class GeneratePage extends StatelessWidget {
  const GeneratePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: Text("Abhi Kaam Chal Raha Hai...🥲",
        style: TextStyle(
          fontSize: 30,
          color: Colors.white
        ),),
      ),
    );
  }
}

class AboutUsPage extends StatelessWidget {
  const AboutUsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("About The Team"),
        backgroundColor: Colors.black,
      ),
      backgroundColor: Colors.black,
      body: Container(
        padding: EdgeInsets.all(10),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget> [
            Padding(padding:EdgeInsets.fromLTRB(20, 50, 20, 0),
                child: Image.asset("assets/grouppic.jpg")),
            SizedBox(height: 20,),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 100),
              child: Text("ViExams Development Team",
              style: TextStyle(
                color: Colors.white
              ),),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 69),
              child: Row(
                children: <Widget> [
                  Icon(Icons.copyright,
                  color: Colors.white,),
                  Text("2023 - ViExams - All Rights Reserved",
                  style: TextStyle(
                    color: Colors.white
                  ),
                  ),
                ],
              ),
            ),
            SizedBox(height: 100,)
          ],
        ),
      ),
    );
  }
}
