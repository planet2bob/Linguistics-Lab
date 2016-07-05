import csv, sys

# filename = sys.argv[1]

patterns = {}

with open("testing.csv", 'rb') as vb:
    rows = list(csv.reader(vb, lineterminator = '\n', dialect='excel'))
    #print rows[row_number][column_number]
    for i in range(len(rows)):
    	try:
    		patterns[rows[i][0]] = patterns[rows[i][0]] + 1
    	except:
    		patterns[rows[i][0]] = 1

print patterns