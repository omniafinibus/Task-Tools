# ==================================================================== #
#  File name:      _local.py                    #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This file handles the        #  |#   #   $      #|  #
#                  routine to manage and update #  |#   #   #      #|  #
#                  todo files, which contain    #   #\  #   #     /#   #
#                  their history within the     #    *= #   #    =+    #
#                  same file.                   #     *++######++*     #
#                                               #        *-==-*        #
#  Rev:            1.0                          # ==================== #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Implemented _remove_header, _get_update_content,        #
#              and local_todos.                                        #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
from definitions import TODO, ARGS, TODAY, get_arg
from lib_file_handling import get_all_files
from os.path import isfile, getmtime
from argparse import Namespace
import subprocess
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
    text = re.sub(TODO.RE_LOCAL_HEADER, "", text)

    # Remove description
    text = text.replace(TODO.DESCRIPTION, "")

    return text


def _get_update_content(args, file):
    """Get all tasks from a file in a sorted fashion

    :param args: Argument object containing command flags
    :type args: Namespace
    :param file: Directory to target file
    :type file: str
    """

    # Get contents
    with open(file, "r") as f:
        text = f.read()

    # Clear header before parsing
    text = _remove_header(text)

    lFinished = list()
    lPreviouslyFinished = list()

    # Generate time stamp of file based on last modified time
    import datetime

    modifiedTime = datetime.datetime.fromtimestamp(
        getmtime(file), tz=datetime.datetime.now().astimezone().tzinfo
    )
    dateString = f"{str(modifiedTime.day).zfill(2)}-{str(modifiedTime.month).zfill(2)}-{modifiedTime.year}"
    timeString = f"{str(modifiedTime.time().hour).zfill(2)}:{str(modifiedTime.time().minute).zfill(2)}:{str(modifiedTime.time().second).zfill(2)}"
    timeStamp = "{" + f"{dateString}|{timeString}" + "}"

    # Was the previous finished line a finished one
    lastLineFinished = False
    newText = TODO.LOCAL_HEADER + "\n"

    for line in text.splitlines(True):
        # Unfinished tasks
        if re.findall(TODO.RE_UNFINISHED, line):
            lastLineFinished = False
            newText += line

        # Previously finished lines
        elif re.findall(TODO.RE_OLD_FINISHED, line):
            lastLineFinished = True
            lPreviouslyFinished.append(line)

        # Finished tasks
        elif re.findall(TODO.RE_FINISHED, line) and not get_arg(args, ARGS.DELETE_OLD):
            lastLineFinished = True
            lFinished.append(timeStamp + " " + line)

        # Don't add blank lines
        elif re.sub(r"\s*", "", line) != "\n":
            if lastLineFinished:
                lFinished.append(timeStamp + " " + line)
            else:
                newText += line

    # Add all newly finished tasks
    newText += "".join(lFinished)

    # Add all old finished tasks
    newText += "".join(lPreviouslyFinished)

    return newText


def local_todos(args: Namespace):
    # Get the relevant arguments
    sourceDirectory = get_arg(args, ARGS.TARGET)
    editor = get_arg(args, ARGS.EDITOR)

    # Update file if a non-directory is entered
    if isfile(sourceDirectory):
        if re.findall(r".*[a-zA-z0-9_]*\.todo", sourceDirectory):
            newText = _get_update_content(args, sourceDirectory)
            with open(sourceDirectory, "w") as f:
                f.write(newText)
                command = f'{editor} "{sourceDirectory}"'
                subprocess.run(command, shell=True)
                print("Done!")
                quit()
        else:
            print(f"Not a todo file: {sourceDirectory}")
        return

    # Get all to do files in the specified directory
    lFiles = get_all_files(
        sourceDirectory, r".*[a-zA-z0-9_]*\.todo", get_arg(args, ARGS.RECURSIVE)
    )

    # Parse each found file
    for file in lFiles:
        newText = _get_update_content(args, file)
        with open(file, "w") as f:
            f.write(newText)
            command = f'{editor} "{file}"'
            subprocess.run(command, shell=True)

    print("Done!")
    quit()
