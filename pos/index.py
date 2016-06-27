import assignment, linecache, csv

progress_file = open("progress.txt", "r")
#print linecache.getline('corpus.txt', 3)
progress = int(progress_file.readline())

while progress <= 12: #finding line count takes a long time if we want to expand this
	#print progress
	sentence = linecache.getline('corpus.txt',progress)
	progress += 1
	progress_file = open("progress.txt", "w")
	progress_file.write(str(progress))
	#print assignment.sentenceToAbbreviated(sentence)
	with open("library.csv", "a") as fp:
	    wr = csv.writer(fp, lineterminator = '\n', dialect='excel')
	    wr.writerow(assignment.sentenceToAbbreviated(sentence))