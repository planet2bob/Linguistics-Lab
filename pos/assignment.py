import nltk

parts_translation = {'$':'dollar sign', 
					'\'':'single quote', 
					'(':'open paren', 
					')':'close paren',
					',':'comma',
					'--':'dash',
					'.':'sentence terminator',
					':':'colon or elipses',
					'CC':'conjunction/coordinating',
					'CD':'cardinal number',
					'DT':'determiner',
					'EX':'existential there',
					'FW':'foreign word',
					'IN':'subordination conjunction',
					'JJ':'ordinal adjective',
					'JJR':'comparative adjective',
					'JJS':'superlative adjective',
					'LS':'list item marker',
					'MD':'modal auxiliary',
					'NN':'singular common noun',
					'NNP':'singular proper noun',
					'NNPS':'plural proper noun',
					'NNS':'plural common noun',
					'PDT':'pre determiner',
					'POS':'possessive marker',
					'PRP':'personal pronoun',
					'PRP$':'possessive pronoun',
					'RB':'adverb',
					'RBR':'comparative adverb',
					'RBS':'superlative adverb',
					'RP':'particle',
					'SYM':'symbol',
					'TO':'to as a marker',
					'UH':'interjection',
					'VB':'base form verb',
					'VBD':'past tense verb',
					'VBG':'present/gerand verb',
					'VBN':'past participle verb',
					'VBP':'1st person present tense verb',
					'VBZ':'3rd person singular present tense verb',
					'WDT':'WH determiner',
					'WP':'WH pronoun',
					'WP$':'WP possessive pronoun',
					'WHB':'WH adverb',
					}

# test_string = "At eight on tuesday morning Nick went to a star."
# tokens = nltk.word_tokenize(test_string)
# print tokens[:]
# tagged = nltk.pos_tag(tokens)
# print tagged[:]

# pos = []

# for a in range(len(tagged)):
# 	pos.append(1)
# 	pos[a] = parts_translation[tagged[a][1]]

# print pos[:]

def sentenceToAbbreviated(sentence):
	tokens = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(tokens)
	abbreviations = []
	for a in range(len(tagged)):
		abbreviations.append(1)
		abbreviations[a] = tagged[a][1]
	return abbreviations

def abbreviationsToEnglish(abbreviations):
	english = []
	for a in range(len(abbreviations)):
		english.append(1)
		english[a] = parts_translation[abbreviations[a]]
	return abbreviations