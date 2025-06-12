#!/usr/bin/env /home/arjan/Nextcloud/Programming/Python/project_tools/project_tools_venv/bin/python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir",     help="Directory of where the project is located", type=str)
parser.add_argument("-v", "--version", help="New version number", type=str)
parser.add_argument("-n", "--name",    help="Name of project directory in project", type=str, default="")
args = parser.parse_args()

def update_line(file, oldLineContains, newLine):
    if os.path.exists(file):
        replacement = ""
        with open(file, "r") as f:
            lines = f.readlines()
            print(f"Altering file {file}")
            for line in lines:
                if line.find(oldLineContains) != -1:
                    print(f"Overwritting line {lines.index(line)}: \"{line}\"")
                    print(f"With: \"{newLine}\"")
                    replacement += newLine
                else:
                    replacement += line
        with open(file, "w") as f:
            f.write(replacement)
# docs /docs/sphinx/conf.py
update_line(
    file=os.path.join(args.dir, "docs", "sphinx", "source", "conf.py"), 
    oldLineContains="release = ",
    newLine=f"release = '{args.version}'\n"
    )
                
# pyproject.toml
update_line(
    file=os.path.join(args.dir, "pyproject.toml"), 
    oldLineContains="version = \"",
    newLine=f"version = \"{args.version}\"\n"
    )

# README.md
update_line(
    file=os.path.join(args.dir, "README.md"), 
    oldLineContains="version \"",
    newLine=f"version \"{args.version}\"\n"
    )