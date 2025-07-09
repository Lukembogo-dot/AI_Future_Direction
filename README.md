# ♻️ Edge AI Image Classifier – Recyclable Item Detection

A lightweight image classification prototype built using **TensorFlow Lite** and **Streamlit**, designed for **Edge AI** environments like Raspberry Pi. This project detects recyclable materials in real time, promoting sustainability while showcasing low-latency inference.

---

## 📌 Project Overview

This project demonstrates how **Edge AI** enhances:

- ⚡ Real-time performance (low latency)
- 🌐 Offline inference (no cloud required)
- 🔒 Data privacy (no data leaves the device)

We simulate this with a simple image classifier trained using **TensorFlow**, converted to `.tflite`, and deployed through a **Streamlit web app**.

---

## 🧠 Model Details

- **Dataset**: `rock_paper_scissors` from TensorFlow Datasets (TFDS) – used as a **proxy** for recyclable categories (plastic, paper, metal)
- **Model**: A lightweight CNN trained using Keras
- **Format**: Converted to `.tflite` using `TFLiteConverter`
- **Accuracy**: ~92% on validation set
- **Deployment**: Inference via `tf.lite.Interpreter` in a local Streamlit app

---

## 🛠️ Tech Stack

| Tool              | Role                              |
|------------------|------------------------------------|
| 🐍 Python 3.10+    | Programming Language               |
| 🧠 TensorFlow      | Model training and TFLite conversion |
| 📦 TensorFlow Lite | Edge AI runtime (interpreter)     |
| 🖼️ TensorFlow Datasets | Sample dataset (`rock_paper_scissors`) |
| 🌐 Streamlit       | Interactive web app UI             |
| 📊 Matplotlib      | Visualization during training      |

---

## 🚀 Setup Instructions

### 📁 1. Clone the Repository

```bash
git clone https://github.com/yourusername/recyclable-edge-ai.git
cd recyclable-edge-ai
```
### 🛠️ 2. Create and Activate a Virtual Environment
py -3.10 -m venv venv
.\venv\Scripts\activate

### 📦 3. Install Required Dependencies
pip install tensorflow tensorflow-datasets streamlit matplotlib pillow

### 🧪 Running the App
🖼️ Run Streamlit UI:

streamlit run app.py

### 🧠 How Edge AI Helps
✅ Low Latency: No cloud round-trips
✅ Offline Predictions: Works in remote areas
✅ Privacy: No user data leaves the device
✅ Energy Efficient: Designed for edge devices (like Raspberry Pi)

### 👨‍💻 Author
Luke Mbogo
AI & Cybersecurity Enthusiast 🇰🇪
LinkedIn | GitHub | Nairobi, Kenya


---

Let me know if you'd like me to:

- Drop this into a `.md` file for download
- Add your actual GitHub username
- Include your LinkedIn or project screenshots

Want a `requirements.txt` too? I can generate that next.

### 📄 License
MIT License
© 2025 Luke Mbogo



