import re

def main():
    
    allIndexesLocation = "C:/Users/Dylan/Desktop/tmp/Gutenberg 3/indexbig.htm"
    endLocation = "C:/Users/Dylan/Desktop/tmp/Gutenberg 3/parsedBooks.txt"
    fileText = ""
    print("start")
    with open(    allIndexesLocation, encoding ="utf8") as iFile:   
        textLines = iFile.readlines()
            #print("loaded " + bookLocation)
    
    titleAndAuthor = r'.*?Title:</font>\s*(.*?)\s*<.*?Author:</font>\s*(.*?)<'
    locationRegex = r'.*?<a href="(.*?)">.*?'
    
    books = []
    currentBook = None
    
    for line in textLines:
        lineMatches = re.match(titleAndAuthor, line)
        try:
            print(line)
            if lineMatches:
                newBook = myBook()
                newBook.title = lineMatches.group(1)
                newBook.author = lineMatches.group(2)
                currentBook = newBook
            elif currentBook != None:
                locationMatches = re.match(locationRegex, line)
                #print(line)
                #print(locationMatches)
                currentBook.location = locationMatches.group(1)
                books.append(currentBook)
                #print(currentBook.title + " was added")
                currentBook = None
                #print(lineMatches.group(1))
            #print(line)
        except Exception:
            currentBook = None
            
    with open(endLocation, 'w') as oFile:
        for book in books:
            book.location = "C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/" + book.location.replace(".zip", ".txt")
            line = book.title + "@" + book.author + "@" + book.location + "\n"
            if not all(ord(c) < 128 for c in line):
                print("not ascii: " + line)
                continue
            #print(book.title + " " + book.author + " " + book.location)
            oFile.write(line)
     
class myBook:
    title = ""
    author = ""
    location = ""
    
    
main()