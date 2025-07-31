import os
import subprocess
from _directory import BASE_DIRECTORY, PROJECT_NAME, VENV_DIRECTORY

def check_file(dir):
    if os.path.isfile(dir) or os.path.isdir(dir):
        return
    print(f"Path not found: {dir}")
    exit()

PATH = os.path.join(BASE_DIRECTORY, "bin")
print(f"Preparing EXE in {PATH}, please wait...")
# os.chdir(os.path.join(BASE_DIRECTORY, "scripts"))

NAME = "Task-Tools"
OPTIONS = "--onefile --clean"
MAIN_FILE = f"{BASE_DIRECTORY}/{PROJECT_NAME}/__main__.py"
check_file(MAIN_FILE)
BIN_DIR = os.path.join(BASE_DIRECTORY, "bin")
check_file(BIN_DIR)
BUILD_DIR = os.path.join(BASE_DIRECTORY, "bin", "build")
check_file(BUILD_DIR)
OUTPUT_DIR = f"--distpath {BIN_DIR} --workpath {BUILD_DIR} --specpath {BIN_DIR}"
DIR_PYINSTALLER = os.path.join(VENV_DIRECTORY, "bin", "pyinstaller")
check_file(DIR_PYINSTALLER)
LOG_DIR = os.path.join(BASE_DIRECTORY, "bin", "logfile.txt")
check_file(LOG_DIR)

with open(LOG_DIR, 'w+') as logFile:
    command = f"\"{DIR_PYINSTALLER}\" {MAIN_FILE} --name \"{NAME}\" {OPTIONS} {OUTPUT_DIR}"
    results = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    logFile.write(results.stdout)
    
print("Done!")

# pyinstaller task_tools/__main__.py --workpath build/ --specpath bin --name Task-Tools