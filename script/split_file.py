import sys

if len(sys.argv) != 4:
	print("Usage: python split_file.py <original file name> <destination dir> <lines per file> ")
	print("Description: Splits a line-based  table into separate files, putting the first line in the original file at the top of each sub file.")
	sys.exit()


# Arguments
orig_file_name = sys.argv[1]
dest_dir_name = sys.argv[2]
lines_per_file = int(sys.argv[3])

# Open the file to be split
orig_file = open(orig_file_name, 'r')


line_count = 1
file_number = 1
dest_file = open(dest_dir_name + '/' + str(file_number) + '.csv', 'w')

# Put the column headers in the file
column_header_line = orig_file.readline()
dest_file.write(column_header_line)

for line in orig_file:

	# Switch to a new file if over the max number of lines
	if line_count > lines_per_file:
		dest_file.close()

		file_number += 1
		dest_file = open(dest_dir_name + '/' + str(file_number) + '.csv', 'w')

		line_count = 1
		dest_file.write(column_header_line)
		

	# Write the line to file
	dest_file.write(line)
	line_count += 1

# Close things up
dest_file.close()