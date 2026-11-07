# wine-quality-MLOps-project

- Created "wine-quality-MLOps-project" repository on GitHub
- Open work directory folder on the local computer
- Right click and select "Open in Terminal"
- Clone the Git repo with 
```
git clone https://github.com/rahmanmohsinur/wine-quality-MLOps-project.git
```
- Then run the following in cmd to open folder in VS Code
```
code .
```
- To activate Conda inside of the VS Code for the first time, open Anaconda Prompt and the following inside the Anaconda Prompt (Skip if already activated):
```
conda init cmd.exe
```
- Created virtual environment for ML project using Conda inside of VS Code
```
conda create -p venv python==3.11 -y
```
- Activated environment by running the code
``` conda activate venv/
```
- Create "template.py" for project structure and run:
```python template.py
```
- To install project and dependencies edit "requirements.txt" and run the following code in cmd:
```
pip install -r requirements.txt
```