import nltk
import heapq
import os
import re
import collections
import math
#import nltk.book

#from Analyzer import Analyzer
import Analyzer

from pybrain.supervised.trainers import BackpropTrainer

booksParsed = 0


def main():
    locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/cache/generated"
    #iterateThroughAllBooks(locationOfBooks)
    #testBook = locationOfBooks + "/68/pg68.txt"
    #testBook0 = "C:/Users/Dylan/AppData/Roaming/nltk_data/corpora/gutenberg/carroll-alice.txt"
    #testBook0 = "C:/Users/Dylan/AppData/Roaming/nltk_data/corpora/gutenberg/milton-paradise.txt"
    #testBook0 = locationOfBooks + "/oz/oz.txt"
    #testBook0 = locationOfBooks + "/mockingbird/mockingbird.txt"
    testBook0 = "C:/Users/Dylan/AppData/Roaming/nltk_data/corpora/gutenberg/shakespeare-hamlet.txt"
    testBook1 = locationOfBooks + "/Dickens/greatExpectations.txt"
    testBook2 = "C:/Users/Dylan/AppData/Roaming/nltk_data/corpora/gutenberg/austen-persuasion.txt"
    testBook3 =  "C:/Users/Dylan/AppData/Roaming/nltk_data/corpora/gutenberg/austen-sense.txt"
    
    #removeGutenbergFromBook(testBook)
    
    testBookContents = loadBook(testBook0)
    Analyzer.analyzeBook(testBookContents)
    
    testBookContents = loadBook(testBook1)
    Analyzer.analyzeBook(testBookContents)
    
    testBookContents = loadBook(testBook2)
    Analyzer.analyzeBook(testBookContents)
    
    testBookContents = loadBook(testBook3)
    Analyzer.analyzeBook(testBookContents)
    #testBookContents = "".join(nltk.corpus.gutenberg.words('austen-persuasion.txt'))
    
    
    #===========================================================================
    # testBookContents = "".join(nltk.corpus.gutenberg.words('austen-sense.txt'))
    # Analyzer.analyzeBook(testBookContents)
    #===========================================================================
     
    #===========================================================================
    # testBookContents = "".join(nltk.corpus.gutenberg.words('melville-moby_dick.txt'))
    # Analyzer.analyzeBook(testBookContents)
    #===========================================================================
    
    #for elem in nltk.corpus.gutenberg.fileids():
    #    print(elem)
        
    #print(nltk.corpus.gutenberg.words('shakespeare-macbeth.txt'))
    
    #print(nltk.book.text1.count('whale'))
    
    
    #print(nltk.book)
    
    
    
    
    
    
    
    
    
    
    
    
    
def iterateThroughAllBooks(locationOfBooks):
    for subdir, dirs, files in os.walk(locationOfBooks):
        for file in files:
            if ".txt" in file:
                fileLocation = subdir +"/" + file
                #print(subdir + "/" + file)
                print("parsing " + file)
                removeGutenbergFromBook(fileLocation)
                
    print("percent" + str(booksParsed/4348))
        

def removeGutenbergFromBook(bookLocation):
    #preGutenRegex = r'^([\s\S]*?\*\*\* START OF THIS PROJECT GUTENBERG.*\n)'
    preGutenRegex = re.compile(r'((^[\s\S]*?\*\*\*.*?START OF.*? PROJECT GUTENBERG.*\n)|(^[\s\S]*?END.*?THE SMALL PRINT.*\n)|(^[\s\S]*?SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP)|(^[\s\S]*?@\w+(\.net)|(\.hotmail)|(\.gmail)|(.\com)))', re.IGNORECASE)
    postGutenRegex = re.compile(r'(End.*?Project Gutenberg[\s\S]*?)$', re.IGNORECASE)
    #preGutenStartRegex = r'*** START OF THIS PROJECT GUTENBERG'
    
    global booksParsed
    bookContent = loadBook(bookLocation)
    if bookContent == "" or "Gutenberg" not in bookContent:
        if bookContent != "":
            booksParsed+=1
        return
    
    preLength = len(bookContent)   
    bookContent = re.sub(preGutenRegex, '', bookContent)
    middleLength = len(bookContent)
    bookContent = re.sub(postGutenRegex, '', bookContent)
    endLength = len(bookContent)
    bookContent = bookContent.strip()
    
    if preLength == middleLength:
        print ("unable to determine prefix")
    elif middleLength == endLength:
        print ("unable to determine postfix")
    else:
        #print (bookContent)
        booksParsed+=1
        with open(bookLocation, 'w', encoding ="utf8") as oFile:
            oFile.write(bookContent)
    
    
    
    #print(bookContent)
    
    #===========================================================================
    # bookContent = loadBook(bookLocation)
    # preGutenIndex = bookContent.find(preGutenStart) + len(preGutenStart)
    # print(preGutenIndex)
    # bookContent = bookContent[preGutenIndex:]
    # print(bookContent)

def loadBook(bookLocation):
    with open(bookLocation, encoding ="utf8") as iFile:
        try:    
            bookContent = iFile.read()
        except UnicodeDecodeError:
            print("could not decode")
            return ""
        
        
        
    return bookContent
 

     
        

main()