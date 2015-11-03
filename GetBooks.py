from Book import Book
import os
import Analyzer

#locationOfBooksInfo = "C:/Users/Dylan/Desktop/AI Project Books/2003/Gutenberg 2003/authorsParsed.txt"
#locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/2003/Gutenberg 2003/books.txt"

locationOfBooksInfo = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/parsedBooks.txt"
locationOfBooks = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/books.txt"

def getBooks(reParse = False):
    books = None
    
    if not os.path.isfile(locationOfBooks) or reParse == True:
        parseBooks()
    
    
    with open(locationOfBooks, 'r') as iFile:
        booksAsFileFormat = iFile.readlines()
    
    books = []
    for bookElem in booksAsFileFormat:
        bookLine = bookElem.split('@')
        title = bookLine[0].strip()
        author = bookLine[1].strip()
        location = bookLine[2].strip()
        bookLine[3] = bookLine[3][1:-2]
        #print(bookLine[3])
        data = [float(x) for x in bookLine[3].split(',')]
        
        newBook = Book(location, author, title, data)
        books.append(newBook)
    
    for book in books:
        authorCount = getAuthorCount(books, book.author)
        book.authorCount = authorCount
        
    booksToUse = [book for book in books if book.authorCount > 3]
        
    return booksToUse
    
def getAuthorCount(books, author):
    authorCount = 0
    for book in books:
        if book.author == author:
            authorCount+=1
    
    return authorCount

def parseBooks():
    with open(locationOfBooksInfo, encoding ="utf8") as iFile:
        booksInfo = iFile.readlines()
    
    #booksInfo = booksInfo[:10]
    
    books = []    
    for book in booksInfo:
        rowData = book.split("@")
        title = rowData[0].strip()
        author = rowData[1].strip()
        location = rowData[2].strip()
        content = ""
        if(not os.path.isfile(location) or author== "Anonymous" or author =="Various" or ".txt" not in location):
            #print(location + " is not found")
            continue
        with open(location, encoding = "utf8") as iFile:
            try:
                content = iFile.read()
                #print("read " + location)
            except UnicodeDecodeError:
                continue
        data = {}
        try:    
            data = Analyzer.analyzeBook(content)
        except Exception:
            continue
        newBook = Book(location, author, title, data)
        books.append(newBook)
        print(newBook.title + " was parsed")
        
    with open(locationOfBooks, 'w', encoding ="utf8") as oFile:
        for book in books:
            print(bookToFileFormat(book))
            oFile.write(bookToFileFormat(book))
    
    #for book in books:
    #    print(book.author)
        
    #return books
def bookToFileFormat(book):
    #bookList = [book.title, book.author, book.location, book.data]
    bookListString = book.title + "@" + book.author + "@" + book.location + "@" + str(book.data) + "\n"
    #bookListSeperated = "@".join(bookList)
    print(bookListString)
    return bookListString