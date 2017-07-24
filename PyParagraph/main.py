#This program takes as input a .txt file which resides in the same folder as this 
#program resides and outputs to the console the number of words in the paragraph, 
# number of sentences, avg, letter count per word, and avg. word count per sentence

import os
import string
import re

# Counter is used for the bonus solution
from collections import Counter

totalLetterCount = 0

# Paths
para_path = os.path.join(os.getcwd(), 'Para.txt')

# Grab the text from the txt file and convert to a list of words based on spaces as a delimiter
with open(para_path, "r") as para_file_handler:
     wordList = para_file_handler.read().split()
#print(wordList) 

#Approximate word count (note: there might be a hyphen here and there counted as a word but it's okay since we're going for approx. count)
wordCount = len(wordList)
print("Approximate word count: " + str(wordCount))

#Convert paragraph to a list of sentences, using as delimiter, punctuation that can be used at the end of a sentence !?.
with open(para_path, "r") as para_file_handler:
	r = '.?!'
	delimiters = ".","?","!","\n"
	sentenceList = para_file_handler.read()
	#allow to build the pattern automatically and have the delimiters escaped nicely
	regexPattern = '|'.join(map(re.escape, delimiters))
	sentenceList = re.split(regexPattern,sentenceList)
#print(sentenceList) 

#Approximate sentence count
sentenceCount = len(sentenceList) - 1 # subtract 1 to compensate the extra space it includes at the end in the split list
print("Approximate sentence count: " + str(sentenceCount))

# Create an empty list
para = []

#List of punctuation symbols 
punctuation = list(string.punctuation)

# Remove trailing punctuation from words -- commas, periods, exclamation marks etc.
for word in wordList:
    para.append(word.split(string.punctuation)[0])

#Average letter count (per word) = Total number of letters in the para div by the total number of words
for word in para:
	#If the word is punctuation or a space, count the letters in it else ignore.
	if (word not in punctuation) and (word != " "):
		totalLetterCount += len(word)

avgLetterCount = totalLetterCount/wordCount
print("Average letter count (per word): " + str(avgLetterCount))

#Average sentence length (in words) = number of words in para div by number of sentences
avgSentenceCount = wordCount/sentenceCount
print("Average sentence length (in words): " + str(avgSentenceCount))