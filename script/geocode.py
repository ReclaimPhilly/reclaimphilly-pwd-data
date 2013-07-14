import sys
import json
import requests

# ----- Execute application -----
if len(sys.argv) != 3:
	print("Usage: python geocode.py <input_file> <output file>")
	print("\t<input file>: Table export of vacant properties (CSV format)")
	print("\t<output file>: The input file with two extra columns: latitude and longitude")
	sys.exit()

orig_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')


skipped_first_line = False

# Get and edit the header line
column_header_line = orig_file.readline().strip() + ",LATITUDE,LONGITUDE\n"
out_file.write(column_header_line)


for line in orig_file:

	# Get the address
	address = line.split(',')[2]
	request = requests.get("http://localhost:8000/services/geocode/" + address)

	try:
		point = json.loads(request.text)[0]
	except:
		print("SKIPPING: " + line.strip())
		continue

	latitude = point['coordinates'][0]
	longitude = point['coordinates'][1]

	new_line = line.strip() + ',' + str(latitude) + ',' + str(longitude) + '\n'
	out_file.write(new_line)
	print(new_line)

out_file.close()