# ==================================================================== #
#  File name:      _file_handler.py             #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    Methods and definitions that #  |#   #   $      #|  #
#                  are related to file handling #  |#   #   #      #|  #
#                  , naming and mangement       #   #\  #   #     /#   #
#                                               #    *= #   #    =+    #
#                                               #     *++######++*     #
#  Rev:            1.0                          #        *-==-*        #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Initial release                                         #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
import datetime
import subprocess
from os import listdir
from os.path import join, isfile, isdir
import re

# =============== #
#   Definitions   #
# =============== #
DATE = datetime.datetime.now()


# =========== #
#   Methods   #
# =========== #
def get_all_files(directory: str, regex: str, recursive: bool):
    """Find all files in a directory for which the regular expression applies

    :param directory: Directory in which to search
    :type directory: str
    :param regex: Regular expression which needs to apply to the files found
    :type regex: str
    :param recursive: Seek in all directories located in the parent directory as well
    :type recursive: bool
    :return: List of all files found
    :rtype: list[str]
    """
    lFoundFiles = []

    # Return empty string if directory does not exist
    if not isdir(directory):
        return lFoundFiles

    # Run through each file
    for target in listdir(directory):
        target = join(directory, target)
        if isdir(target) and recursive:
            lFoundFiles.append(*get_all_files(target, regex, recursive))
        elif isfile(target) and re.findall(regex, target):
            lFoundFiles.append(target)

    # Make sure there is no empty directory added
    if "" in lFoundFiles:
        lFoundFiles.remove("")
    return lFoundFiles


def open_file(editor, file):
    """Open a file with a specific editor

    :param editor: Edite command, can include flags
    :type editor: str
    :param file: directory to file
    :type file: str
    """

    if not isfile(file):
        print(f"Cannot find file: {file}")

    command = f'{editor} "{file}"'
    subprocess.run(command, shell=True)


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


def get_last_file(targetPath):
    """Get the notes file which was most recently created[x]
    p.write(oldText)
    """
    # Find last created file
    dPrevDate = get_previous_date(DATE.day, DATE.month, DATE.year)
    previousFile = join(
        targetPath,
        get_folder_name(dPrevDate["month"], dPrevDate["year"]),
        get_file_name(**dPrevDate),
    )

    # Continue until a valid file is found or the year is not present anymore
    while all([not isfile(previousFile), dPrevDate["year"] >= 2023]):
        dPrevDate = get_previous_date(**dPrevDate)
        previousFile = join(
            targetPath,
            get_folder_name(dPrevDate["month"], dPrevDate["year"]),
            get_file_name(**dPrevDate),
        )

    return previousFile
