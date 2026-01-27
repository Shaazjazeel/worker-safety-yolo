<p align="center">
  <img src="assets/banner.jpeg" alt="Worker Safety Monitoring System Banner" width="100%" />
</p>
<div align="center">

  <h1>WORKER SAFETY MONITORING SYSTEM</h1>
  <h3>(worker-safety-yolo)</h3>
  
  <p>
    <b>Transform Safety Monitoring with AI-Driven Precision</b>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
    <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=for-the-badge&logo=yolo&logoColor=black" alt="YOLOv8" />
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
		<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  </p>

  <br />
</div>

---

## 📑 Table of Contents

| &nbsp; | Section | Description |
|:---:|:---|:---|
| 📖 | [**Overview**](#-overview) | _Project summary and core objectives_ |
| ✨ | [**Key Features**](#-key-features) | _Main capabilities of the system_ |
| 🛠️ | [**Tech Stack**](#-tech-stack) | _Tools and technologies used_ |
| 🏗️ | [**Project Architecture**](#-project-architecture) | _Flow of data and processing_ |
| 📂 | [**Project Structure**](#-project-structure) | _File organization tree_ |
| 🚀 | [**Installation**](#-installation) | _Setup guide and requirements_ |
| 💡 | [**Usage**](#-usage) | _How to run the application_ |
| 🧠 | [**Model & Classes**](#-model--detected-classes) | _Detected objects and alerts_ |

---

## 📖 Overview

**Worker Safety Monitoring System** is a cutting-edge AI application designed to enhance safety standards on construction sites. By leveraging the power of computer vision and deep learning, this system automatically analyzes video footage to detect Personal Protective Equipment (PPE) compliance in real-time.

Using a fine-tuned **YOLOv8** model, the system identifies workers, safety gear, and potential hazards. It provides immediate visual feedback, highlighting violations such as missing hardhats or safety vests with distinct alerts, ensuring a safer working environment.

---

## ✨ Key Features

* **🎥 Seamless Video Upload:** User-friendly web interface allows for easy uploading of recorded CCTV or site footage directly from the browser.
* **🤖 Advanced AI Inference:** Powered by **YOLOv8**, ensuring high-speed and accurate detection of safety elements.
* **🚨 Violation Alerts:** Automatically highlights safety violations (e.g., missing helmet) in **RED** and displays a blinking "VIOLATION DETECTED" warning.
* **✅ Intelligent Color Coding:** Compliant detections (wearing PPE) are shown in standard neutral colors, while violations stand out immediately.
* **📹 Recorded Video Support:** Optimized for processing pre-recorded videos, eliminating the need for live camera feeds during analysis.
* **🎨 Modern Premium UI:** A dark-themed, responsive interface built with HTML, CSS, and JS for a professional user experience.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Model** | ![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-blue) | Fine-tuned `best.pt` for object detection |
| **Backend** | ![Flask](https://img.shields.io/badge/Flask-Python-black) | Python web framework for handling requests |
| **Processing** | ![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green) | Video frame manipulation and drawing |
| **Frontend** | ![HTML/CSS/JS](https://img.shields.io/badge/Frontend-HTML_CSS_JS-orange) | Responsive and interactive user interface |

---

## 🏗️ Project Architecture

The system follows a streamlined pipeline to process video data:

1.  **Input:** User uploads a video file via the Flask web interface.
2.  **Preprocessing:** OpenCV reads the video frame-by-frame.
3.  **Inference:** Each frame is passed to the YOLOv8 model (`best.pt`).
4.  **Logic:** The system checks class IDs. If a "NO-Hardhat" or "NO-Mask" class is detected, a violation flag is raised.
5.  **Annotation:** Bounding boxes are drawn (Red for violations, Green/Blue for safe). Text alerts are overlaid.
6.  **Output:** Processed frames are streamed back to the user's browser.

---

## 📂 Project Structure

```bash
worker-safety-yolo/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── weights/
│   └── best.pt           # Fine-tuned YOLOv8 model
├── static/
│   ├── css/
│   │   └── style.css     # Modern styling
│   ├── js/
│   │   └── script.js     # Frontend logic
│   └── uploads/          # Temp folder for uploaded videos
├── templates/
│   └── index.html        # Main dashboard interface
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```
## 🚀 Installation

Follow these steps to set up the project locally:

### 1) Clone the Repository
```bash
git clone https://github.com/your-username/worker-safety-yolo.git
cd worker-safety-yolo
```
### 2) Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
### 3) Install Dependencies
```bash
pip install -r requirements.txt
```
### 4) Add Model Weights Ensure your fine-tuned model best.pt is placed inside the weights/ directory.
## 💡 Usage
### 1) Run the Application
```bash
python app.py
```
### 2) Access the Interface Open your web browser and navigate to: http://127.0.0.1:5000/

### 3) Analyze Video

Click the Upload button to select a construction site video.

Watch the processed video stream with real-time bounding boxes and violation alerts.

## 🧠 Model & Detected Classes
The model has been trained on the Construction Site Safety Dataset (Kaggle/Roboflow) and can detect the following classes:
| Class ID | Class Name | Status |
| :---: | :--- | :--- |
| 0 | **Person** | 🟢 Neutral |
| 1 | **Hardhat** | ✅ Safe |
| 2 | **NO-Hardhat** | 🔴 **VIOLATION** |
| 3 | **Mask** | ✅ Safe |
| 4 | **NO-Mask** | 🔴 **VIOLATION** |
| 5 | **Safety Vest** | ✅ Safe |
| 6 | **NO-Safety Vest** | 🔴 **VIOLATION** |
| 7 | **Machinery** | 🟡 Caution |
| 8 | **Vehicle** | 🟡 Caution |
| 9 | **Safety Cone** | 🔵 Info |

## 🔮 Future Improvements
[ ] Live Webcam Support: Enable real-time detection via RTSP or webcam feeds.

[ ] Email/SMS Notifications: Send automated alerts to supervisors when violations are detected.

[ ] Database Integration: Log violations with timestamps and snapshots for reporting.

[ ] Mobile App: Develop a companion mobile application for on-site monitoring.

[ ] Dashboard Analytics: Add graphs and charts to visualize safety trends over time.

## 
<div align="center">
  <p>Designed & Developed by <b>Shaaz Jazeel</b></p>
  <p>
    <a href="https://github.com/Shaazjazeel">
      <img src="https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github" alt="GitHub" />
    </a>
  </p>
</div>
