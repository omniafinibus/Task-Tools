import datetime

TO_DO_FLAG = "[ ]"
IMPORTANT_FLAG = "[!]"
COMPLETED_FLAG = "[x]"
IN_PROGRESS_FLAG = "[o]"
FAILED_FLAG = "[-]"
INFO_FLAG = "#"

RE_MOVE = r"^\s*\[[ |\!]\]"  # To do or important
RE_COPY = r"^\s*\[o\]|^\s*#"  # In progress or comments
RE_KEEP = r"^\s*[[\w\W]|\[[x|X|\-]\]]" # Completed, failed or any other

RE_HEADER = r'Daily notes:\s*[0-9]*-[0-9]*-[0-9]*\s*@\s*[0-9]*:[0-9]*:[0-9]*\s*\n'
def todo_header():
    now = datetime.datetime.now()
    return f"Daily notes: {now.day}-{now.month}-{now.year} @ {now.time().hour}:{now.time().minute}:{now.time().second}\n"

DESCRIPTION = f"\
\t{INFO_FLAG} = Info\n\
\t{TO_DO_FLAG} = To do\n\
\t{IMPORTANT_FLAG} = Important\n\
\t{COMPLETED_FLAG} = Completed\n\
\t{IN_PROGRESS_FLAG} = In progress\n\
\t{FAILED_FLAG} = Failed\n\n"