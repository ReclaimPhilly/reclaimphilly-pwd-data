import sys
import MySQLdb

# Get command line arguments
if len(sys.argv) != 6:
	print("Usage: python load_file_mysql.py <PWD CSV file path> <DB host URL> <DB user ID> <DB user password> <DB name>")
	print("Description: Loads date from a geocoded PWD CSV into a Reclaim Philly MySQL database")
	sys.exit()

input_file_path = sys.argv[1]
host = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
db_name = sys.argv[5]


# Open the input file, skip the first line (header row)
input_file = open(input_file_path, 'r')
input_file.readline()

# Connect to the database
db_connection = MySQLdb.connect(host=host, user=user, passwd=password, db=db_name)
db_cursor = db_connection.cursor()

# Iterate through the records and get the necessary parts, put into tuples
locations = []
geocodes = []
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
		parcel_type = 'res'
	elif bldg_code == 'sc' or bldg_code == 'sd' or bldg_code == 'si' or bldg_code == 'sj': # commercial or industrial
		parcel_type = 'nrs'
	else:
		continue

	# Create the tuples
	location_row = (latitude, longitude, address, parcel_type, 'Philadelphia Water Dept. idenfied this as vacant', 0, 0)
	geocode_row = (latitude, longitude, address)

	# Store it
	locations.append(location_row)
	geocodes.append(geocode_row)

# Persist to the database
db_cursor.executemany('INSERT into web_location (latitude, longitude, address, lot_type, description, upVotes, downVotes) values (?, ?, ?, ?, ?, ?, ?)', locations)
db_cursor.executemany('INSERT into web_geocodecache (latitude, longitude, address) values (?, ?, ?)', geocodes)
db_connection.commit()
