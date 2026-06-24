## Setup Instructions

This project requires **Python 3.11** and uses a virtual environment to manage dependencies like NumPy, OpenCV, and MediaPipe.

### 1. Create the Virtual Environment
Navigate to your project root directory and create a virtual environment named `.venv` using Python 3.11:

* **Windows:**
  ```bash
  py -3.11 -m venv .venv
  ```
* **macOS / Linux:**
  ```bash
  python3.11 -m venv .venv
  ```

### 2. Activate the Virtual Environment
Activate the environment before installing packages to ensure they remain isolated within this project:

* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```
*Note: Once activated, your terminal prompt will show `(.venv)` at the beginning of the line.*

### 3. Install Dependencies
Upgrade `pip` and install the required packages using the following command:

```bash
python -m pip install --upgrade pip && pip install numpy opencv-python mediapipe
```

### 4. Verify Installation
Ensure that the virtual environment is running Python 3.11 and that all libraries have been imported successfully:

```bash
python --version
python -c "import numpy as np, cv2, mediapipe as mp; print(f'NumPy: {np.__version__}\nOpenCV: {cv2.__version__}\nMediaPipe: {mp.__version__}')"
```
