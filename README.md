
# MNIST Digit Predictor Web App

This is a Flask-based web application that allows users to upload handwritten digit images (28x28 grayscale) and predicts the digit using a pre-trained ONNX model. It also displays the confidence scores for each digit class using a bar chart.

---

## Features

The web application allows users to upload their own digit images for prediction, offering a preview of the selected image before the prediction is processed. It displays the predicted digit along with a probability distribution visualized using Chart.js. Users can also test the model using built-in sample MNIST digit images for convenience. Additionally, the app includes error handling mechanisms to manage invalid or missing file uploads, ensuring a smooth user experience.

---

## Tech Stack

- **Flask (Python)** for backend web server
- **onnxruntime** for model inference
- **HTML + CSS + JavaScript** for the frontend
- **Chart.js** for visualizing prediction confidence

---

## Project Structure

```
mnist_flask/
├── app.py               # Flask backend with ONNX prediction and routing
├── mnist_cnn.onnx       # Pre-trained ONNX model
├── environment.yml      # Conda environment file with all required dependencies
├── static/
│   └── samples/         # Sample digit images (0.png to 9.png)
├── templates/
│   └── index.html       # HTML frontend with upload form and sample image display
├── README.md            # This file

```

---

## How to Run the App

1. **Clone the repository** or download the project folder.

2. **Create and activate the conda environment** using the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   conda activate mnist_flask
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to:  
   ```
   http://127.0.0.1:5000/
   ```

   ```

---

## 🛠 Error Handling

If the uploaded file is not an image, it cannot be selected due to input restrictions. Additionally, if the predict button is clicked without selecting a file, an error popup will appear prompting the user to upload an image first.

---

## 📷 Sample Images

- The web page includes clickable sample MNIST digits (0–9) that users can test without uploading their own images.

---
