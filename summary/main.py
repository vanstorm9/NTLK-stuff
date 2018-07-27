from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer

import sys
reload(sys)
sys.setdefaultencoding('utf8')


with open("test.txt","r") as readFile:
	text = readFile.read().replace('\n','')

stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()

for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word,freq in freqTable.items():
		
		if word in sentence.lower():
			#print sentence
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues/len(sentenceValue))

summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and sentenceValue[sentence] > (1.2*average):
		summary += " " + sentence


print(summary)
			
		
