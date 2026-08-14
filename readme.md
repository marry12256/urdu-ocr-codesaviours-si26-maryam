1. What is OCR (Optical Character Recognition)?
OCR (Optical Character Recognition) is a technology that converts text from images, scanned documents, or photos into editable and searchable digital text. It helps computers recognize printed or handwritten characters automatically. OCR saves time because people do not have to type the text manually.
2. Why is Urdu OCR harder than English OCR?
Urdu OCR is more difficult than English OCR because Urdu is written from right to left and its letters change shape depending on their position in a word. Many Urdu letters look very similar and are distinguished only by dots, making them harder for computers to recognize accurately. In addition, connected writing styles and different fonts increase the complexity of Urdu OCR.
3. What are 2 real-world situations where Urdu OCR would be useful?
One useful application of Urdu OCR is digitizing old Urdu books, newspapers, and historical documents so they can be searched and preserved electronically. Another application is extracting text from printed forms, bills, or government documents, allowing organizations to store and process information more efficiently. These uses reduce manual data entry, save time, and improve access to Urdu-language information.

WHY WE NEED A BETTER MODEL?
## Gap Analysis
### Image 1: sign3.jpg.jpeg

**Actual Urdu Text:**

آگے پٹرول پمپ ہے۔

**Tesseract Output:**
 ٹا
ہس تی ۴سط ہرد سور ری


**What went wrong?**

Tesseract incorrectly recognized the Urdu text. Most words were wrong and the output did not match the original sentence.

### Image 2: book1.jpg.jpeg

**Actual Urdu Text:**

شاعری ادب کی اعلیٰ ترین صنف ہے۔

**Tesseract Output:**

No text detected.

**What went wrong?**

Tesseract failed to detect the Urdu text and returned a blank output.

### Image 3: news1.jpg.jpeg

**Actual Urdu Text:**

غیر ملکی خبر رساں ادارے اے ایف پی کی رپورٹ کے

**Tesseract Output:**

غیرملکی خبررساں ادارے اے ایف پی کی رپورٹ کے

**What went wrong?**

Tesseract recognized most of the sentence but merged some words together and spacing was incorrect.

### Image 4: news11.jpg.jpeg

**Actual Urdu text**

کراچی (نیوز ڈیسک) پاکستان نے اپنی سب سے بڑی فعال چینی

**Tesseract Output:**

9:6

**What went wrong?**

Tesseract detected only a few incorrect characters and failed to recognize the Urdu sentence.

### Image 5: news10.jpg.jpeg

**Actual Urdu Text:**

سرپرستی میں منعقدہ ایک ثقافتی تقریب کے دوران

**Tesseract Output:**

وپ اہ اک ار ری کے لوان

**What went wrong?**

Tesseract recognized only a few incorrect words and missed most of the original text.

# **Summary**

Tesseract fails on Urdu because Urdu is a cursive script with connected characters and complex shapes. The default Tesseract OCR model could recognize only some parts of the text, while many words were incorrect, missing, or not detected. Therefore, a better OCR model trained specifically for Urdu is needed for accurate text recognition.



## Urdu OCR — Code Saviours SI-26

**A fine-tuned TrOCR model for extracting Urdu text from images.**

## 1. What Problem This Solves and Why It Matters

OCR (Optical Character Recognition) is used to convert text from images into editable text.

Urdu OCR is challenging because Urdu is a connected script and the shape of letters can change when they are joined together. Different fonts, image quality, backgrounds, and text sizes can also make Urdu text difficult for an OCR model to recognize.

This project focuses on recognizing Urdu text from images.

One real-world use case is **digitizing Urdu books and newspapers**. Instead of typing the text manually, an OCR system can extract the text from images and make it easier to store, edit, and search.

## 2. How It Works

This project uses **TrOCR (Transformer-based Optical Character Recognition)** to recognize Urdu text from images.

The basic process is:

**Urdu Image → TrOCR Model → Extracted Urdu Text**

First, we collected Urdu images and created text labels for them. The final dataset contained **200 images**.

We then used these image-text pairs to train/fine-tune the OCR model. **Fine-tuning** means training an already existing model on our own dataset so that it can learn from our specific type of data, in this case Urdu text images.

After training, the model was connected to a web application. The user uploads an Urdu image, and the application gives the text predicted by the model.

## 3. Live Demo

The trained Urdu OCR model is deployed as a **Streamlit web application**.

**[Open Live Urdu OCR App](https://marry12256-urdu-ocr-codesaviours-si26-maryam-app-oioulg.streamlit.app/)**

## 4. How to Run It Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/marry12256/urdu-ocr-codesaviours-si26-maryam.git
```

### Step 2: Open the Project Folder

```bash
cd urdu-ocr-codesaviours-si26-maryam
```

### Step 3: Install the Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the App

```bash
streamlit run app.py
```

The Streamlit application will then open in your browser.

## 5. Dataset Details

The final dataset contains **200 Urdu images**.

The dataset was prepared during the internship by collecting Urdu text images and creating labels for them.

The images were collected from different sources, including **newspapers, books, and other Urdu text images**.

We also prepared synthetic Urdu text images as part of the dataset work.

The dataset contains variation in the appearance of Urdu text, including different image sources, text styles, backgrounds, and sizes.

Each image was matched with its corresponding Urdu text label. We also checked the final image paths, and the final check showed **0 missing images**.

## 6. Results

The model was trained for **3 epochs**.

The training loss was:

| Epoch | Training Loss |
| ----- | ------------: |
| 1     |        4.5476 |
| 2     |        2.9887 |
| 3     |        2.7755 |

The training loss decreased from **4.5476 to 2.7755**.

The model accuracy from Week 4 was **0%**.

The low accuracy shows that the model still needs improvement. With more time, we would collect a larger Urdu dataset, add more variety in fonts and image types, improve preprocessing, and train the model for more epochs.

Even with the low accuracy, the project was successfully taken from dataset collection and labeling to model training and deployment as a live Streamlit application.

## 7. Credit

**Maryam**

Built during the **Code Saviours ML/AI Internship — Batch SI-26**.

