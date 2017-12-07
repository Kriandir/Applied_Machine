def word_frequency_mail(mail, dataset):
    datasetwords = dict.copy(dataset)
    
    for word in mail:
        if word in datasetwords:
            datasetwords[word] += 1
            
    word_freq = [(word,freq) for word,freq in datasetwords.items()]
    return word_freq