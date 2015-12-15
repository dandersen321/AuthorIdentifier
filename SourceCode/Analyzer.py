import nltk;
import heapq;
import collections
import matplotlib.pyplot as plotter
#from curses.ascii import isupper
from SourceCode.bookCleaner import bookCount

#see http://www2.tcs.ifi.lmu.de/~ramyaa/publications/stylometry.pdf
#http://cs229.stanford.edu/proj2012/BarryLuna-StylometryforOnlineForums.pdf
  
def analyzeBook(bookContent):
    #bookContent.count('river')
    
    wordAndPuncContent = nltk.word_tokenize(bookContent)
    wordContent = [w.lower() for w in wordAndPuncContent if w.isalpha() and len(w) > 1] #and len(w) > 3'
    sentences = nltk.sent_tokenize(bookContent)
    
    wordCounts = nltk.FreqDist(wordContent)
    
    awl = averageWordLength(wordAndPuncContent)
    awps = averageWordsPerSentence(sentences, wordContent)
    #standardDeviationOfSentenceLength = standardDeviation()
    averageParagraphLength = getAverageParagraphLength(bookContent, wordContent)
    apostrophesPerWord = getApostrophesPerWord(wordAndPuncContent)
    uppercaseFraction = getUppercaseFraction(wordAndPuncContent)
    numberOfWords = len(wordContent)
    whitespaceFraction = getWhiteSpaceFraction(bookContent)
    digitFraction = getDigitFraction(bookContent)
    
    bigraphsToTest = ['lc', 'co', 'me', 'we']
    frequencyOfBigraphs = getFrequencyOfBigraphs(bigraphsToTest, wordContent)
    
    wordPerThousand = {
        ",": 0,
        ";": 0,
        '"': 0,
        '!': 0,
        ':': 0,
        '-': 0,
        '--': 0,
        'and': 0,
        'but': 0,
        'however': 0,
        'if': 0,
        'that': 0,
        'more': 0,
        'must': 0,
        'might': 0,
        'this': 0,
        'very': 0,
        'since': 0,
        'because': 0
                 }
     
    countWordOccurancePerThousand(wordAndPuncContent, wordPerThousand)
    
    dataParameters = wordPerThousand
    dataParameters['awl'] = awl
    dataParameters['awps'] = awps
    dataParameters['averageParagraphLength'] = averageParagraphLength
    dataParameters['apostrophesPerWord'] = apostrophesPerWord
    dataParameters['uppercaseFraction'] = uppercaseFraction
    dataParameters['numberOfWords'] = numberOfWords
    dataParameters['whitespaceFraction'] = whitespaceFraction
    dataParameters['digitFraction'] = digitFraction
    for biograph in frequencyOfBigraphs:
        dataParameters[biograph] = frequencyOfBigraphs[biograph]
        
    for param in dataParameters:
        dataParameters[param] = round(dataParameters[param], 5)
    
    
    return dataParameters

def mostCommonNGrams(wordContent, numberOfTopNGrams):
    #split on spaces, don't allow empty string in tuples
    
    #textNGrams = nltk.ngrams(filter(bool,bookContent.lower().replace("\n", "").split(" ")), 3)
    textNGrams = nltk.ngrams(wordContent, 3)
    nGramsFreq = nltk.FreqDist(textNGrams)    
    topNGrams = []
    
    for words, freq in nGramsFreq.items():
        if len(topNGrams) < numberOfTopNGrams or freq > topNGrams[0][0]:
            if len(topNGrams) == numberOfTopNGrams:
                heapq.heappop(topNGrams)
            heapq.heappush(topNGrams, (freq, words))
    
    return sorted(topNGrams, reverse = True)



def countWordOccurancePerThousand(wordContent, words):
    counter = collections.Counter(wordContent)
    #print(len(wordContent))
    for word in words:
        #print(counter[word])
        #print(counter[word] / len(words))
        #words[word] = counter[word] / len(wordContent) * 1000 / (len(wordContent))
        words[word] = round(counter[word]/len(wordContent) * 1000)
        
    return words

def averageWordLength(wordContent):
    totalLength = 0
    for word in wordContent:
        totalLength += len(word)
    return totalLength / len(wordContent)

def averageWordsPerSentence(sentences, wordContent):
    return len(wordContent) / len(sentences)

def getAverageParagraphLength(bookContent, wordContent):
    paragraphs = bookContent.split('\n')
    return len(wordContent)/len(paragraphs)

def getApostrophesPerWord(wordAndPuncContent):
    numberOfApostrophes = 0

    for word in wordAndPuncContent:
        if "'" in word:
            numberOfApostrophes+=1
    
    return numberOfApostrophes / len (wordAndPuncContent)

def getUppercaseFraction(wordAndPuncContent):
    numberOfUpperCases = 0
    numberOfWords = len(wordAndPuncContent)
    for word in wordAndPuncContent:
        for character in word:
            if character.isupper():
                numberOfUpperCases+=1
                continue
    
    return numberOfUpperCases / numberOfWords

    
def getWhiteSpaceFraction(bookCount):    
    numberOfWhiteSpaces = 0
    numberOfCharacters = len(bookCount)
    for character in bookCount:
        if character == ' ':
            numberOfWhiteSpaces+=1
    
    return numberOfWhiteSpaces / numberOfCharacters

def getDigitFraction(bookCount):
    numberOfDigits = 0
    numberOfCharacters = len(bookCount)
    for character in bookCount:
        if character.isdigit():
            numberOfDigits+=1
    
    return numberOfDigits / numberOfCharacters

def getFrequencyOfBigraphs(bigraphsToTest, wordContent):
    bigraphs = {}
    for bigraph in bigraphsToTest:
        bigraphs["bigraph-" + bigraph]= 0
    numberOfWords = len(wordContent)
    
    for word in wordContent:
        #print(bigraphsToTest)
        for bigraph in bigraphsToTest:
            #print("biograph: " + bigraph + " word: " + word)
            if bigraph in word:
                bigraphs["bigraph-" + bigraph] +=1
                
    
    for bigraph in bigraphs:
        bigraphs[bigraph] = bigraphs[bigraph]/numberOfWords * 100
        
    return bigraphs
 
def __init__():
    print("anayzlFileinit")
    
def testLoadBook():
    testBookContent = None
    with open('C:/Users/Dylan/Desktop/AI Project Books/Gutenberg 3/testBook.txt', 'r') as iFile:
        testBookContent = iFile.read()
    
    print(testBookContent)    
        
    testBookAnalysis = analyzeBook(testBookContent)
    
    print(testBookAnalysis)
    