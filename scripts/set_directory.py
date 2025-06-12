# ==================================================================== #
#  File name:      set_directory.py             #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           12-Jun-2025                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    Script which creates the     #  |#   #   $      #|  #
#                  _directory file used to know #  |#   #   #      #|  #
#                  the relative directory of    #   #\  #   #     /#   #
#                  this project by other        #    *= #   #    =+    #
#                  scripts.                     #     *++######++*     #
#  Rev:            1.0                          #        *-==-*        #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  12-Jun-2025 File created                                            #
# ==================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                       #
#                                                                      #
# ==================================================================== #

import os
import re
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory where main is located")
args = parser.parse_args()


# Ask the user for the target directory
targetDir = ""

if not os.path.isdir(args.dir):
    incorrectDir = True
    print(f"No directory entered or incorrect \"{args.dir}\"")
    print("Enter the directory where the __main__.py is located: ")
    while(incorrectDir):
        dir = input()
        
        if not os.path.isdir(dir):
            print(f"\tEntered directory does not exist: {dir}\n\tPlease try again: ")
        else:
            targetDir = dir
            incorrectDir = False
else:
    targetDir = args.dir
    
projectName = os.path.basename(os.path.normpath(targetDir))
baseDir = os.path.dirname(targetDir)
print(f"Using directory: {targetDir}")

# Check for the script directory
scriptDir = os.path.join(baseDir, "scripts")
if not os.path.isdir(scriptDir):
    print(f"The script directory does not exists in the parent directory.\nWould you like the create one now? [y/N]")
    if re.match(r'[yY][eE]*[sS]*', input()):
        os.makedirs(scriptDir)
    else:
        scriptDir = baseDir

# Create _directory file
if os.path.isdir(scriptDir):
    dirFile = os.path.join(scriptDir, "_directory.py")
    with open(dirFile, "w+") as file:
        dateString = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') # 29
        dateString = "{:<29}".format(dateString)
        
        content = "\n".join([
            "# ==================================================================== #",
            "#  File name:      _directory.py                #        _.==._        #",
            "#  Author:         Arjan Lemmens                #     .+=##**##=+.     #",
            f"#  Date:           {dateString}#    *= #        =*    #",
            "# ============================================= #   #/  #         \\#   #",
            "#  Description:    Contains the local directory #  |#   #   $      #|  #",
            "#                  used by other scripts        #  |#   #   #      #|  #",
            "#                  This file is automatically   #   #\\  #   #     /#   #",
            "#                  generated using the          #    *= #   #    =+    #",
            "#                  set_directory.py script.     #     *++######++*     #",
            "#                                               #        *-==-*        #",
            "# ==================================================================== #",
            "",
            "import os",
            "",
            f"PROJECT_NAME = \"{projectName}\"",
            f"BASE_DIRECTORY = \"{baseDir}\"",
            f"PROJECT_DIRECTORY = os.path.join(BASE_DIRECTORY, PROJECT_NAME)"
            ])
        
        if os.path.isdir(os.path.join(baseDir, ".venv")):
            content += f"\nVENV_DIRECTORY = os.path.join(BASE_DIRECTORY, \".venv\")"
        
        file.write(content)