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
    return prediction[0]

def test(testingBooks):
    totalBooks = len(testingBooks)
    booksCorrect = 0
    for book in testingBooks:
        authorPrediction = predict(book)
        if authorPrediction == book.author:
            booksCorrect += 1
            
    return round(booksCorrect/totalBooks * 100, 2)

def outputImageToFile():
    fileLocation = "C:/Users/Dylan/Desktop/AI Project Books/classifier.dot"
     
    tree.export_graphviz(decisionTree, out_file=fileLocation)