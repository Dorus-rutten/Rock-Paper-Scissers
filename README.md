Welcome to **Rock-Paper-Scissors AI** – the hand gesture game powered by **OpenCV**, **MediaPipe**, and my own **AI**. Play against your computer with your hand gestures while the AI tries to predict your next move.

---

## 🌟 Features

- **Hand Gesture Recognition**: Play Rock, Paper, Scissors using your hands, thanks to MediaPipe's powerful hand tracking.
- **AI Opponent**: An AI that learns and predicts your next move.
- **OpenCV Integration**: Real-time video feed and gesture detection.
  
---

## 🖥️ Requirements

- **Python 3.9** (Required)
- **Camera** (To track your hand gestures)
  
---

## 🚀 Installation

To get started with **Rock-Paper-Scissors AI**, follow these steps:

### 1. Clone the Repository

Download the game from GitHub:

```bash
git clone https://github.com/dorus-rutten/Rock-Paper-Scissors
cd Rock-Paper-Scissors
```

### 2. Set Up a Python Environment

We recommend using Conda or venv for creating a dedicated Python environment.

Conda:
```bash
conda create -n rock-paper-scissors-env python=3.9
```
```bash
conda activate rock-paper-scissors-env
```

venv:
For macOS/Linux:
```bash
python3.9 -m venv rock-paper-scissors-env
source rock-paper-scissors-env/bin/activate
```
For Windows
```bash
python3.9 -m venv rock-paper-scissors-env
rock-paper-scissors-env\Scripts\activate
```
### 3. Install Dependencies

After setting up your environment, install the necessary libraries and dependencies:
```bash
python setup.py install
```
Alternatively, you can use pip:
```bash
pip install .
```

### 🎮 Running the Game
Once you have everything set up, you're all set to play! Simply run the game with:
```bash
python -m RPS
```

### 💬 Contributions
Contributions are always welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.


Enjoy the game! ✨✌️
