################################################################################
# Renamer for MO 300                                                           #
# Author: Joseph Howard | github.com/jopahoward                                #
# Revised on 11.5.19                                                           #
# Usage: Put both this file, and a csv named 'mo319codes.csv' into folder with #
#        all files to rename. Files should follow the format:                  #
#        mo300section<section #>group<group #>_*.<filetype>                    #
#                                                                              #
# CSV Formatting: No headers or other extraneous data should be included       #
# Row format: <section #>,<group #>,<New assignment name>                      #
#                                                                              #
# Effects: Renames the files in the folder to the names designated in          #
#          mo300codes.csv                                                      #
################################################################################

import os
import csv

# Find current path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Open csv and import to code_interpreter
code_file = open('mo300codes.csv', 'r')
code_reader = csv.reader(code_file, delimiter=',')
code_interpreter = []
for row in code_reader:
    code_interpreter.append(row)

# Main body to rename files
for file in os.listdir(dir_path):
    filename = os.fsdecode(file)

    # Ignore this file, and the code_file
    if filename.endswith(".py") or filename.endswith(".csv"):
        continue

    # Find "section" & "group"
    section_delim = filename.find("section")
    group_delim = filename.find("group")
    delimiter = filename.find('_')

    # Skip files if they do not contain the correct filename format
    if (delimiter == -1 or section_delim == -1 or group_delim == -1):
    	continue

    # get section and group numbers
    section = int(filename[(section_delim + 7):group_delim])
    group = int(filename[(group_delim + 5):delimiter])

    # Get filetype
    delimiter = filename.rfind('.')
    filetype = filename[delimiter:]

    # find appropriate row for this file, rename
    for row in code_interpreter:
        if section == int(row[0]) and group == int(row[1]):
            new_filename = str(row[2]) + filetype
            try:
                os.rename(filename, new_filename)
            except:
                new_filename = str(row[2]) + '_1' + filetype
                os.rename(filename, new_filename)
