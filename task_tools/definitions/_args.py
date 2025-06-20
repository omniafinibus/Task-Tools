TARGET = "target"
TARGET_SHORT = "tg"
UPDATE = "update"
EDITOR_SHORT = "e"
EDITOR = "editor"
TYPE_SHORT = "t"
TYPE = "type"
DELETE_OLD_SHORT = "do"
DELETE_OLD = "deleteold"
TYPE_LOCAL_SHORT = "l"
TYPE_LOCAL = "local"
TYPE_DAILY_SHORT = "d"
TYPE_DAILY = "daily"
RECURSIVE_SHORT = "r"
RECURSIVE = "recursive"

def short_flag(flag):
    return f"-{flag}"

def long_flag(flag):
    return f"--{flag}"