from Book import Book
import os
import Analyzer
import json
import zipfile
import random

locationOfBooksInfo = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/parsedBooks.txt"
locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/books.txt"


def getBooks(reParse = False, minNumberOfBooksRequired = 2, numberOfAuthorsToUse = 100):
    books = None
     
    if not os.path.isfile(locationOfBooks) or reParse == True:
        parseBooks()
     
     
    with open(locationOfBooks, 'r') as iFile:
        booksAsFileFormat = iFile.readlines()
         
    titlesUsed = {}
     
    books = []
    authorCount = {}
    random.shuffle(booksAsFileFormat)
    for bookElem in booksAsFileFormat:
         
        bookLine = bookElem.split('@')
        title = bookLine[0].strip()
        author = bookLine[1].strip()
        location = bookLine[2].strip()

        print("loading: " + title)
        data = json.loads(bookLine[3])
         
        if title in titlesUsed or author == 'Unknown' or author.strip() == '':
            continue
         
        newBook = Book(location, author, title, data)
        titlesUsed[title] = True
         
        if len(authorCount) >= numberOfAuthorsToUse and author not in authorCount:
            continue
         
        books.append(newBook)
         
        if author in authorCount:
            authorCount[author]+=1
        else:
            authorCount[author] = 1
             
 
    booksToUse = [book for book in books if authorCount[book.author] >= minNumberOfBooksRequired]
    print("author count: " + str(len(authorCount)))
    print("booksToUse count: " + str(len(booksToUse)))
    
    if len(authorCount) < numberOfAuthorsToUse:
        print("not enough authors used for: authors: " + str(authorCount) + ", minNumBooks: " + str(minNumberOfBooksRequired)) 
        raise Exception("not enough authors")   

    if len(booksToUse) < 100:
        print("not enough authors used for: authors: " + str(authorCount) + ", minNumBooks: " + str(minNumberOfBooksRequired)) 
        raise Exception("not enough authors")
         
    return booksToUse
    
def getAuthorCount(books, author):
    authorCount = 0
    for book in books:
        if book.author == author:
            authorCount+=1
    
    return authorCount

def parseBooks():
    print("starting to parse books")
    booksInfo = []
    with open(locationOfBooksInfo, encoding ="utf8") as iFile:
        booksInfo = iFile.readlines()
    
    #booksInfo = booksInfo[:30]
    booksParsedCount = 0
    bookLength = len(booksInfo)
    books = []    
    for book in booksInfo:
        booksParsedCount+=1
        rowData = book.split("@")
        title = rowData[0].strip()
        author = rowData[1].strip()
        location = rowData[2].strip()
        content = ""
        errorMessage = ""
        print("looking at book" + title + " " + location + " " + author)
        if(not os.path.isfile(location)):
            zipLocation = location[:-3] 
            zipLocation += "zip"
            if os.path.isfile(zipLocation):
                try:
                    zfile = zipfile.ZipFile(zipLocation)
                    zipFolder = zipLocation[:zipLocation.rfind('/')]
                    zfile.extractall(zipFolder)
                except Exception:
                    continue
            if(not os.path.isfile(location)):
                errorMessage += "location not found"
        if author== "Anonymous" or author =="Various":
            errorMessage += "author unknown"
        if ".txt" not in location:
            errorMessage+= "location weird"
        
        if errorMessage is not "":
            print(errorMessage)
            continue
        
        with open(location) as iFile:
            try:
                content = iFile.read()
                #print("read " + location)
            except UnicodeDecodeError as e:
                print("decode error")
                print(e)
                continue
            except Exception as e:
                print(e)
        data = {}
        try:    
            data = Analyzer.analyzeBook(content)
            
            print("anayzled " + title)
        except Exception as e:
            print(e)
            continue
        newBook = Book(location, author, title, data)
        books.append(newBook)
        print(newBook.title + " was parsed")
        print("percent finished: " + str(booksParsedCount/bookLength))
        
    with open(locationOfBooks, 'w', encoding ="utf8") as oFile:
        for book in books:
            print(bookToFileFormat(book))
            oFile.write(bookToFileFormat(book))
    
def bookToFileFormat(book):
    bookListString = book.title + "@" + book.author + "@" + book.location + "@" + json.dumps(book.data) + "\n"
    print(bookListString)
    return bookListString