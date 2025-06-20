# ==================================================================== #
#  File name:      __main__.py                  #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This programme provides a    #  |#   #   $      #|  #
#                  command tool which allows    #  |#   #   #      #|  #
#                  for management of todo files #   #\  #   #     /#   #
#                  and conversions of todo, ics #    *= #   #    =+    #
#                  and csv files to each other  #     *++######++*     #
#                  making it easier to plan out #        *-==-*        #
#                  and update project plans     # ==================== #
#  Rev:            2.0                                                 #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Added daily and local todo file management.             #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
from definitions import ARGS
from lib_todo import update
import argparse


# ================ #
#   Parser Setup   #
# ================ #
mainParser = argparse.ArgumentParser()
subParser = mainParser.add_subparsers(dest="command", help="Update a todo file")
subParser.required = True

# ================ #
#   To do parser   #
# ================ #
todoParser = subParser.add_parser(ARGS.UPDATE, add_help=False)
todoParser.set_defaults(func=update)
todoParser.add_argument(
    ARGS.long_flag(ARGS.TARGET), 
    ARGS.short_flag(ARGS.TARGET_SHORT), 
    nargs=1, 
    help="Base directory where notes are handled"
)
todoParser.add_argument(
    ARGS.long_flag(ARGS.EDITOR),
    ARGS.short_flag(ARGS.EDITOR_SHORT),
    nargs=1,
    default="vim",
    help="Text editor used to open files (supports flags)",
)
todoParser.add_argument(
    ARGS.long_flag(ARGS.TYPE),
    ARGS.short_flag(ARGS.TYPE_SHORT),
    nargs=1,
    default=ARGS.TYPE_LOCAL_SHORT,
    choices=[ARGS.TYPE_DAILY, ARGS.TYPE_DAILY_SHORT, ARGS.TYPE_LOCAL, ARGS.TYPE_LOCAL_SHORT],
    help="Type of to do files.\n\tl: local, where 1 file is used for both history and current todos.\n\td: daily, where each day has a new file, and the history is spread in monthly folders with daily files.",
)   
todoParser.add_argument(
    ARGS.long_flag(ARGS.DELETE_OLD),
    ARGS.short_flag(ARGS.DELETE_OLD_SHORT),
    action='store_true',
    help="Delete old tasks, in daily  mode this deletes the latest file only containing completed tasks.",
)
todoParser.add_argument(
    ARGS.long_flag(ARGS.RECURSIVE),
    ARGS.short_flag(ARGS.RECURSIVE_SHORT),
    action='store_true',
    help="Look for all .todo files in recursively, only works for local todo runs",
)

# ================== #
#   Execution code   #
# ================== #
args = mainParser.parse_args()
args.func(args)