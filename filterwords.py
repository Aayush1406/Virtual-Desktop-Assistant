import audio
import speech
from nltk.corpus import stopwords #natural language toolkit
from nltk.tokenize import word_tokenize 
#nltk.download("all")
#nltk.download("stopwords")
def filter_txt(response):
        
    stop_words=(stopwords.words("english")) #list of english stopwords are stored in stop_words
    filter=[]#empty filter list is created

    #quote="hey professor please open shershah movie"
    result=word_tokenize(response) #response is separated into each word separated by comma inside a list
    for items in result: # iterating a list
        if items.casefold() not in stop_words: #if words are not present inside stopwords list than it will append in empty filter list
            filter.append(items)
    print(filter)
    return filter
    