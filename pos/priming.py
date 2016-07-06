terminators = {".":".\n", "?":"?\n", "!":"!\n"}

file = open("corpus.txt", "r")
	content = file.read()
for i, j in terminators.iteritems():
    content = content.replace(i, j)	
# print content

file = open("corpus.txt", "w") file.write(content)
