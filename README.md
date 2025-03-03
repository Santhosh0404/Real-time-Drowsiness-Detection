# 🚗 Real-time Drowsiness Detection

A **computer vision-based** real-time drowsiness detection system that detects driver fatigue by monitoring **eye aspect ratio (EAR)** and triggers an **alarm** if drowsiness is detected.

![Drowsiness Detection Demo](https://your-image-link.com) *(Optional: Add a demo image!)*

---

## 📌 Table of Contents
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Project Status](#project-status)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## 🚀 Introduction
Drowsiness while driving is a significant cause of road accidents. This project uses **OpenCV, dlib, and machine learning** to detect **eye closure duration** and determine drowsiness in real-time.

### 🔍 How It Works:
- Captures **video from a webcam**.
- Detects the **face and eye landmarks** using `shape_predictor_68_face_landmarks.dat`.
- Computes **Eye Aspect Ratio (EAR)** to monitor drowsiness.
- If the EAR drops **below a threshold for consecutive frames**, a **warning sound** is triggered.

---

## ✨ Features
✔️ **Real-time eye tracking** 📷  
✔️ **Drowsiness detection using EAR** 💤  
✔️ **Audio alert system** 🔊  
✔️ **Adjustable sensitivity (threshold & frame count)** 🎯  
✔️ **Works on most systems (Windows recommended due to `winsound`)** 💻  

---

## 🛠️ Technologies Used
- **Python** 🐍  
- **OpenCV** (for face & eye detection)  
- **dlib** (for facial landmark detection)  
- **imutils** (for image processing)  
- **scipy.spatial** (for computing EAR)  
- **winsound** (for generating alert sounds in Windows)  

---

## ⚙️ Installation
### **Step 1: Clone the Repository**
```sh
git clone https://github.com/Santhosh0404/Real-time-Drowsiness-Detection.git
cd Real-time-Drowsiness-Detection

Step 2: Install Dependencies
sh
Copy
Edit
pip install opencv-python dlib imutils scipy
Step 3: Download the Shape Predictor File
The model file shape_predictor_68_face_landmarks.dat is required.

If not included in the repo, Download Here.
Extract it and place it inside the code/ directory.
Step 4: Run the Program
sh
Copy
Edit
python main.py
(Ensure your webcam is connected!)

📌 Usage
Run the script using the above command.
Look at the camera and keep your eyes open.
If your eyes remain closed for too long, the system triggers a warning beep.
Note: Modify earThresh and earFrames in main.py to fine-tune sensitivity.

📊 Project Status
✅ Current Progress:

Implemented real-time eye tracking ✅
Integrated EAR-based drowsiness detection ✅
Added audio alerts using winsound ✅
Basic UI using OpenCV window ✅
🚧 Future Enhancements:

 Implement yaw detection (detect head tilts)
 Add a mobile app version
 Improve multi-platform support (Mac/Linux)
 Optimize performance for low-end devices
🤝 Contributing
Contributions are welcome! Follow these steps:

Fork the repo
Create a new branch (git checkout -b feature-name)
Commit changes (git commit -m "Added new feature")
Push to GitHub (git push origin feature-name)
Open a Pull Request
📜 License
This project is licensed under the MIT License.

📩 Contact
For any queries or suggestions, feel free to reach out:
📧 Email: santhoshkalpana098@gmail.com
🔗 GitHub: Santhosh0404
