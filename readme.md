1. What is OCR (Optical Character Recognition)?
OCR (Optical Character Recognition) is a technology that converts text from images, scanned documents, or photos into editable and searchable digital text. It helps computers recognize printed or handwritten characters automatically. OCR saves time because people do not have to type the text manually.
2. Why is Urdu OCR harder than English OCR?
Urdu OCR is more difficult than English OCR because Urdu is written from right to left and its letters change shape depending on their position in a word. Many Urdu letters look very similar and are distinguished only by dots, making them harder for computers to recognize accurately. In addition, connected writing styles and different fonts increase the complexity of Urdu OCR.
3. What are 2 real-world situations where Urdu OCR would be useful?
One useful application of Urdu OCR is digitizing old Urdu books, newspapers, and historical documents so they can be searched and preserved electronically. Another application is extracting text from printed forms, bills, or government documents, allowing organizations to store and process information more efficiently. These uses reduce manual data entry, save time, and improve access to Urdu-language information.

## Why We Need a Better Model
Tesseract OCR is a general OCR tool that works well for many languages, but it struggles with Urdu text recognition. Urdu is a cursive script where characters are connected, have different shapes depending on their position in a word, and contain complex writing patterns.
The results from Tesseract show that many Urdu words were incorrectly recognized, missed completely, or returned with wrong spacing. Therefore, a specialized OCR model trained on Urdu datasets is needed to improve accuracy and correctly recognize Urdu text from newspapers, books, signboards, and other documents.
A better Urdu OCR model can handle complex character connections, different fonts, and real-world image conditions, resulting in more reliable text extraction.
# Gap Analysis
### Image 1: sign3.jpg.jpeg 

**Actual Urdu Text:**

آگے پٹرول پمپ ہے۔
**Tesseract Output:**

تا
پس تی عسط برد سور ری
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

Actual Urdu Text:
**bold text**
غیر ملکی خبر رساں ادارے اے ایف پی کی رپورٹ کے

**Tesseract Output:**

غیرملکی خبررساں ادارے اے ایف پی کی رپورٹ کے
**What went wrong?**

Tesseract recognized most of the sentence but merged some words together and spacing was incorrect.

### Image 4: news11.jpg.jpeg

**Actual Urdu Text:**

کراچی (نیوز ڈیسک) پاکستان نے اپنی سب سے بڑی فعال چینی
**Tesseract Output:**

9:6

**What went wrong?**

Tesseract detected only a few incorrect characters and failed to recognize the Urdu sentence.

### Image 5: news10.jpg.jpeg

**Actual Urdu Text:**

سرپرستی میں منعقدہ ایک ثقافتی تقریب کے دوران

**Tesseract Output:**

ویب اہ اک رے کے لوان

**What went wrong?**

Tesseract recognized only a few incorrect words and missed most of the original text.

# **Summary**
Tesseract fails on Urdu because Urdu is a cursive script with connected characters and complex shapes. The default Tesseract OCR model could recognize only some parts of the text, while many words were incorrect, missing, or not detected. Therefore, a better OCR model trained specifically for Urdu is needed for accurate text recognition.
