import nltk;
import heapq;
import collections
import matplotlib.pyplot as plotter

  
def analyzeBook(bookContent):
    bookContent.count('river')
    
    wordAndPuncContent = nltk.word_tokenize(bookContent)
    wordContent = [w.lower() for w in wordAndPuncContent if w.isalpha() and len(w) > 1] #and len(w) > 3'
    sentences = nltk.sent_tokenize(bookContent)
    
    wordCounts = nltk.FreqDist(wordContent)
    
    
    
    #return
    
    awl = averageWordLength(wordAndPuncContent)
    awps = averageWordsPerSentence(sentences, wordContent)
     
    #print("awl: " + str(awl))
    #print("awps: " + str(awps))
     
     
    #wordCounts.plot(20)
     
    #print(wordCounts)
    
    #x = input()
    
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
        'very': 0
                 }
     
    countWordOccurancePerThousand(wordAndPuncContent, wordPerThousand)
    
    dataParameters = wordPerThousand
    dataParameters['awl'] = awl
    dataParameters['awps'] = awps
    
    data = []
    
    for key in sorted(dataParameters):
        data.append(dataParameters[key])
    
    #===========================================================================
    # for key in sorted(dataParameters):
    #     print("key" + str(key))
    #     print("value " + str(dataParameters[key]))
    #     dataValue = dataParameters[key]
    #     print("dataValue: " + str(dataValue))
    #     data.append(dataValue)
    # 
    # for elem in data:
    #     print("data: " + str(elem))
    #===========================================================================
        
    
     
    #===========================================================================
    # for word in wordPerThousand:
    #     print(word + " " + str(wordPerThousand[word]))
    #===========================================================================
    #print("\n\n")     
    return data
    
        
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