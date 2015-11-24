import Classifier
import GetBooks
import random
#import NerualNetworkClassifier

def splitBooksIntoTrainingAndTestingSet(books):
    trainingPercent = 0.80
    #===========================================================================
    # randomBooks = books[:]
    # random.shuffle(randomBooks)
    # trainingEndIndex = int(len(randomBooks) * trainingPercent)
    # 
    # trainingList = randomBooks[:trainingEndIndex]
    # testingList = randomBooks[trainingEndIndex:]
    # 
    # return trainingList, testingList
    #===========================================================================
    
    randomBooks = books[:]
    random.shuffle(randomBooks)
    
    initTrainingAuthors = {}
    trainingList = []
    testingList = []
    
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
                #print("training ")
                break
             
        if found == False:
            print(x/y)
            
    #newlist = sorted(ut, key=lambda x: x.count, reverse=True)
    trainingList.sort(key=lambda x: x.author )
    testingList.sort(key=lambda x: x.author)
     
    #===========================================================================
    # print(len(trainingList))
    # print(len(testingList))
    # 
    # for book in trainingList:
    #     print("training: " + book.author + "-" + book.title)
    #     
    # for book in testingList:
    #     print("testing: " + book.author + "-" + book.title)
    #===========================================================================
     
     
    #print(x/y)
     
    return trainingList, testingList
        
            
    
    #===========================================================================
    # 
    # numberOfBooksNeededToTest = (1-trainingPercent) * len(books)
    # 
    # while len(testingList) <numberOfBooksNeededToTest:
    #     for book in books:
    #         if book.author not in trainingAuthors:
    #             trainingList.append(book)
    #             trainingAuthors[book.author] = True
    # 
    # 
    #===========================================================================
def runOneTrial(books):
    trainingList, testingList = splitBooksIntoTrainingAndTestingSet(books)
    Classifier.train(trainingList)
    #NerualNetworkClassifier.train(trainingList)
    
    accuracy = Classifier.test(testingList)
    
    print("\nclassifier accuracy: " + str(accuracy))
    #print("\nclassifier accuracy: " + str(NerualNetworkClassifier.test(testingList)))
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
    
def weedForParameters(books):
    allDataKeys = list(books[0].data.keys())
    
    print(allDataKeys)
    random.shuffle(allDataKeys)
    print(allDataKeys)
    
    #startingDataKey = allDataKeys[0]
    
    currentDataKeys = []
    #currentDataKeys = [ startingDataKey]
    for book in books:
        book.setDataKeys(currentDataKeys)
    
    #bestAccuracy = runOneSimulation(books)
    bestAccuracy = 0
    
    #with open("weedingParams.txt", 'w+') as oFile:
    with open("singleParams.txt", 'w+') as oFile:
        for key in allDataKeys:
            #if key == startingDataKey:
            #    continue
            
            currentDataKeys = [key]
            #currentDataKeys.append(key)
            print("testing with currentDataKeys: ")
            print(currentDataKeys)
            for book in books:
                book.setDataKeys(currentDataKeys)
            accuracy = runOneSimulation(books)
            if accuracy < bestAccuracy:
                print("bad key: " + key)
                #===============================================================
                # oFile.write("bad key: " + key)
                # oFile.write('\n')
                # oFile.write("best accuracy: " + str(bestAccuracy))
                # oFile.write('\n')
                #===============================================================
                currentDataKeys.remove(key)
            else:
                bestAccuracy = accuracy
                print("good key: " + key)
                print("new best accuracy: " + str(bestAccuracy))
                #===============================================================
                # oFile.write("good key: " + key)
                # oFile.write('\n')
                # oFile.write("new best accuracy: " + str(bestAccuracy))
                # oFile.write('\n')
                #===============================================================
                
            oFile.write(key + "\t" + str(accuracy))
            oFile.write('\n')
                
        
        print(currentDataKeys)    
        print("best Accuracy: " + str(bestAccuracy))
        #=======================================================================
        # oFile.write(str(currentDataKeys))
        # oFile.write('\n')    
        # oFile.write("best Accuracy: " + str(bestAccuracy))
        #=======================================================================
        #oFile.write('\n')
        
        print("all: ")
        print(allDataKeys)
        
    
    
    
def main():
    
    books = GetBooks.getBooks(reParse = False)    
    weedForParameters(books)
    #===========================================================================
    # dataKeys = ['awl', '-', 'this', 'averageParagraphLength', 'awps', 'must', 'and', 'since', 'if', '--', 'uppercaseFraction', 'whitespaceFraction', 'numberOfWords', ';', 'bigraph-lc', 'however', 'apostrophesPerWord', '!', ':']
    # for book in books:
    #         book.setDataKeys(dataKeys)
    #===========================================================================
    
    #runOneSimulation(books)
        
    
    
    #Classifier.outputImageToFile()

main()