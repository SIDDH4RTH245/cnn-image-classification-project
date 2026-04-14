# 🧠 CNN Image Classification Project

## 📌 Overview
This project builds a **Convolutional Neural Network (CNN)** to classify images from the CIFAR-10 dataset.

It demonstrates how deep learning models can learn visual patterns and classify images into multiple categories.

---

## 🎯 Objective
- Load and preprocess image dataset
- Build a CNN model using TensorFlow/Keras
- Train the model on image data
- Evaluate performance using accuracy
- Deploy the model for real-time predictions

---

## 📊 Dataset
- Dataset: CIFAR-10
- Total Classes: 10
  - Airplane
  - Automobile
  - Bird
  - Cat
  - Deer
  - Dog
  - Frog
  - Horse
  - Ship
  - Truck

- Each image:
  - Size: 32x32 pixels
  - RGB format

---

## ⚙️ Project Workflow

### 1️⃣ Data Loading
- Loaded dataset using TensorFlow
- Split into training and testing sets

### 2️⃣ Data Preprocessing
- Normalized pixel values (0–255 → 0–1)

### 3️⃣ Model Building
- Convolutional Layers (Conv2D)
- Pooling Layers (MaxPooling)
- Fully Connected Layers (Dense)

### 4️⃣ Model Training
- Trained CNN on image dataset
- Optimizer: Adam
- Loss: Categorical Crossentropy

### 5️⃣ Model Evaluation
- Accuracy on test dataset
- Loss & accuracy visualization

### 6️⃣ Model Saving
- Saved trained model as `.h5` file

### 7️⃣ Deployment
- Built Streamlit app
- Upload image → Predict class

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Streamlit

---
