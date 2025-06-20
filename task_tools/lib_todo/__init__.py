# ==================================================================== #
#  File name:      __init__.py (lib_todo)       #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This file controls which     #  |#   #   $      #|  #
#                  methods and definitions are  #  |#   #   #      #|  #
#                  passed to the higher level   #   #\  #   #     /#   #
#                  files.                       #    *= #   #    =+    #
#                  This lib handles to do files #     *++######++*     #
#                  and everything related to    #        *-==-*        #
#                  them.                        # ==================== #
#  Rev:            1.0                                                 #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Initial release                                         #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
from lib_todo._daily import daily_todos
from lib_todo._local import local_todos
from definitions import ARGS, get_arg


# =========== #
#   Methods   #
# =========== #
def update(args):
    """Select method based on update type

    :param args: arguments flags passed into program upon call
    :type args: Namespace
    """
    print("running update")
    type = get_arg(args, ARGS.TYPE)
    if type in [ARGS.TYPE_LOCAL, ARGS.TYPE_LOCAL_SHORT]:
        local_todos(args)
    elif type in [ARGS.TYPE_DAILY, ARGS.TYPE_DAILY_SHORT]:
        daily_todos(args)
    else:
        print(f"unknown type {type}")
        quit()
