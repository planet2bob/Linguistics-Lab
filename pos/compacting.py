import csv, sys

# filename = sys.argv[1]
row_number, column_number = 1, 1
patterns = [['',''],['','']]

with open("testing.csv", 'rb') as vb:
    rows = list(csv.reader(vb, lineterminator = '\n', dialect='excel'))
    #print rows[row_number][column_number]

with open("testing.csv", 'rb') as vb:
	rows = list(csv.reader(vb, lineterminator = '\n', dialect='excel'))
	for i in range(len(rows)):
		pattern = ""
		for l in range(len(rows[i])):
			pattern += (str(rows[i][l]))
		placement = -1
		for l in range(2):
			if(patterns[l][0] == pattern):
				placement = l
		if placement == -1:
			patterns.append(pattern)
		else:
			patterns[l][0] += 1

		print patterns[:]