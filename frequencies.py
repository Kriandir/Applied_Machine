def frequencies(train, test):

#     split dataset into ham and spam emails
    hamdata = train[train.spam == 0]
    spamdata = train[train.spam == 1]
      
# get words in test data
    wordstest = dict()
    for line in test['text']:
        words = line.split()
        for word in words:
            wordstest[word] = wordstest.setdefault(word, 0)
    
    frequencyham = word_frequency(hamdata['text'], wordstest)
    print(frequencyham[1])
    frequencyspam = word_frequency(spamdata['text'], wordstest)
    print(frequencyspam[1])
    frequency = word_frequency(train['text'], wordstest)
    print(frequency[1]) 