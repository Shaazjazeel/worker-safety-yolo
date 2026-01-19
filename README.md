# 🛡️ Worker Safety Monitoring System (YOLOv8)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Video%20Processing-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A smart AI-powered system that detects **PPE compliance** and **safety violations** from construction site videos using **YOLOv8**.

---

## ✨ Overview

Construction sites face accidents due to missing PPE like:
- ❌ No Helmet (Hardhat)
- ❌ No Mask
- ❌ No Safety Vest

This project helps by analyzing uploaded videos and automatically detecting:
✅ Workers  
✅ PPE equipment  
⚠️ Safety violations (highlighted in **red** + warning alert)

---

## 🎯 Features

- 📤 Upload construction site video
- 🎥 Frame-by-frame safety analysis
- 🔴 Violation detection highlighted in **RED**
- ⚡ Blinking **“VIOLATION DETECTED”** alert on output
- 🌐 Modern web interface (Flask + HTML/CSS)
- 📌 Works on recorded videos (no real-time CCTV required)

---

## 🧠 Model & Classes

This system uses a fine-tuned **YOLOv8** model (`best.pt`) trained on a construction safety dataset.

### ✅ Detected Classes
- Person  
- Hardhat / NO-Hardhat  
- Mask / NO-Mask  
- Safety Vest / NO-Safety Vest  
- Machinery, Vehicle, Safety Cone

---

## 🏗️ Project Architecture

