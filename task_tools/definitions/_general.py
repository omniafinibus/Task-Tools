# ==================================================================== #
#  File name:      _general.py                  #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           20-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    This file contains all       #  |#   #   $      #|  #
#                  global definitions related   #  |#   #   #      #|  #
#                  which are used by this       #   #\  #   #     /#   #
#                  project.                     #    *= #   #    =+    #
#  Rev:            1.0                          #     *++######++*     #
# ============================================= #        *-==-*        #
# Revision history:                             # ==================== #
# Date        Description                                              #
# 20-Jun-2025 Added time related definitions                           #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
import datetime

# =============== #
#   Definitions   #
# =============== #
TODAY = datetime.datetime.now()
DATE_STRING = f"{str(TODAY.day).zfill(2)}-{str(TODAY.month).zfill(2)}-{TODAY.year}"
TIME_STRING = f"{str(TODAY.time().hour).zfill(2)}:{str(TODAY.time().minute).zfill(2)}:{str(TODAY.time().second).zfill(2)}"
