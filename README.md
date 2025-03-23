# 🌟 Inspiration

One of life's challenges is making wise choices, such as finding the best deals on products. This has become even more important as the impact of rising tariffs has been felt—not just in the news but also in the cost of groceries. We realized there’s no quick way to know if the products we buy are affected by U.S.-Canada trade tariffs. We wanted to build something simple, smart, and empowering — a tool that supports local businesses and helps people make better choices at the shelf.
<br/><br/>


# 📱 What it does

**MapleLens** lets users:

- Take a picture of a product using their phone camera or upload a picture
- *(Beta)* Suggest Canadian or tariff-free alternatives
- Process everything through a custom backend using image recognition
<br/><br/>


# 🛠 How we built it

- **Frontend**: Built in Flutter, we created a responsive mobile UI with a camera-powered homepage. Users can capture and upload images directly from the app.
- **Backend**: Hosted on Vercel, it processes image uploads and runs classification logic to detect U.S. products.
- **Camera Integration**: Used Flutter’s `image_picker` package to access live camera preview and capture functionality.
- **Networking**: Used the `http` package to handle photo uploads and receive results from the backend API.
- **Text Recognition (OCR)**: Integrated **Google Vision API** to extract product names and details directly from images.
- **Product Matching**: Used **RapidFuzz** for fuzzy string matching, allowing better identification of Canadian alternatives.
<br/><br/>


# 🚧 Challenges we ran into (and how we overcame them)

### 1️⃣ Deciding the logic behind matching products to Canadian alternatives  
*How we overcame it:* The Google Cloud Vision API returns a string of product features. Since a category of products (chips, drinks, etc.) has certain features (potatoes, bottle), we matched each product to a category so all we have to display are the alternatives associated with a category.

### 2️⃣ Getting the camera plugin to work on emulators (it kept showing a placeholder animation)  
*How we overcame it:* We had to update the `pubspec.yaml` 🤦‍♂️  

### 3️⃣ Handling a range of image sizes  
*How we overcame it:* We kept receiving error `413` when testing. The issue was that some images were too big. We resolved this through the Flutter package `flutter_image_compress`.
<br/><br/>


# 🏆 Accomplishments that we're proud of

- Successfully built a working end-to-end **photo → backend → result** pipeline
- Delivered a polished and intuitive **user interface** in Flutter
- Collaborated quickly under pressure and kept things **clean, simple, and usable**
- Tackled a **real-world, timely issue** that could genuinely help people make informed buying decisions
<br/><br/>


# 🧠 What we learned

- How to **capture and upload images** using Flutter's `image_picker` + `http` stack
- How to **integrate a Dart frontend with a Python backend**
- Best practices in **structuring a multi-developer Flutter project**
- The importance of **debugging emulator quirks** and adapting fast
- **Sleep is important** 😴
<br/><br/>


# 🚀 What's next for MapleLens

- Add **OCR** to extract product names directly from the label
- Show **side-by-side Canadian alternatives** pulled from public sources
- Implement **sign-up feature for local vendors** to display their own products
- Add **barcode scanning**
- Expand support to include **other countries’ import statuses**
- Publish to the **Google Play Store** and **TestFlight** for real-world testing
