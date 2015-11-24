from random import randint

class Book:
    location = ""
    author = ""
    title = ""
    content = ""
    authorCount = 1
    data = {}
    dataKeysToUse = None
    
    def setDataKeys(self, dataKeysToUse):
        self.dataKeysToUse = dataKeysToUse
        
    
    def getDataValues(self):
        dataValues = []
        count = 0 
        for key in sorted(self.data):
            if self.dataKeysToUse is not None and key not in self.dataKeysToUse:
                continue
            #===================================================================
            # if key == "digitFraction" or key == "bigraph-lc" or key == "bigraph-we" or key == "whitespaceFraction" or key == "bigraph-co" or key == "bigraph-me":
            #     continue
            #===================================================================
                #self.data[key]*=100
            
            
            
            #if randint(0,1) == 0:
            #    continue
            #===================================================================
            # count+=1
            # if count > 20:
            #     continue
            #===================================================================
            dataValues.append(self.data[key])
             
        return dataValues
    
    
    def __init__(self, location, author, title, data):
        self.location = location
        self.author = author
        self.title = title
        self.data = data
        #self.content = content