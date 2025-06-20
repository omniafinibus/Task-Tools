# ==================================================================== #
#  File name:      _args.py                     #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This file contains all       #  |#   #   $      #|  #
#                  global definitions related   #  |#   #   #      #|  #
#                  to argument usage.           #   #\  #   #     /#   #
#  Rev:            1.0                          #    *= #   #    =+    #
# ============================================= #     *++######++*     #
#  Revision history:                            #        *-==-*        #
#  Date        Description                      # ==================== #
#  20-Jun-2025 Added flag definitions and short/long flag methods.     #
# ==================================================================== #

# =============== #
#   Definitions   #
# =============== #
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


# =========== #
#   Methods   #
# =========== #
def short_flag(flag):
    return f"-{flag}"


def long_flag(flag):
    return f"--{flag}"
