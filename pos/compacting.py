import csv, sys

# filename = sys.argv[1]

patterns = {}

with open("library.csv", 'rb') as vb:
    rows = list(csv.reader(vb, lineterminator = '\n', dialect='excel'))
    #print rows[row_number][column_number]
    for i in range(len(rows)):
    	try:
    		patterns[rows[i][0]] = patterns[rows[i][0]] + 1
    	except:
    		patterns[rows[i][0]] = 1

writer = csv.writer(open('dict.csv', 'wb'))
for key, value in patterns.items():
   writer.writerow([key, value])