# WebScraping

Description: A set of scripts that web scrape various sites.

FrequencyAnalysis.py - Identifies synonyms of the 5 brand personality words base on Leacock-Chodorow similarity and parses through the text on a webpage to identify similar words.

KeywordScrape.py - Parses through the code of a website and pulls content out based on the specified meta tags.

Keywords.py - Identifies the most freqently appearing words in a given text.

WebsiteScrape.py - Extracts text from a website and trains the Punkt Sentence Tokenizer to tag the POS of each word. All adjectives are then pulled out at the end.

### Dependencies

1. Python 2.7
2. NLTK
3. BeautifulSoup
4. requests
5. re

### Setup

1. In order to setup an environment you can use for development, you can simply install virtualenv via pip

[Installing virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

[Using virtualenv](https://virtualenv.pypa.io/en/stable/userguide/#usage)

2. Once you have installed and setup a virtualenv, proceed to install the Python packages listed in the Dependencies section above.

3. Now you should have an environment that can run the scripts!

### How to Use

1. Activate your virtualenv and change directories to where you have cloned this repo using the terminal commands **cd** and **ls** to change your current directory and to list the files in your current location respectively.

2. Once you navigate to the directory that stores the scripts listed above, you can run each script by typing "./*script*" and following the command prompts.
