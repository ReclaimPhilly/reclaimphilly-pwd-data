import sys
import sqlite3

# Get command line arguments
if len(sys.argv) != 3:
	print("Usage: python load_file_sqlite.py <PWD CSV file path> <DB file path>")
	print("Description: Loads date from a geocoded PWD CSV into a SQLite database")
	sys.exit()

input_file_path = sys.argv[1]
db_path = sys.argv[2]


# Open the input file, skip the first line (header row)
input_file = open(input_file_path, 'r')
input_file.readline()

# Connect to the database
db_connection = sqlite3.connect(db_path)
db_cursor = db_connection.cursor()

# Iterate through the records and get the necessary parts, put into tuples
locations = []
for line in input_file:
	# Get the parts of the CSV row
	split_line = line.split(',')

	# parcelid = split_line[0]
	# tencode = split_line[1]
	address = split_line[2].lower()
	# owner1 = split_line[3]
	# owner2 = split_line[4]
	bldg_code = split_line[5].lower()
	# bldg_desc = split_line[6]
	# brt_id = split_line[7]
	# num_brt = split_line[8]
	# num_accoun = split_line[9]
	# gross_area = split_line[10]
	# brt_websit = split_line[11]
	# shape_area = split_line[12]
	# shape_len = split_line[13]
	# d_num_brt = split_line[14]
	latitude = split_line[15]
	longitude = split_line[16]

	# Convert the building code
	if bldg_code == 'sr':
		type = 'res'
	elif bldg_code == 'sc' or bldg_code == 'sd' or bldg_code == 'si' or bldg_code == 'sj': # commercial or industrial
		type = 'nrs'
	else:
		continue

	# Create the tuple
	row = (latitude, longitude, address, type, 'Philadelphia Water Dept. idenfied this as vacant')

	# Store it
	locations.append(row)

# Persist to the database
db_cursor.executemany('INSERT into web_location (latitude, longitude, address, type, description) values (?, ?, ?, ?, ?)', locations)
db_connection.commit()
# for row in locations:
# 	print(row)