import os
import subprocess
from ._directory import BASE_DIRECTORY, PROJECT_NAME, VENV_DIRECTORY

PATH = os.path.join(BASE_DIRECTORY, "bin")
print(f"Preparing EXE in {PATH}, please wait...")
os.chdir(os.path.join(BASE_DIRECTORY, "scripts"))

NAME = "Task Tools"
OPTIONS = "--onefile --clean"
ICON = "-i ../assets/logo.png"
MAIN_FILE = f"..\\{PROJECT_NAME}\\__main__.py"
OUTPUT_DIR = "--distpath ../bin/ --workpath ../bin/build --specpath ../bin/"
DIR_PYINSTALLER = os.path.join(VENV_DIRECTORY, "Scripts", "pyinstaller.exe")

with open(os.path.join(BASE_DIRECTORY, "bin", "logfile.txt"), 'w+') as logFile:
    results = subprocess.run(f"{DIR_PYINSTALLER} --name \"{NAME}\" {MAIN_FILE} {OPTIONS} {OUTPUT_DIR}", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    logFile.write(results.stdout)
    
print("Done!")