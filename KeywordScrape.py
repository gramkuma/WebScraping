from bs4 import BeautifulSoup
import nltk
import requests
import re

# Runs through the code of a website and pulls out the specified meta tags and other tags and their content. C

url = raw_input("Enter a website url to scrape:") 

r = requests.get("http://"+url)
website = r.text

soup = BeautifulSoup(website,"lxml")
#print soup.prettify()

desc = ""
keywords=""
title =""
h1 = ""
for meta in soup.findAll("meta"):
    metaname = meta.get('name', '').lower()  #Finds attribute title and lowercases for case sensitivity
    metaprop = meta.get('property', '').lower()

    if 'description' == metaname or metaprop.find("description")>0:
      desc = meta['content'].strip().encode("utf8")
      #print desc

    if 'keywords' == metaname or metaprop.find("keywords")>0:
      keywords = meta['content'].strip().encode("utf8")
      #print keywords

title = soup.findAll("title")     #Other Tags
h1 = soup.findAll("h1")

print( "Description: ", desc ,  "\n" , "title: ", title , "\n" , "h1 tag: ", h1 , "\n")

#with open("RawInfo", "a") as f:                      #Writing information to a file
    #f.write(url + "\n" + desc + "\n" + "Keywords: " + keywords + "\n" + "Title: " + title +  "\n" + "H1 Tag:"  + h1  + "\n" + "\n")
#f.close()


#metaContent = soup.find(attrs={"name":"Description"}) #attribute : attribute title

#if metaContent == None:
  #metaContent = soup.find(attrs={"name":"description"})     #case sensitive 

#print "Description: " + '\n' + metaContent['content'].strip()




