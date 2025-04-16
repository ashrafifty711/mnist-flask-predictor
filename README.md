
# MNIST Digit Predictor Web App

This is a Flask-based web application that allows users to upload handwritten digit images (28x28 grayscale) and predicts the digit using a pre-trained ONNX model. It also displays the confidence scores for each digit class using a bar chart.

---

## 🚀 Features

- Upload custom digit images for prediction.
- Preview the uploaded image before submission.
- Display predicted digit and probability distribution using Chart.js.
- Select from example MNIST digit images for quick testing.
- Error handling for invalid or missing file uploads.

---

## 🧠 Tech Stack

- **Flask (Python)** for backend web server
- **onnxruntime** for model inference
- **HTML + CSS + JavaScript** for the frontend
- **Chart.js** for visualizing prediction confidence

---

## 📁 Project Structure

```
mnist_flask/
├── app.py               # Flask backend with ONNX prediction and routing
├── model/
│   └── mnist_model.onnx # Pre-trained ONNX model
├── static/
│   └── samples/         # Sample digit images (0.png to 9.png)
├── templates/
│   └── index.html       # HTML frontend with upload form and sample image display
├── README.md            # This file
```

---

## ⚙️ How to Run the App

1. **Clone the repository** (if applicable) or download the project folder.

2. **Create a conda environment** (optional but recommended):
   ```bash
   conda create -n mnist_flask python=3.9
   conda activate mnist_flask
   ```

3. **Install dependencies**:
   ```bash
   pip install flask onnxruntime numpy pillow
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open your browser** and go to:  
   ```
   http://127.0.0.1:5000/
   ```

---

## 🛠 Error Handling

- If the uploaded file is **not an image**, the app will show a browser alert and not submit the file.
- If **no file** is uploaded and the predict button is clicked, nothing will happen.

---

## 📷 Sample Images

- The web page includes clickable sample MNIST digits (0–9) that users can test without uploading their own images.

---

## 📞 Contact

For questions, feel free to reach out to **Md Ashraf Hossain Ifty**.

---
