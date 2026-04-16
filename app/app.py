import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

import os
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'cnn_model.h5')
model = tf.keras.models.load_model(model_path)

class_names = [
    "airplane","automobile","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

st.title("🖼️ Image Classification App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB').resize((32, 32))
    
    st.image(img, caption="Uploaded Image", width=300)

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Prediction: {predicted_class}")