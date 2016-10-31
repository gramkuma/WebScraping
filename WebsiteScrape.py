from bs4 import BeautifulSoup
import requests

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

# -*- coding: utf-8 -*-

# def filter(text):
# 	#text = word_tokenize(text)                      #Tokenize words for preprocessing

# 	trashWords = set(stopwords.words('english'))    

# 	textStorage = []

# 	for i in text:                                #Deleting filler words out of text
#     	 if i not in trashWords:
#         	textStorage.append(i)
# 	return textStorage

def process_content(tokenizedText):
    tagged = []
    for i in tokenized:
         words = nltk.word_tokenize(i)
         tagged.append(nltk.pos_tag(words))
         #print tagged
    return tagged


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

#print(text)

#filteredText = filter(text)

trainText = inaugural.raw("2009-Obama.txt")                         #Training the punkt sentence tokenizer for POS tagging
custom_sent_tokenizer = PunktSentenceTokenizer(trainText)
tokenized = custom_sent_tokenizer.tokenize(text)

posContent = process_content(tokenized)
print posContent
