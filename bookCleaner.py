import nltk
import heapq
import os
import re
import collections
import math
from main import booksParsed

booksParsed = 0

def main():
    #locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/cache/generated"
    locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/2003/Gutenberg 2003"
    iterateThroughAllBooks(locationOfBooks)

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
    
    bookParsed = False
    
    if preLength == middleLength:
        print ("unable to determine prefix")
    elif middleLength == endLength:
        print ("unable to determine postfix")
    else:
        bookParsed = True
        #print (bookContent)
        booksParsed+=1
        with open(bookLocation, 'w', encoding ="utf8") as oFile:
            oFile.write(bookContent)
    
    if not booksParsed:
        deleteBook(bookLocation)
        #os.remove()
    
    
    #print(bookContent)
    
    #===========================================================================
    # bookContent = loadBook(bookLocation)
    # preGutenIndex = bookContent.find(preGutenStart) + len(preGutenStart)
    # print(preGutenIndex)
    # bookContent = bookContent[preGutenIndex:]
    # print(bookContent)
def deleteBook(bookLocation):
    print("deleting book at: " + bookLocation)

def loadBook(bookLocation):
    with open(bookLocation, encoding ="utf8") as iFile:
        try:    
            bookContent = iFile.read()
            print("loaded " + bookLocation)
        except UnicodeDecodeError:
            print("could not decode")
            deleteBook(bookLocation)
            return ""
        
        
        
    return bookContent
 

     
        

main()