import Classifier
import GetBooks
import random
#import NerualNetworkClassifier

def splitBooksIntoTrainingAndTestingSet(books):
    trainingPercent = 0.80    
    randomBooks = books[:]
    random.shuffle(randomBooks)
    
    initTrainingAuthors = {}
    trainingList = []
    
    for book in randomBooks:
        if book.author not in initTrainingAuthors:
            initTrainingAuthors[book.author] = book.title
    
    
    restOfBooks = []   
    for book in randomBooks:
        if initTrainingAuthors[book.author] == book.title:
            trainingList.append(book)
            continue
        restOfBooks.append(book)
        
    
    trainingEndIndex = int(len(randomBooks) * trainingPercent - len(initTrainingAuthors)) 
    trainingList += restOfBooks[:trainingEndIndex]
    testingList = restOfBooks[trainingEndIndex:]  
    
    x=2
    y = 0
    for book in testingList:
        found = False
        for trainingBook in trainingList:
            if book.author == trainingBook.author:
                found = True
                break
             
        if found == False:
            print(x/y)
            
    trainingList.sort(key=lambda x: x.author )
    testingList.sort(key=lambda x: x.author)

     
    return trainingList, testingList
        
def runOneTrial(books):
    trainingList, testingList = splitBooksIntoTrainingAndTestingSet(books)
    Classifier.train(trainingList)
    
    accuracy = Classifier.test(testingList)
    
    print("\nclassifier accuracy: " + str(accuracy))
    print("\nnumber of books used: " + str( len(books)))
    
    return accuracy

def runOneSimulation(books):
    numberOfTrials = 10
    totalAccuracy = 0
    for i in range(0, numberOfTrials):
        totalAccuracy += runOneTrial(books)
        
    averageAccuracy = totalAccuracy / numberOfTrials
    
    print("average accuracy: " + str(averageAccuracy))
    return averageAccuracy
    
def singleParameters(books):
    allDataKeys = list(books[0].data.keys())
     
    print(allDataKeys)
    random.shuffle(allDataKeys)
    print(allDataKeys)
     
     
    currentDataKeys = []
    for book in books:
        book.setDataKeys(currentDataKeys)
     
    bestAccuracy = 0
     
    with open("singleParams.txt", 'w+') as oFile:
        for key in allDataKeys:
             
            currentDataKeys = [key]
            print("testing with currentDataKeys: ")
            print(currentDataKeys)
            for book in books:
                book.setDataKeys(currentDataKeys)
            accuracy = runOneSimulation(books)
            if accuracy < bestAccuracy:
                print("bad key: " + key)
                currentDataKeys.remove(key)
            else:
                bestAccuracy = accuracy
                print("good key: " + key)
                print("new best accuracy: " + str(bestAccuracy))
                 
            oFile.write(key + "\t" + str(accuracy))
            oFile.write('\n')
                 
         
        print(currentDataKeys)    
        print("best Accuracy: " + str(bestAccuracy))
         
        print("all: ")
        print(allDataKeys)
        
def weedForParameters(books):
    allDataKeys = list(books[0].data.keys())
     
    print(allDataKeys)
    random.shuffle(allDataKeys)
    print(allDataKeys)
     
    currentDataKeys = []
    for book in books:
        book.setDataKeys(currentDataKeys)
     
    bestAccuracy = 0
     
    with open("weedingParams.txt", 'w+') as oFile:
        for key in allDataKeys:
            currentDataKeys.append(key)
            print("testing with currentDataKeys: ")
            print(currentDataKeys)
            for book in books:
                book.setDataKeys(currentDataKeys)
            accuracy = runOneSimulation(books)
            if accuracy < bestAccuracy:
                print("bad key: " + key)
                currentDataKeys.remove(key)
            else:
                bestAccuracy = accuracy
                print("good key: " + key)
                print("new best accuracy: " + str(bestAccuracy))
                 
            oFile.write(key + "\t" + str(accuracy))
            oFile.write('\n')
                 
         
        print(currentDataKeys)    
        print("best Accuracy: " + str(bestAccuracy))         
        print("all: ")
        print(allDataKeys)



def testAddingParameters(books):
    allDataKeys = list(books[0].data.keys())
    
    print(allDataKeys)
    random.shuffle(allDataKeys)
    print(allDataKeys)
    
    currentDataKeys = []
    for book in books:
        book.setDataKeys(currentDataKeys)
    
    with open("addingParams.txt", 'w+') as oFile:
        for key in allDataKeys:
            #if key == startingDataKey:
            #    continue
            
            currentDataKeys.append(key)
            #currentDataKeys.append(key)
            print("testing with currentDataKeys: ")
            print(currentDataKeys)
            for book in books:
                book.setDataKeys(currentDataKeys)
            accuracy = runOneSimulation(books)
                
            oFile.write(key + "\t" + str(accuracy))
            oFile.write('\n')
            print(key + "\t" + str(accuracy))
        
        print("all: ")
        print(allDataKeys)
        
    
def runWithMinBooksChanging():
    with open("minBooks.txt", "w+") as oFile:
        for i in range (2, 21):
            books = GetBooks.getBooks(reParse = False, minNumberOfBooksRequired = i, numberOfAuthorsToUse = 50)
            average = runOneSimulation(books)
            print("on" + str(i))
            oFile.write(str(i) + "\t" + str(average))
            oFile.write('\n')
            
def runWithNumberOfAuthorsChanging():
    with open("authorsChanging.txt", "w+") as oFile:
        for i in range (20, 320, 10):
            books = GetBooks.getBooks(reParse = False, minNumberOfBooksRequired = 3, numberOfAuthorsToUse = i)
            average = runOneSimulation(books)
            print("on" + str(i))
            oFile.write(str(i) + "\t" + str(average))
            oFile.write('\n')
         
def demo():
    books = GetBooks.getBooks(reParse = False, minNumberOfBooksRequired = 3, numberOfAuthorsToUse = 100)
    runOneSimulation(books)
    
     
def main():
    
    demo()
    #runWithMinBooksChanging()
    #runWithNumberOfAuthorsChanging()
    
    #books = GetBooks.getBooks(reParse = False, minNumberOfBooksRequired = 3, numberOfAuthorsToUse = 500)    
    #weedForParameters(books)
    #testAddingParameters(books)
    #singleParameters(books)
    
    
    
    #===========================================================================
    # dataKeys = ['awl', '-', 'this', 'averageParagraphLength', 'awps', 'must', 'and', 'since', 'if', '--', 'uppercaseFraction', 'whitespaceFraction', 'numberOfWords', ';', 'bigraph-lc', 'however', 'apostrophesPerWord', '!', ':']
    # for book in books:
    #         book.setDataKeys(dataKeys)
    #===========================================================================
    
    #runOneSimulation(books)
        
    
    
    #Classifier.outputImageToFile()

main()