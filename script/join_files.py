import sys
import os
import re
import glob

# Get command line arguments
if len(sys.argv) != 3:
	print("Usage: python join_file.py <directory with geocoded JSON files> <output file>")
	print("Description: Joins a bunch of a files (with a common filename convention) together into one file")
	sys.exit()

input_dir_path = sys.argv[1]
output_file_path = sys.argv[2]

# Get a list of files
input_files = glob.glob(input_dir_path + '/*_geo.csv')

# Open the output file
output_file = open(output_file_path, 'w')

# Write lines to
applied_header_line = False
for input_file_path in input_files:
	print('Reading ' + input_file_path)
	input_file = open(input_file_path, 'r')

	if not applied_header_line: # skip first line, with header row, after written once
		header_line = input_file.readline() 
		output_file.write(header_line)
	for line in input_file:
		output_file.write(line)

output_file.close()