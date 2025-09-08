# Computer Vision for Biomechanical Analysis

This project uses Python, OpenCV, and MediaPipe for real-time biomechanical analysis, identifying human body landmarks via webcam and calculating elbow angles.

## Features
- Human pose detection using MediaPipe
- Calculation of left and right elbow angles
- Real-time visualization of landmarks, connections, and angles on the screen

## Requirements
- Python 3.10
- Webcam

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Pedr0bert/Visao-Computacional-para-Analise-Biomecanica.git
   cd Visao-Computacional-para-Analise-Biomecanica
   ```
2. Create a virtual environment (optional, but recommended):
   ```sh
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
   ```sh
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
