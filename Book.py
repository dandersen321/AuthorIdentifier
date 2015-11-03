class Book:
    location = ""
    author = ""
    title = ""
    content = ""
    authorCount = 1
    data = {}
    
    
    def __init__(self, location, author, title, data):
        self.location = location
        self.author = author
        self.title = title
        self.data = data
        #self.content = content