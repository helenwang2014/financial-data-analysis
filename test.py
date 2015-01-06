# open files in a folder

import csv as csv
import numpy as np
import os

#open up a csc file in to a python object

for filename in os.listdir('./HKEX/HKEX_2010'):
	csv_file_object = csv.reader(open('./HKEX/HKEX_2010/' + filename, 'rb'))
	
	data = []
	for row in csv_file_object:
		data.append(row)
	data = np.array(data)

print data[-1]
