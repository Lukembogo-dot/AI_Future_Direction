import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.set_page_config(page_title="Recyclable Classifier", layout="centered")
st.title("♻️ Recyclable Item Classifier (Edge AI Prototype)")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPG or PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path="recyclable_classifier.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Preprocess image: resize, normalize, expand dims
    resized_img = image.resize((160, 160))
    img_array = np.array(resized_img) / 255.0
    img_array = np.expand_dims(img_array.astype(np.float32), axis=0)

    # Inference
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    # Define class names (simulate for now)
    class_names = ['Paper', 'Rock', 'Scissors']  # Adjust as per your dataset
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Predicted Class: **{predicted_class}**")
else:
    st.info("👈 Please upload an image to classify.")
