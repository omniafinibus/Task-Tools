import os
import subprocess
from _directory import *

PATH = os.path.join(MAIN_DIRECTORY, "bin")
print(f"Preparing EXE in {PATH}, please wait...")
os.chdir(os.path.join(MAIN_DIRECTORY, "scripts"))

NAME = "Program Name"
OPTIONS = "--onefile --clean --noconsole"
ICON = "-i ../assets/logo.png"
EXTRA_DATA = "--collect-data sv_ttk" # Required for embedded images
MAIN_FILE = f"..\{PROJECT_NAME}\__main__.py"
OUTPUT_DIR = "--distpath ../bin/ --workpath ../bin/build --specpath ../bin/"
SPLASH_SCREEN = "--splash ../assets/splash.png"
DIR_PYINSTALLER = os.path.join(VENV_DIRECTORY, "Scripts", "pyinstaller.exe")

with open(os.path.join(MAIN_DIRECTORY, "bin", "logfile.txt"), 'w+') as logFile:
    results = subprocess.run(f"{DIR_PYINSTALLER} --name \"{NAME}\" {MAIN_FILE} {OPTIONS} {ICON} {EXTRA_DATA} {OUTPUT_DIR}", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    logFile.write(results.stdout)
    
print("Done!")