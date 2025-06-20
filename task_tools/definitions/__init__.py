# ==================================================================== #
#  File name:      __init__.py                  #        _.==._        #
#                  (definitions)                #     .+=##**##=+.     #
#  Author:         Arjan Lemmens                #    *= #        =*    #
#  Date:           20-Jun-2025                  #   #/  #         \#   #
# ============================================= #  |#   #   $      #|  #
#  Description:    This file controls which     #  |#   #   #      #|  #
#                  methods and definitions are  #   #\  #   #     /#   #
#                  passed to the higher level   #    *= #   #    =+    #
#                  files.                       #     *++######++*     #
#                  This lib handles global      #        *-==-*        #
#                  definitions and methods      # ==================== #
#                  which are used throughout the whole project.        #
#  Rev:            1.0                                                 #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Initial release                                         #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
import definitions._args as ARGS
import definitions._todo as TODO
from definitions._general import TODAY


# =========== #
#   Methods   #
# =========== #
def get_arg(args, flag):
    if any(
        [
            isinstance(args.__dict__[flag], list),
            isinstance(args.__dict__[flag], tuple),
            isinstance(args.__dict__[flag], set),
            isinstance(args.__dict__[flag], dict),
        ]
    ):
        return args.__dict__[flag][0]
    else:
        return args.__dict__[flag]
