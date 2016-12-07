from bs4 import BeautifulSoup
import requests

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.draw.dispersion import dispersion_plot

# Gets the frequency data and plots dispersion and cumulative frequency plots.


def filter(text):
 	text = word_tokenize(text)                      #Tokenize words for preprocessing

 	trashWords = set(stopwords.words('english'))

 	text = [word for word in text if len(word) > 1]     #Remove punctuation(keep words)
 	text = [word for word in text if not word.isnumeric()]     #Remove numbers
 	text = [word.lower() for word in text]          #Lower case all words

 	textStorage = []

 	for i in text:                                #Deleting filler words out of text
     	 if i not in trashWords:
         	textStorage.append(i)
 	return textStorage

url = raw_input("Enter a website url to scrape:") 

r = requests.get("http://"+url)
website = r.text

soup = BeautifulSoup(website,"lxml")
#print soup.prettify()

for script in soup(["script", "style"]):     #Rip out script and styling text
    script.extract()

clean_text = soup.get_text(" ")
#print clean_text

lines = (line.strip() for line in clean_text.splitlines())            # break multi-headlines into a line each
text = '\n'.join(line for line in lines)

filteredText = filter(text)                       #Filter text for punct,nums and normalize words to lower case
mytext = nltk.Text(filteredText)             #Make it into an nltk object

fdist = nltk.FreqDist(filteredText)   

print fdist.most_common(15)        #top 15 most common 
#mytext.dispersion_plot(["daniels", "college"])              #how often certain words appear in the text
fdist.plot(15,cumulative = True)