import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter_image_compress/flutter_image_compress.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MapleLens',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFFE31837), // Canadian Red
          brightness: Brightness.light,
        ),
        useMaterial3: true,
      ),
      home: const ImageCapture(),
    );
  }
}

class ImageCapture extends StatefulWidget {
  const ImageCapture({super.key});

  @override
  createState() => _ImageCaptureState();
}

class _ImageCaptureState extends State<ImageCapture> {
  File? _imageFile;
  final ImagePicker _picker = ImagePicker();
  bool _isLoading = false;
  List<Map<String, dynamic>> _alternatives = [];
  String? _matchedCategory;

  void _clear() {
    setState(() {
      _imageFile = null;
      _alternatives = [];
      _matchedCategory = null;
    });
  }
  
  Future<File> _compressImage(File file) async {
    final filePath = file.absolute.path;
    final lastIndex = filePath.lastIndexOf(RegExp(r'.jp'));
    final splitted = filePath.substring(0, lastIndex);
    final outPath = "${splitted}_compressed.jpg";
    
    var result = await FlutterImageCompress.compressAndGetFile(
      file.absolute.path,
      outPath,
      quality: 70, // Adjust this value to balance quality and file size
      minWidth: 1024, // Max width
      minHeight: 1024, // Max height
    );
    
    return File(result!.path);
  }

  Future<void> _uploadImage(File imageFile) async {
    setState(() {
      _isLoading = true;
      _alternatives = [];
      _matchedCategory = null;
    });

    try {
      // Compress the image before uploading
      final compressedImage = await _compressImage(imageFile);
      
      // Create multipart request
      var request = http.MultipartRequest(
        'POST',
        Uri.parse('https://maple-lens-haokai-xuan-haokai-xuans-projects.vercel.app/api/upload/'),
      );

      // Add compressed file to request
      request.files.add(
        await http.MultipartFile.fromPath(
          'image',
          compressedImage.path,
          filename: 'image.jpg',
        ),
      );

      // Add headers
      request.headers.addAll({
        'Accept': 'application/json',
        'Origin': 'https://maple-lens-haokai-xuan-haokai-xuans-projects.vercel.app'
      });

      // Send request
      var streamedResponse = await request.send();
      var response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 200) {
        final result = json.decode(response.body);
        setState(() {
          _matchedCategory = result['matched_category'];
          if (result['canadian_alternatives'] != null) {
            _alternatives = List<Map<String, dynamic>>.from(
                result['canadian_alternatives']);
          }
        });
      } else {
        throw Exception('Failed to upload image: ${response.statusCode}');
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error: $e')),
      );
    } finally {
      setState(() {
        _isLoading = false;
      });
    }
  }

  Future<void> _pickImage(ImageSource source) async {
    try {
      final XFile? selected = await _picker.pickImage(
        source: source,
        imageQuality: 70, // Add initial compression at pickup
        maxWidth: 1024,   // Limit image dimensions
        maxHeight: 1024,
      );
      
      if (selected != null) {
        setState(() {
          _imageFile = File(selected.path);
        });
        // Upload image immediately after selection
        await _uploadImage(_imageFile!);
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error: $e')),
      );
    }
  }

  // ... existing _pickImage method remains the same ...

  @override
  Widget build(BuildContext context) {
    return Scaffold(
    appBar: AppBar(
      title: const Text(
        'MapleLens',
        style: TextStyle(
          fontFamily: 'Domine',
          fontSize: 24,  // You can adjust this size
          fontWeight: FontWeight.bold,
        ),
      ),
      backgroundColor: Theme.of(context).colorScheme.primary,
      foregroundColor: Colors.white,
    ),
      body: Column(
        children: <Widget>[
          if (_imageFile == null)
            Expanded(
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(
                      Icons.add_photo_alternate_outlined,
                      size: 64,
                      color: Colors.grey[400],
                    ),
                    const SizedBox(height: 16),
                    Text(
                      'Take a picture or choose from gallery',
                      style: TextStyle(
                        color: Colors.grey[600],
                        fontSize: 16,
                      ),
                    ),
                    const SizedBox(height: 24),
                    const Text(
                      '"See the Alternative"',
                      style: TextStyle(
                        fontFamily: 'Lugrasimo',
                        fontSize: 24,
                        color: Color(0xFFE31837),
                      ),
                    )
                  ],
                ),
              ),
            )
          else
            Expanded(
              child: Column(
                children: [
                  // Image and Loading Overlay
                  Stack(
                    children: [
                      Image.file(
                        _imageFile!,
                        height: 300,
                        width: double.infinity,
                        fit: BoxFit.cover,
                      ),
                      if (_isLoading)
                        Container(
                          height: 300,
                          color: Colors.black54,
                          child: const Center(
                            child: CircularProgressIndicator(
                              color: Colors.white,
                            ),
                          ),
                        ),
                      Positioned(
                        top: 16,
                        right: 16,
                        child: CircleAvatar(
                          backgroundColor: Colors.black54,
                          child: IconButton(
                            icon: const Icon(
                              Icons.close,
                              color: Colors.white,
                            ),
                            onPressed: _clear,
                          ),
                        ),
                      ),
                    ],
                  ),

                  // Category
                  if (_matchedCategory != null)
                    Container(
                      padding: const EdgeInsets.all(16),
                      width: double.infinity,
                      color: Theme.of(context).colorScheme.primary,
                      child: Text(
                        'Category: ${_matchedCategory!}',
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),

                  // Alternatives List
                  if (_alternatives.isNotEmpty)
                    Expanded(
                      child: ListView.builder(
                        itemCount: _alternatives.length,
                        itemBuilder: (context, index) {
                          final alternative = _alternatives[index];
                          return Card(
                            margin: const EdgeInsets.symmetric(
                              horizontal: 16,
                              vertical: 8,
                            ),
                            child: ListTile(
                              leading: alternative['image_url'] != null
                                  ? ClipRRect(
                                      borderRadius: BorderRadius.circular(8),
                                      child: Image.network(
                                        'https://maple-lens-haokai-xuan-haokai-xuans-projects.vercel.app${alternative['image_url']}',
                                        width: 60,
                                        height: 60,
                                        fit: BoxFit.cover,
                                        errorBuilder: (context, error,
                                                stackTrace) =>
                                            const Icon(Icons.image_not_supported),
                                      ),
                                    )
                                  : const Icon(Icons.image_not_supported),
                              title: Text(
                                alternative['brand'] ?? 'Unknown',
                                style: const TextStyle(
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          );
                        },
                      ),
                    ),
                ],
              ),
            ),
        ],
      ),
      bottomNavigationBar: BottomAppBar(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            _buildBottomBarButton(
              icon: Icons.photo_camera,
              label: 'Camera',
              onPressed: () => _pickImage(ImageSource.camera),
            ),
            _buildBottomBarButton(
              icon: Icons.photo_library,
              label: 'Gallery',
              onPressed: () => _pickImage(ImageSource.gallery),
            ),
          ],
        ),
      ),
    );
  }



  Widget _buildBottomBarButton({
    required IconData icon,
    required String label,
    required VoidCallback onPressed,
  }) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8.0),
      child: ElevatedButton.icon(
        onPressed: onPressed,
        icon: Icon(icon),
        label: Text(label),
        style: ElevatedButton.styleFrom(
          padding: const EdgeInsets.symmetric(
            horizontal: 24,
            vertical: 12,
          ),
        ),
      ),
    );
  }
}