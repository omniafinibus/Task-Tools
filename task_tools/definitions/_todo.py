import datetime
from _general import DATE_STRING, TIME_STRING

TO_DO_FLAG = "[ ]"
IMPORTANT_FLAG = "[!]"
COMPLETED_FLAG = "[x]"
IN_PROGRESS_FLAG = "[o]"
FAILED_FLAG = "[-]"
INFO_FLAG = "#"

DESCRIPTION = f"\
\t{INFO_FLAG} = Info\n\
\t{TO_DO_FLAG} = To do\n\
\t{IMPORTANT_FLAG} = Important\n\
\t{COMPLETED_FLAG} = Completed\n\
\t{IN_PROGRESS_FLAG} = In progress\n\
\t{FAILED_FLAG} = Failed\n\n"

RE_MOVE = r"^\s*\[[ |\!]\]"  # To do or important
RE_COPY = r"^\s*\[o\]|^\s*#"  # In progress or comments
RE_KEEP = r"^\s*[[\w\W]|\[[x|X|\-]\]]" # Completed, failed or any other
RE_DAILY_HEADER = r'Daily notes:\s*[0-9]*-[0-9]*-[0-9]*\s*@\s*[0-9]*:[0-9]*:[0-9]*\s*\n'
RE_LOCAL_HEADER = r'Last update:\s*[0-9]*-[0-9]*-[0-9]*\s*@\s*[0-9]*:[0-9]*:[0-9]*\s*\n'

DAILY_HEADER = f"Daily notes: {DATE_STRING} @ {TIME_STRING}\n"

LOCAL_HEADER = f"Last update: {DATE_STRING} @ {TIME_STRING}\n"

TIME_STAMP = f"{DATE_STRING}|{TIME_STRING}"
