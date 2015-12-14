from sklearn import tree
#import graphviz as gv
#import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt

decisionTree = None

def train(books):
    print("training . . .")
    global decisionTree
    decisionTree = tree.DecisionTreeClassifier()
    
    bookData = []
    bookAuthors = []
    for book in books:
        bookData.append(book.getDataValues())
        bookAuthors.append(book.author)
    
    decisionTree = decisionTree.fit(bookData, bookAuthors)
    
def predict(book):
    
    prediction = decisionTree.predict(book.getDataValues())
    #prob = decisionTree.predict_proba(book.getDataValues())
    #prob = decisionTree.score(book.getDataValues(), prediction[0])
    #print(prob)
    return prediction[0]

def test(testingBooks):
    #print("testingBooks")
    #print(testingBooks)
    totalBooks = len(testingBooks)
    booksCorrect = 0
    for book in testingBooks:
        authorPrediction = predict(book)
        if authorPrediction == book.author:
            booksCorrect += 1
        #else:
            #given = "given: " book.author
            #print( ("given: " + book.author).ljust(60, ' ') + " predicted: " + str(authorPrediction))
            #print("author: " + book.author + " predicted: " + authorPrediction)
            
    return round(booksCorrect/totalBooks * 100, 2)

def outputImageToFile():
    fileLocation = "C:/Users/Dylan/Desktop/AI Project Books/classifier.dot"
     
    tree.export_graphviz(decisionTree, out_file=fileLocation)


#===============================================================================
# def train(data, predData):
#     
#     #===========================================================================
#     # X = [[0, 0], [1, 1], [2,2]]
#     # Y = [0, 3, 5]
#     # clf = tree.DecisionTreeClassifier()
#     # clf = clf.fit(X, Y)
#     # 
#     # print("classified")
#     # 
#     # pred = clf.predict([2.,2.])
#     # print(pred)
#     #===========================================================================
#     
#     bookData = []
#     bookAuthors = []
#     
#     for key in data:
#         bookAuthors.append(key)
#         bookData.append(data[key])
#         
#     
#     decisionTree = tree.DecisionTreeClassifier()
#     decisionTree = decisionTree.fit(bookData, bookAuthors)
#     
#     prediction = decisionTree.predict(predData)
#     
#     print(prediction)
#===============================================================================