from bs4 import BeautifulSoup
import requests

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.draw.dispersion import dispersion_plot

# -*- coding: utf-8 -*-

def filter(text):
 	text = word_tokenize(text)                      #Tokenize words for preprocessing

 	trashWords = set(stopwords.words('english'))

 	text = [word for word in text if len(word) > 1]     #Remove punctuation
 	text = [word for word in text if not word.isnumeric()]     #Remove numbers
 	text = [word.lower() for word in text]          #Lower case all words

 	textStorage = []

 	for i in text:                                #Deleting filler words out of text
     	 if i not in trashWords:
         	textStorage.append(i)
 	return textStorage

def syn(word, lch_threshold):
    synonyms = []
    for word1 in wn.synsets(word):
        synonyms.append(word1.lemmas()[0].name())        #Append synonyms of word to set
        for word2 in wn.all_synsets():
            try:
                lch = word1.lch_similarity(word2)
            except:                                 #skip over words that dont address same POS
                continue
            
            if lch >= lch_threshold:
                synonyms.append(word2.lemmas()[0].name())     #Append synonyms of the synonyms (if they meet threshold) to set
                #yield (word1, word2, lch)
    return synonyms


url = raw_input("Enter a website url to scrape:") 

r = requests.get("http://"+url)
website = r.text

soup = BeautifulSoup(website,"lxml")
#print soup.prettify()

for script in soup(["script", "style"]):     #Rip out script and styling text
    script.extract()

clean_text = soup.get_text(" ")

lines = (line.strip() for line in clean_text.splitlines())            # break multi-headlines into a line each
text = '\n'.join(line for line in lines)

filteredText = filter(text)                       #Filter text for punct,nums and normalize words to lower case

synSincerity = syn("sincerity",2.26)
synRugged = (syn("ruggedness",2.26))
synSophistic = (syn("sophistication",2.26))     #Getting every synonym possible.ever.
synCompetence = (syn("competence",2.26))
synExcite = (syn("excitement",2.26))



#filteredText.dispersion_plot([synSincerity,synRugged, synSophistic, synCompetence,synExcite])

#print allSyn

# synonyms = wn.synsets("sincerity")

# for i in synonyms:
# 	#print(i.lemmas()[0].name())
# 	allSyn.append(i.lemmas()[0].name())


fdist = nltk.FreqDist(filteredText)            #Frequency Distribution

allSyn = [synSincerity,synRugged, synExcite, synCompetence,synSophistic]

for i in allSyn:
    for j in i:
        if fdist[j] != 0:
            print "Word:",j ," Frequency: ",fdist[j]

    










