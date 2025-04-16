import numpy as np
import onnxruntime as ort
from flask import Flask, render_template, request, jsonify
from PIL import Image
import io


# Load the pre-trained model (make sure the model file is in your working directory)
session = ort.InferenceSession('mnist_cnn.onnx')

def predict(image: np.ndarray):
    """
    Predicts a digit from a 28x28 grayscale image.
    """

    # Normalize pixel values: convert 0-255 range to 0-1
    image = image.astype(np.float32) / 255.0
    # Reshape to fit model input (batch size 1, single channel)
    image = image.reshape(1, 1, 28, 28)
    
    # Get input name for the model
    input_name = session.get_inputs()[0].name
    # Run inference. Expecting outputs shape of [1, 10]
    outputs = session.run(None, {input_name: image})[0][0]
    probabilities = np.exp(outputs) / np.sum(np.exp(outputs))  # Retrieve the output vector for class probabilities
    # Predicted digit corresponds to the highest probability
    predicted_digit = np.argmax(probabilities)
    
    return predicted_digit, probabilities

app = Flask(__name__)

@app.route('/')
def index():
    # Render the homepage with the image upload form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Open the uploaded file as an image and convert to grayscale
        image = Image.open(file).convert('L')
    except Exception as e:
        return jsonify({'error': 'Uploaded file is not a valid image'}), 400
    
    # Ensure the image is 28x28 pixels; if not, resize it
    if image.size != (28, 28):
        image = image.resize((28, 28))
    
    # Convert the PIL image into a NumPy array
    image_np = np.array(image)
    
    # Perform prediction using the defined ONNX inference function
    digit, confidence = predict(image_np)
    
    # Construct a JSON result with the predicted digit and confidence scores
    result = {
        'predicted_digit': int(digit),
        'confidence': confidence.tolist()  # convert numpy array to list for JSON serialization
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
