# ==================================================================== #
#  File name:      __init__.py                  #        _.==._        #
#                  (lib_file_handling)          #     .+=##**##=+.     #
#  Author:         Arjan Lemmens                #    *= #        =*    #
#  Date:           20-Jun-2025                  #   #/  #         \#   #
# ============================================= #  |#   #   $      #|  #
#  Description:    This file controls which     #  |#   #   #      #|  #
#                  methods and definitions are  #   #\  #   #     /#   #
#                  passed to the higher level   #    *= #   #    =+    #
#                  files.                       #     *++######++*     #
#                  This lib handles file        #        *-==-*        #
#                  handling and everything and  # ==================== #
#                  everything related to that.                         #
#  Rev:            1.0                                                 #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  20-Jun-2025 Initial release                                         #
# ==================================================================== #

from lib_file_handling._file_handler import (
    get_file_name,
    get_folder_name,
    get_last_file,
    get_previous_date,
    open_file,
    get_all_files,
)
