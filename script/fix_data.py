import sys
import re

GROUPED_ADDRESS_REGEX = re.compile(r'^(\d+)-\d*\s+(.*)')
LEADING_ADDRESS_REGEX = re.compile(r'(.*)\s0+(\d+th.*)', re.IGNORECASE)
 
def make_address_singular(address=''):
	fixed_address = address

	matched_address = GROUPED_ADDRESS_REGEX.match(address)
	if matched_address:
		number = matched_address.group(1)
		street = matched_address.group(2)
		fixed_address = number + ' ' + street
		# print("SINGULARIZED: " + address + " to " + fixed_address)

	return fixed_address

def remove_leading_zeroes_from_street(addresss=''):
	fixed_address = address
	matched_address = LEADING_ADDRESS_REGEX.match(address)
	if matched_address:
		first_part = matched_address.group(1)
		second_part = matched_address.group(2)
		fixed_address = first_part + ' ' + second_part
		# print("LEADING 0 REMOVED: " + address + " to " + fixed_address)

	return fixed_address



# ----- Execute application -----
if len(sys.argv) != 3:
	print("Usage: python scripts/fix_data.py <input_file> <output file>")
	print("\t<input file>: Table export of vacant properties (CSV format)")
	print("\t<output file>: Fixed version of the input file (CSV format)")
	sys.exit()

orig_file = open(sys.argv[1], 'r')
mod_file = open(sys.argv[2], 'w')

skipped_first_line = False
num = 1



for line in orig_file.readlines():
    # Skip over the header line
	if not skipped_first_line:
		mod_file.write(line)
		skipped_first_line = True
		continue

	# Break the line into pieces
	split_line = line.split(',')

	# parcelid = split_line[0]
	# tencode = split_line[1]
	address = split_line[2]
	# owner1 = split_line[3]
	# owner2 = split_line[4]
	# bldg_code = split_line[5]
	# bldg_desc = split_line[6]
	# brt_id = split_line[7]
	# num_brt = split_line[8]
	# num_accoun = split_line[9]
	# gross_area = split_line[10]
	# brt_websit = split_line[11]
	# shape_area = split_line[12]
	# shape_len = split_line[13]
	# d_num_brt = split_line[14]
	
	# Remove lines that don't have an address
	if not address:
		# print "BLANK ADDRESS LINE REMOVED"
		continue

	# Make addresses singular (remove "-\d* from street addresses)
	address = make_address_singular(address)

	# Remove leading 0s from streets
	address = remove_leading_zeroes_from_street(address)

	# Write the fixed line to file
	split_line[2] = address
	fixed_line = ','.join(split_line)
	mod_file.write(fixed_line)