🎮 Gesture-Controlled Tic-Tac-Toe using OpenCV & MediaPipe

A computer-vision-based Tic-Tac-Toe game controlled entirely using hand gestures.
This project demonstrates Human–Computer Interaction (HCI) using Python, OpenCV, and MediaPipe.

📌 Project Overview:

This application allows players to play Tic-Tac-Toe without a keyboard or mouse.
Players interact with the game using finger gestures detected via a webcam.

The system supports:

    Two-hand multiplayer

    Gesture-based menu

    Gesture-based reset

    Winning line animation

This project is suitable for:

    🎓 Final Year Project

    🤖 Computer Vision & AI demos

    🧠 Human-Computer Interaction (HCI) studies

    ✨ Features

    ✋ Two-Hand Multiplayer

    Left hand → Player X

    Right hand → Player O

    🖐️ Gesture-Based Menu

    Start game

    Reset game

    Exit using hand gestures

    👆 Touch-Free Gameplay

    Point index finger to select a cell

    Hover to confirm move

    🔄 Gesture-Based Reset

    Show open palm (5 fingers) to reset game

    🏆 Winning Line Animation

    Visual line drawn across winning combination

    🎯 Improved Accuracy

    Stable hover detection

    Reduced false gesture triggers

    Handedness-based player control

🛠️ Technologies Used
    Technology	Purpose
    Python	Core programming language
    OpenCV	Camera input & UI rendering
    MediaPipe	Hand & finger tracking
    NumPy	Mathematical operations
📂 Project Structure
Finger-Tic-Tac-Toe-OpenCV/
│
├── gesture_tictactoe.py
├── README.md
├── requirements.txt
└── screenshots/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/motesanchita16/Finger-Tic-Tac-Toe-OpenCV.git
cd Finger-Tic-Tac-Toe-OpenCV

2️⃣ Install Dependencies
pip install -r requirements.txt


requirements.txt

opencv-python
mediapipe
numpy

3️⃣ Run the Application
python gesture_tictactoe.py

🖐️ Gesture Controls
Gesture	Action
Index finger hover	Select cell
Open palm (5 fingers)	Reset / Open menu
Left hand	Player X
Right hand	Player O
🧠 System Workflow

Webcam captures real-time video

MediaPipe detects hand landmarks

Index finger position mapped to grid

Gesture confirmed via hover detection

Game logic checks win/draw

UI updates in real-time



🚀 Future Enhancements

AI opponent (Minimax)
Difficulty selection using gestures
Scoreboard & match history
Sound effects
Android / Web version
Multiplayer over network

🎓 Academic Relevance

Computer Vision
Human-Computer Interaction
Artificial Intelligence
Real-Time Systems
Perfect for final year projects, demos, and research.

👩‍💻 Author

Sanchita Nitin Mote
Second year student 
VIT PUNE'28 (AIDS)

GitHub:
👉 https://github.com/motesanchita16