from bs4 import BeautifulSoup
import requests  											#Import statements to make sure the libraries we want are accessible 

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

#Extracts all readable text from a website, trains the Punkt Sentence Tokenizer and tags the POS of each word. It then extracts the adjectives.

# -*- coding: utf-8 -*-

# def filter(text):
# 	#text = word_tokenize(text)                      #Tokenize words for preprocessing

# 	trashWords = set(stopwords.words('english'))    

# 	textStorage = []

# 	for i in text:                                #Deleting filler words out of text
#     	 if i not in trashWords:
#         	textStorage.append(i)
# 	return textStorage

def process_content(tokenizedText):             #Function to tokenize each word and append a POS tag to each word and store it
    tagged = []
    for i in tokenized:
         words = nltk.word_tokenize(i)
         tagged.append(nltk.pos_tag(words))
         #print tagged
    return tagged


url = raw_input("Enter a website url to scrape:")  # Prompts user of program for a website 

r = requests.get("http://"+url)
website = r.text                   #Gets website content 

soup = BeautifulSoup(website,"lxml")      #Makes the website content into a beautiful soup object with a backend lxml parser
#print soup.prettify()

for script in soup(["script", "style"]):     #Rip out script and styling text
    script.extract()

clean_text = soup.get_text(" ")      #Obtains text from soup object separated by a space

lines = (line.strip() for line in clean_text.splitlines())            # break multi-headlines into a line each and join them to get rid of conjoined words
text = '\n'.join(line for line in lines)


trainText = inaugural.raw("2009-Obama.txt")                         #Training the punkt sentence tokenizer for POS tagging
custom_sent_tokenizer = PunktSentenceTokenizer(trainText)
tokenized = custom_sent_tokenizer.tokenize(text)

posContent = process_content(tokenized)         #Processes tokenized words and passes into the process_content function to tag the words

adjectives = []               #Creating an array to store the adjectives in
nouns = []

#JJ = Adjectives
#NN = Nouns
#NNS = Plural nouns
#VB = Verb

for i in posContent:
	if i[1] == "JJ":    # If the word is tagged as an adjective 
		#print i                     
		adjectives.append(i[0])  #Append the word to the array
	for j in i:                        #This extra for loop is due to there being arrays within arrays in the posContent variable
		if j[1] == "JJ":
			#print j	
			adjectives.append(j[0])
print adjectives

for i in posContent:
	if i[1] == "NN":    # If the word is tagged as an adjective 
		#print i                     
		nouns.append(i[0])  #Append the word to the array
	for j in i:                        #This extra for loop is due to there being arrays within arrays in the posContent variable
		if j[1] == "NN":
			#print j	
			nouns.append(j[0])
print nouns

# with open("POS Words", "a") as f:
#  	f.write("URL: " + url + "\n" + "Adjectives: ")                      #Writing information to a file
#  	for adj in adjectives:
#  		f.write(adj.encode('utf-8') + ", ")
#  	f.write("\n" + "Nouns: ")
#  	for n in nouns:
#  		f.write(n.encode('utf-8') + ", ")
    	
# f.close()

#print fdist.most_common(10)
