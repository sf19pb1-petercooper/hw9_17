"""
Output a list of the words from multiple cells in a CSV, in order of the most 
frequent. Ignores common words. 

Sample output:
58 br
36 banking
26 content
17 baas
14 across
14 amp
14 open
etc.
"""
import collections
import requests
import pandas
import matplotlib
import nltk
from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize - This looks to be a significantly 
# easier implementation of tokenizing words vs the string punctuation solution.

#nltk.download('punkt')
  
stop_words = set(stopwords.words('english')) 
listOfWords=[]
cleanListOfWords = []


with open('/content/sample_data/media_data2.csv', newline='',encoding='mac_roman') as csvfile:
     dataFrame = pandas.read_csv(csvfile)

#have a look at the data

#dataFrame
#print(dataFrame.body)
#print(type(dataFrame.body))


punctuation = string.punctuation + "\u201C\u201D"   #double quotes “ ”
paragraphs = dataFrame.body.tolist()
print(type(paragraphs))

for paragraph in paragraphs:
    for word in paragraph.split():
        word = word.strip(punctuation)
        if word:   #if word is not the empty string
            word = word.lower()
            listOfWords.append(word)

# Clean list to make sure stop words are not counted
for word in listOfWords:
    if word not in stop_words:
        cleanListOfWords.append(word)

#Counter is like a dict.  Keys are words, values are counts.
counter = collections.Counter(cleanListOfWords)
listOfTuples = counter.most_common()
#print(counter)

for word, i in listOfTuples:
    print(f"{i:2} {word}")

#sys.exit(0)
