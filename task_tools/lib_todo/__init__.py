from lib_todo._daily import daily_todos
from lib_todo._local import local_todos
from definitions import ARGS, get_arg

def update(args):
    print("running update")
    type = get_arg(args, ARGS.TYPE)
    if type in [ARGS.TYPE_LOCAL, ARGS.TYPE_LOCAL_SHORT]:
        local_todos(args)
    elif type in [ARGS.TYPE_DAILY, ARGS.TYPE_DAILY_SHORT]:
        daily_todos(args)
    else:
        print(f"unknown type {type}")
        quit()