from sklearn import tree





def classify(data, predData):
    
    #===========================================================================
    # X = [[0, 0], [1, 1], [2,2]]
    # Y = [0, 3, 5]
    # clf = tree.DecisionTreeClassifier()
    # clf = clf.fit(X, Y)
    # 
    # print("classified")
    # 
    # pred = clf.predict([2.,2.])
    # print(pred)
    #===========================================================================
    
    bookData = []
    bookAuthors = []
    
    for key in data:
        bookAuthors.append(key)
        bookData.append(data[key])
        
    
    decisionTree = tree.DecisionTreeClassifier()
    decisionTree = decisionTree.fit(bookData, bookAuthors)
    
    prediction = decisionTree.predict(predData)
    
    print(prediction)