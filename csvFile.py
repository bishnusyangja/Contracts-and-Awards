import csv

# read the file and return rows
def read_file(filepath):
	rows = []
	header = []
	with open(filepath) as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=',')
	    for i, row_item in enumerate(spamreader):
	    	if i == 0:
	    		header = row_item
	    	else:
	        	row = {}
	        	for j, item in enumerate(row_item):
	        		row[header[j]] = item 
	        	rows.append(row)
	return header, rows
