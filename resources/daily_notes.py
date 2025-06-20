import os
import subprocess
from os.path import join, isdir, isfile
from lib_file_handling._file_handler import get_folder_name, get_file_name, get_last_file, DATE
from lib.todo_parser import parse_todo, create_new_todo
from lib_arguments import args

if args.nano:
    editor = "nano"
else:
    editor = "code"

# Target path handling
if not isdir(args.targetPath):
    print(f"Directory not found: {args.targetPath}")
    quit()
directory = join(args.targetPath, get_folder_name(DATE.month, DATE.year))
newFile = join(directory, get_file_name(DATE.day, DATE.month, DATE.year))
command = f'{editor} "{newFile}"'

# Create the directory of the current month if it doesn't exist
if not isdir(directory):
    os.makedirs(directory)

# If a file for today is already present, load that instead
if isfile(newFile):
    subprocess.run(command, shell=True)
    print("Done!")
    quit()

# Find the previous notes
lastFile = get_last_file()
undoneTasks = ""
oldText = ""

# If it's a file start reading it
if isfile(lastFile):
    undoneTasks = parse_todo(lastFile)

create_new_todo(newFile, undoneTasks)

subprocess.run(command, shell=True)

print("Done!")
