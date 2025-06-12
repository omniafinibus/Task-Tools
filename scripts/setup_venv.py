#!/usr/bin/env /home/arjan/Nextcloud/Programming/Python/project_tools/project_tools_venv/bin/python3
import os
from ._directory import BASE_DIRECTORY

VENV_NAME = ".venv"
VENV_PY = os.path.join(BASE_DIRECTORY, VENV_NAME, "Scripts", "python.exe")
lProjDirs = [
    # os.path.join(BASE_DIRECTORY, "local_library"),
]

def prepare_environments():
    os.chdir(BASE_DIRECTORY)
    os.system(f"python -m venv {VENV_NAME}")
    os.system(f"python -m pip install pyinstaller")
    os.system(f"python -m pip install pip-upgrader")
    os.system(f"python -m pip install pipreqs")
    os.system(f"{VENV_PY} -m pip install {dir}")
    os.system(f"{VENV_PY} -m pip install pyinstaller")
    os.system(f"{VENV_PY} -m pip install pip-upgrader")
    os.system(f"{VENV_PY} -m pip install pipreqs")

def create_requirements(overwrite=False):
    # Prepare requirement files (Pillow packages is added twice too tkinter_tools, db_maintainer, and job_generator)
    # Some requirements could still be missing
    for dir in lProjDirs:
        if overwrite: os.system(f"pipreqs --force {dir}")
        else:         os.system(f"pipreqs {dir}")

def install_custom_modules():
    # Install job_gen_db, script_generator, and tkinter_tools
    for dir in lProjDirs[:3]:
        os.system(f"py -m pip install {dir}")
        os.system(f"{VENV_PY} -m pip install {dir}")

def install_requirements():
    # Install requirements
    for req in [os.path.join(dir, "requirements.txt") for dir in lProjDirs]:
        os.system(f"pip-upgrade --skip-virtualenv-check {req}")
        os.system(f"pip-upgrade --skip-virtualenv-check {req}")
        os.system(f"python -m pip install -r {req}")
        os.system(f"{VENV_PY} -m pip install -r {req}")
    
prepare_environments()
create_requirements()
install_requirements()
install_custom_modules()