def word_frequency(dataframe, dataset):
    # for w in dataframe.str.lower():
#     create a dataframe of all words
    
    datasetwords = dict.copy(dataset)
    
    for line in dataframe:
        words = line.split()
        for word in words:
            if word in datasetwords:
                datasetwords[word] += 1
    
    word_freq = [(word,freq) for word,freq in datasetwords.items()]
    return word_freq       