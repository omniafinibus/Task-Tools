import os
import re
import argparse
import datetime
import subprocess
from os.path import join, isdir, isfile


def str2bool(arg):
    """Convert an argument to a boolean

    :param arg: Argument to convert
    :type arg: bool or string
    :raises argparse.ArgumentTypeError: Error when value is not correct
    :return: Boolean value of original argument
    :rtype: bool
    """
    if isinstance(arg, bool):
        return arg
    if arg.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif arg.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def get_previous_date(day: int, month: int, year: int):
    """Get the previous DATE while taking the month and year into account

    :param day: Current day
    :type day: integer
    :param month: Current Month
    :type month: integer
    :param year: Current year
    :type year: integer
    :return: Dictionary the previous day, year, and month
    :rtype: dict{ "day": int, "month": int,  "year": int }
    """
    prevDay = day - 1 if day > 1 else 31
    prevMonth = month
    prevYear = year

    if day <= 1:
        prevMonth = month - 1 if month > 1 else 12

        if month <= 1:
            prevYear = year - 1

    return {"day": prevDay, "month": prevMonth, "year": prevYear}


def get_folder_name(month: int, year: int):
    """Definition of how month folders are name

    :param month: Month of the folder
    :type month: integer
    :param year: Year of the folder
    :type year: integer
    :return: Name of the folder
    :rtype: string
    """
    return f"{year}_{month}"


def get_file_name(day: int, month: int, year: int):
    """Definition of how a notes text file is named (ends in .txt)

    :param day: Day of the note
    :type day: integer
    :param month: Month of the note
    :type month: integer
    :param year: Year of the note
    :type year: integer
    :return: Name of the notes file
    :rtype: string
    """
    return f"{day}_{month}_{year}.todo"


def get_last_file():
    """Get the notes file which was most recently created[x]
    p.write(oldText)
    """
    # Find last created file
    dPrevDate = get_previous_date(DATE.day, DATE.month, DATE.year)
    previousFile = join(
        args.targetPath,
        get_folder_name(dPrevDate["month"], dPrevDate["year"]),
        get_file_name(**dPrevDate),
    )

    # Continue until a valid file is found or the year is not present anymore
    while all([not isfile(previousFile), dPrevDate["year"] >= 2023]):
        dPrevDate = get_previous_date(**dPrevDate)
        previousFile = join(
            args.targetPath,
            get_folder_name(dPrevDate["month"], dPrevDate["year"]),
            get_file_name(**dPrevDate),
        )

    return previousFile


TO_DO_FLAG = "[ ]"
COMPLETED_FLAG = "[x]"
IN_PROGRESS_FLAG = "[o]"
FAILED_FLAG = "[-]"
IMPORTANT_FLAG = "[!]"
INFO_FLAG = "#"
DATE = datetime.datetime.now()
PARSER = argparse.ArgumentParser()

# Flags for the command
PARSER.add_argument("targetPath", help="Defines base directory where notes are handled")
PARSER.add_argument(
    "-n ",
    "--nano",
    type=str2bool,
    nargs="?",
    const=True,
    default=False,
    help="Open the notes with nano",
)
PARSER.add_argument(
    "-c ",
    "--code",
    type=str2bool,
    nargs="?",
    const=True,
    default=True,
    help="Open the notes with VS code (default)",
)

# Read the flags
args = PARSER.parse_args()

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

# Create the directory of the current month if it doesn't exist
if not isdir(directory):
    os.makedirs(directory)

# If a file for today is already present, load that instead
if isfile(newFile):
    command = f'{editor} "{newFile}"'
    subprocess.run(command, shell=True)
    print("Done!")
    quit()

# Find the previous notes
lastFile = get_last_file()
undoneTasks = ""
oldText = ""

# If it's a file start reading it
if isfile(lastFile):
    # Move all undone tasks into the new file

    # Initialize the text of the old file, since it is going to be altered
    text = ""
    with open(lastFile, "r+") as p:
        text = p.read()

    infoIndex = text.find("\n\n")
    oldText += text[: infoIndex + 2]
    deleteOld = True

    # Find find all to do's, work in progress and infos
    for line in text.splitlines(True)[8:]:
        index = line.find(INFO_FLAG)
        if re.findall(r"^\s*\[[ |\!]\]", line):  # To do or important
            undoneTasks += line
        elif re.findall(r"^\s*\[o\]|^\s*#", line):  # In progress or comments
            undoneTasks += line
            oldText += line
            deleteOld = False
        elif re.findall(
            r"^\s*[[\w\W]|\[[x|X|\-]\]]", line
        ):  # Completed, failed or any other
            oldText += line
            deleteOld = False

    if not deleteOld:
        with open(lastFile, "w") as p:
            p.write(oldText)
    else:
        print(f"Removing file {lastFile}")
        os.remove(lastFile)

# Create a new file
with open(newFile, "w+") as notes:
    notes.write(
        f"Daily notes: {DATE.day}-{DATE.month}-{DATE.year} @ {DATE.time().hour}:{DATE.time().minute}:{DATE.time().second}\n\
\t{INFO_FLAG} = Info\n\
\t{TO_DO_FLAG} = To do\n\
\t{IMPORTANT_FLAG} = Important\n\
\t{COMPLETED_FLAG} = Completed\n\
\t{IN_PROGRESS_FLAG} = In progress\n\
\t{FAILED_FLAG} = Failed\n\n\
{undoneTasks}\
"
    )
command = f'{editor} "{newFile}"'
subprocess.run(command, shell=True)

print("Done!")
