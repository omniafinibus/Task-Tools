from lib_todo._daily import daily_todos
from lib_todo._local import local_todos
from definitions import ARGS

def update(args):
    type = args.__dict__[ARGS.TYPE]
    if type == ARGS.TYPE_LOCAL or type == ARGS.TYPE_LOCAL_SHORT:
        local_todos(args)
    elif type == ARGS.TYPE_DAILY or type == ARGS.TYPE_DAILY_SHORT:
        daily_todos(args)
    else:
        print(f"unknown type {type}")
        quit()