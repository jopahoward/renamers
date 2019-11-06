################################################################################
# Renamer for MO 319 (Accounting for middle names)                             #
# Author: Joseph Howard | github.com/jopahoward                                #
# Revised on 11.5.19                                                           #
# Usage: Put both this file, and a csv named 'mo319codes.csv' into folder with #
#        all files to rename. Files should follow the format:                  #
#        <lastname,firstname>[middlename]_*.<filetype>												 #
#				 This program accounts for changing names and simply searches for the  #
#				 string <lastnamefirstname>									                           #
#                                                                              #
# CSV Formatting: No headers or other extraneous data should be included       #
# Row format: <lastname><firstname>,<New assignment name>                      #
#                                                                              #
# Effects: Renames the files in the folder to the names designated in          #
#          mo319codes.csv                                                      #
################################################################################

import os
import csv

# Find current path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Open csv and import to code_interpreter
code_file = open('mo319codes.csv', 'r')
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

	# Find first underscore
	delimiter = filename.find('_')
	# If delimiter not found, skip file
	if (delimiter == -1):
		continue

	# Extract student name
	studentName = filename[:delimiter]
	# Get filetype
	delimiter = filename.rfind('.')
	filetype = filename[delimiter:]

	# Find appropriate row for this file, rename
	for row in code_interpreter:
		found = -1
		found = studentName.find(row[0])
		if (found == 0):
			new_filename = str(row[1]) + filetype
			# For two files, rename the second as filename_1
			try:
				os.rename(filename, new_filename)
			except:
				new_filename = str(row[1]) + '_1' + filetype
				os.rename(filename, new_filename)
