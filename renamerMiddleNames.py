import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

code_file = open('mo319codes.csv', 'r')
code_reader = csv.reader(code_file, delimiter=',')
code_interpreter = []
for row in code_reader:
	code_interpreter.append(row)

for file in os.listdir(dir_path):
	filename = os.fsdecode(file)
	if filename.endswith(".py") or filename.endswith(".csv"):
		continue

	delimiter = filename.find('_')
	if (delimiter == -1):
		continue

	studentName = filename[:delimiter]
	delimiter = filename.rfind('.')
	filetype = filename[delimiter:]
	for row in code_interpreter:
		found = -1
		found = studentName.find(row[0])
		if (found == 0):
			new_filename = str(row[1]) + filetype
			try:
				os.rename(filename, new_filename)
			except:
				new_filename = str(row[1]) + '_1' + filetype
				os.rename(filename, new_filename)
