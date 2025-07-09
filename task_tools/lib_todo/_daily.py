# ==================================================================== #
#  File name:      _daily.py                    #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This file handles the        #  |#   #   $      #|  #
#                  routine to manage and update #  |#   #   #      #|  #
#                  todo files, which contain    #   #\  #   #     /#   #
#                  their history a folder       #    *= #   #    =+    #
#                  structure in the target      #     *++######++*     #
#                  directory.                   #        *-==-*        #
#  Rev:            1.0                          # ==================== #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Rewrote original daily_task script into _remove_header, #
#              _parse_text, _contains_tasks, and daily_todos methods.  #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
from lib_file_handling import get_file_name, get_folder_name, get_last_file, open_file
from os.path import join, isdir, isfile
from definitions import TODO, ARGS, TODAY, get_arg
from argparse import Namespace
import subprocess
import sys
import os
import re


# =========== #
#   Methods   #
# =========== #
def _remove_header(text):
    """Remove the todo header from a text

    :param text: Text to remove the header from
    :type text: str
    :return: text without the header
    :rtype: str
    """
    # Remove the first line with the date/time
    text = re.sub(TODO.RE_DAILY_HEADER, "", text)

    # Remove description
    text = text.replace(TODO.DESCRIPTION, "")

    return text


def _parse_text(text):
    """Split the contents of text into the complete and in progress tasks and create the content for the new to do file containing all unfinished tasks

    :param text: text to parse
    :type text: str
    :return: oldText, undoneTasks
    :rtype: str, str
    """

    # Place holder for the todos which will be placed in the new to do file
    undoneTasks = ""

    # Keep the date and time saved in the updated todo file
    oldText = text.splitlines(True)[0] + "\n"

    # Clear header before parsing
    text = _remove_header(text)

    # Find find all to do's, work in progress and infos
    for line in text.splitlines(True):
        if re.findall(TODO.RE_MOVE, line):
            # Save the "move" task types to the new file
            undoneTasks += line
        elif re.findall(TODO.RE_COPY, line):
            # Keep the "copy" task types in the original location and the new file
            undoneTasks += line
            oldText += line
        elif re.findall(TODO.RE_KEEP, line):
            # Keep the "keep" task types in the original file
            oldText += line

    return oldText, undoneTasks


def _contains_tasks(text):
    """Check if a text contains tasks of any kind

    :param text: Text to check
    :type text: str
    :return: Boolean indicating the presence of tasks
    :rtype: bool
    """
    # Don't check the header
    text = _remove_header(text)

    # Look for any copy, keep or move tasks
    if any(
        [
            re.findall(TODO.RE_COPY, text),
            re.findall(TODO.RE_KEEP, text),
            re.findall(TODO.RE_MOVE, text),
        ]
    ):
        return True

    return False


def daily_todos(args: Namespace):
    """daily_todos Create a new to do file in a year/month/. folder

    :param args: arguments passed to this program
    :type args: Namespace
    """
    # Get the relevant arguments
    sourceDirectory = get_arg(args, ARGS.TARGET)
    editor = get_arg(args, ARGS.EDITOR)
    undoneTasks = ""

    # Check if the source directory exists
    if not isdir(sourceDirectory):
        print(f"Directory not found: {sourceDirectory}")
        sys.exit()

    # directory and file of new day
    monthDirectory = join(sourceDirectory, get_folder_name(TODAY.month, TODAY.year))
    newFile = join(monthDirectory, get_file_name(TODAY.day, TODAY.month, TODAY.year))

    # Create the month directory of the current month if it doesn't exist
    if not isdir(monthDirectory):
        os.makedirs(monthDirectory)

    # If a file for today is already present, load that instead
    if isfile(newFile):
        command = f'{editor} "{newFile}"'
        subprocess.run(command, shell=True)
        print("Done!")
        sys.exit()

    # Find the previous notes
    lastFile = get_last_file(sourceDirectory)

    # If it's a file start reading it
    if isfile(lastFile):
        # Move all undone tasks into the new file

        # Initialize the text of the old file, since it is going to be altered
        with open(lastFile, "r+") as p:
            oldText, undoneTasks = _parse_text(p.read())

        # Update the contents of the old file if there are any tasks left
        if _contains_tasks(oldText):
            with open(lastFile, "w") as p:
                p.write(oldText)
        else:  # Otherwise remove the file
            print(f"Removing file {lastFile}")
            os.remove(lastFile)

    # Create a new file
    with open(newFile, "w+") as notes:
        notes.write(f"{TODO.DAILY_HEADER}{TODO.DESCRIPTION}{undoneTasks}")

    open_file(editor, newFile)

    print("Done!")
