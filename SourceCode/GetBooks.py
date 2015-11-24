from Book import Book
import os
import Analyzer
import json
import zipfile
import random

#locationOfBooksInfo = "C:/Users/Dylan/Desktop/AI Project Books/2003/Gutenberg 2003/authorsParsed.txt"
#locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/2003/Gutenberg 2003/books.txt"

locationOfBooksInfo = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/parsedBooks.txt"
locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/books.txt"

def getBooks(reParse = False, minNumberOfBooksRequired = 2):
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
        #print(bookLine)
        title = bookLine[0].strip()
        author = bookLine[1].strip()
        location = bookLine[2].strip()
        #bookLine[3] = bookLine[3][1:-2]
        #print(bookLine[3])
        #data = [float(x) for x in bookLine[3].split(',')]
        #print(bookLine[3])
        print("loading: " + title)
        data = json.loads(bookLine[3])
        
        if title in titlesUsed or author == 'Unknown' or author.strip() == '':
            continue
        
        newBook = Book(location, author, title, data)
        titlesUsed[title] = True
        
        if len(authorCount) >= 600 and author not in authorCount:
            continue
        
        books.append(newBook)
        
        if author in authorCount:
            authorCount[author]+=1
        else:
            authorCount[author] = 1
            

        
    
    #===========================================================================
    # for book in books:
    #     authorCount = getAuthorCount(books, book.author)
    #     book.authorCount = authorCount
    #     print("reading book " + book.title)
    #===========================================================================
    
    print("author count: " + str(len(authorCount)))
    
    #minNumberOfBooksRequired = 2
    
    booksToUse = [book for book in books if authorCount[book.author] >= minNumberOfBooksRequired]
        
    #booksToUse = [book for book in books if book.authorCount >= minNumberOfBooksRequired]
        
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
                    #print("unzipping")
                    #print(zipFolder)
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
            #print(data)
        except Exception as e:
            print(e)
            #print("exception raised")
            continue
        newBook = Book(location, author, title, data)
        books.append(newBook)
        print(newBook.title + " was parsed")
        print("percent finished: " + str(booksParsedCount/bookLength))
        
        #if booksParsedCount > 100:
        #    break
        
    with open(locationOfBooks, 'w', encoding ="utf8") as oFile:
        #json.dump(books, oFile)
        for book in books:
            print(bookToFileFormat(book))
            oFile.write(bookToFileFormat(book))
    
    #for book in books:
    #    print(book.author)
        
    #return books
def bookToFileFormat(book):
    #bookList = [book.title, book.author, book.location, book.data]
    #bookListString = book.title + "@" + book.author + "@" + book.location + "@" + str(book.data) + "\n"
    bookListString = book.title + "@" + book.author + "@" + book.location + "@" + json.dumps(book.data) + "\n"
    #bookListSeperated = "@".join(bookList)
    print(bookListString)
    return bookListString