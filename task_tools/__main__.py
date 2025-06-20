from definitions import ARGS
from lib_todo import update
import argparse

mainParser = argparse.ArgumentParser()
# To Do handling
subParser = mainParser.add_subparsers(dest="command", help="Update a todo file")
subParser.required = True
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
    help="Delete old tasks, in daily  mode this deletes the latest file only containing completed tasks.",
)

args = mainParser.parse_args()
args.func(args)