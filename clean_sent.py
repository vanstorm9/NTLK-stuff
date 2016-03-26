from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize
import string


# For splitting words into tokens 
punctuations = list(string.punctuation)
#print punctuations
punctuations.append("''")
#sent = '''He said,"that's it."'''
sent = 'He said "Yes, this works!", which is why he was successful'
print sent
#print word_tokenize(sent)
#print [i for i in word_tokenize(sent) if i not in punctuations]
print ''
print ''


for i in word_tokenize(sent):
    if i not in punctuations:
        #print i
        print WordNetLemmatizer().lemmatize(i,'v')



#print [i.strip("".join(punctuations)) for i in word_tokenize(sent) if i not in punctuations]
