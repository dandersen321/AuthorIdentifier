import Classifier
import GetBooks
import random

def splitBooksIntoTrainingAndTestingSet(books):
    trainingPercent = 0.80
    randomBooks = books[:]
    random.shuffle(randomBooks)
    trainingEndIndex = int(len(randomBooks) * trainingPercent)
    
    trainingList = randomBooks[:trainingEndIndex]
    testingList = randomBooks[trainingEndIndex:]
    
    return trainingList, testingList
    
    


def main():
    
    books = GetBooks.getBooks()    
    
    
    
        
    trainingList, testingList = splitBooksIntoTrainingAndTestingSet(books)
    
    Classifier.train(trainingList)
    
    print("\nclassifier accuracy: " + str(Classifier.test(testingList)))
    print("\nnumber of books used: " + str(len(books)))

main()