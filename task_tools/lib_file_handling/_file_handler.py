import datetime
import subprocess
from os.path import join, isfile

DATE = datetime.datetime.now()


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