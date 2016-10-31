from bs4 import BeautifulSoup
import nltk
import requests
import re


url = raw_input("Enter a website url to scrape:") 

r = requests.get("http://"+url)
website = r.text

soup = BeautifulSoup(website,"lxml")
#print soup.prettify()

desc = ""
keywords=""
twitterDesc =""
for meta in soup.findAll("meta"):
    metaname = meta.get('name', '').lower()  #Finds attribute title and lowercases for case sensitivity
    metaprop = meta.get('property', '').lower()

    if 'description' == metaname or metaprop.find("description")>0:
      desc = meta['content'].strip().encode("utf8")
      #print desc

    #if 'twitter:description' == metaname or metaprop.find("twitter:description"):
      #twitterDesc = meta['content'].strip()

    if 'keywords' == metaname or metaprop.find("keywords")>0:
      keywords = meta['content'].strip().encode("utf8")
      #print keywords

with open("RawInfo", "a") as f:
    f.write(url + "\n" + desc + "\n" + "Keywords: " + keywords + "\n" + "\n")
f.close()


#metaContent = soup.find(attrs={"name":"Description"}) #attribute : attribute title

#if metaContent == None:
  #metaContent = soup.find(attrs={"name":"description"})     #case sensitive 

#print "Description: " + '\n' + metaContent['content'].strip()



#text = soup.find_all(["p","h1","h2","h3","h4"])





