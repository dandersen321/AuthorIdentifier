import nltk;
import heapq;
import collections
import matplotlib.pyplot as plotter

  
def analyzeBook(bookContent):
    bookContent.count('river')
    
    wordAndPuncContent = nltk.word_tokenize(bookContent)
    wordContent = [w.lower() for w in wordAndPuncContent if w.isalpha() and len(w) > 3] #and len(w) > 3'
    sentences = nltk.sent_tokenize(bookContent)
    
    wordCounts = nltk.FreqDist(wordContent)
    
    
    
    #return
     
    print("awl: " + str(averageWordLength(wordAndPuncContent)))
    print("awps: " + str(averageWordsPerSentence(sentences, wordContent)))
     
     
    wordCounts.plot(20)
     
    print(wordCounts)
    
    #x = input()
    
    wordCount = {
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
        'very': 0
                 }
     
    countWordOccurancePerThousand(wordAndPuncContent, wordCount)
     
    for word in wordCount:
        print(word + " " + str(wordCount[word]))
         
    return
    
        
    commonNGrams = mostCommonNGrams(wordContent, 20)
    #print(commonNGrams)
    #print("most common")
    for freq, word in commonNGrams:
        print(str(freq) + ": " + str(word))
        
    
    #for k, v in freq.items():
    #    print(k, v)

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
    
 
def __init__():
    print("anayzlFileinit")        

#===============================================================================
# import nltk;
# import heapq;
# 
# 
# def analyzeBook(bookContent):
#     
#     freqDist = nltk.probability.FreqDist(bookContent)
#     testFreq = freqDist['the'] * 1000 / freqDist.N()
#     #print(testFreq)
#     #return
#         
#     commonNGrams = mostCommonNGrams(bookContent, 50)
#     #print(commonNGrams)
#     #print("most common")
#     for freq, word in commonNGrams:
#         print(str(freq) + ": " + str(word))
#         
#     
#     #for k, v in freq.items():
#     #    print(k, v)
# 
# def mostCommonNGrams(bookContent, numberOfTopNGrams):
#     #split on spaces, don't allow empty string in tuples
#     textNGrams = nltk.ngrams(filter(bool,bookContent.lower().split(" ")), 3)
#     nGramsFreq = nltk.FreqDist(textNGrams)    
#     topNGrams = []
#     
#     for words, freq in nGramsFreq.items():
#         if len(topNGrams) < numberOfTopNGrams or freq > topNGrams[0][0]:
#             if len(topNGrams) == numberOfTopNGrams:
#                 heapq.heappop(topNGrams)
#             heapq.heappush(topNGrams, (freq, words))
#     
#     return sorted(topNGrams, reverse = True)
# 
#      
#===============================================================================