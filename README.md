# Visao Computacional para Analise Biomecanica / Computer Vision for Biomechanical Analysis

This project uses Python, OpenCV, and MediaPipe for real-time biomechanical analysis, identifying human body landmarks via webcam or video and calculating elbow angles.

## Mediapipe
  Mediapipe is a framework for computer vision that can be used in embedded systems and mobile apliccations, such as android or IOS apps.
  It can be simply implemented using different types of programming languages like Python, C++, JavaScript and others mentioned in their website.

## Features
  This apliccation features humam pose detection and calculates angles of the left and right elbow angles. It is also capable of Real-time vizualization of landmarks, connections and showing numerical values of the respective angles.

## Requirements
- Python 3.10

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Pedr0bert/Visao-Computacional-para-Analise-Biomecanica.git
   cd Visao-Computacional-para-Analise-Biomecanica
   ```
2. Create a virtual environment (optional, but recommended):
   ```
   python -m venv venv
   # Activate the environment:
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## How to Use
1. Run the main script:
   ```
   python main.py
   ```
2. A window will open showing the webcam image with body landmarks and elbow angles.
3. Press `ESC` to exit.

## Project Structure
- `main.py`: Main biomechanical analysis code
- `requirements.txt`: List of dependencies
- `pyproject.toml`: Project configuration

## Notes
- Do not commit the `venv` folder or large files to the repository.
- Dependencies are installed automatically via `requirements.txt`.

## License
This project is for educational purposes only.
