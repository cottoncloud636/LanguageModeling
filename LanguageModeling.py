from collections import defaultdict
import math
def training_preprocess():
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        training = data.readlines() #read each line into a list

    #pad <s> and </s>
    training = ["<s> " + sentence.lower() + " </s>" for sentence in training]

    
    #split sentence into word. Appears in format of: each sentence in a list, each list was tokennized into words
    training=[sentence.split() for sentence in training] #*********output is ['<s>', 'the', 'service', 'helps', 'children', 'affected', 'by', 'conditions', 'such', 'as', 'autism', 'and', 'down', "'s", 'syndrome', '.', '</s>'], ['<s>', 'or', 'did', 'she', 'hit', 'rock', '-', 'bottom', '?', '</s>'], 
    
    #build a dictionary and check if word appear once or more than once 
    word_dict={}
    for sentence in training:
        for word in sentence:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1

    #for training data, if word appear once, replace the word with <unk>
    training=[[word if word_dict[word]>1 else "<unk>" for word in sentence] for sentence in training]
    #print(training) #********************output is ['<s>', 'the', 'service', 'helps', 'children', 'affected', 'by', 'conditions', 'such', 'as', 'autism', 'and', 'down', "'s", 'syndrome', '.', '</s>'], ['<s>', 'or', 'did', 'she', 'hit', 'rock', '-', 'bottom', '?', '</s>'], 
    #after complete three tasks, join the sentnce back together
    # training = "\n".join([" ".join(sentence) for sentence in training]) #**************output is <s> the hot santa ana winds , which have fanned the flames as they blow in to southern california from the desert , continued to gust up to 65 mph ( 105 kph ) and high wind warnings remained in effect for most of the region until wednesday afternoon . </s>
                                                                                                #<s> some solutions involve controversy . </s>
                                                                                                #<s> palestinian medics identified the dead man as adel <unk> , 23 , a member of the armed wing of hamas , according to agence france - presse . </s>
    
    return training

def training_preprocess_WOSS():
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        trainingWOSS = data.readlines() #read each line into a list

    #pad <s> and </s>
    trainingWOSS = [sentence.lower() + " </s> " for sentence in trainingWOSS]
    
    #split sentence into word
    trainingWOSS=[sentence.split() for sentence in trainingWOSS]
    
    #build a dictionary and check if word appear once or more than once 
    word_dict={}
    for sentence in trainingWOSS:
        for word in sentence:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1

    #for training data, if word appear once, replace the word with <unk>
    trainingWOSS=[[word if word_dict[word]>1 else "<unk>" for word in sentence] for sentence in trainingWOSS]

    #after complete three tasks, join the sentnce back together
    # trainingWOSS = "\n".join([" ".join(sentence) for sentence in trainingWOSS])
    # print(training)
    return trainingWOSS

def test_preprocess():
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        training = data.readlines() #read each line into a list

    with open ("test.txt","r", encoding='UTF8') as data:
        test = data.readlines() #read each line into a list

    #pad <s> and </s>
    training = ["<s> " + sentence.lower() + " </s>" for sentence in training]
    test = ["<s> " + sentence.lower() + " </s>" for sentence in test]

    #split sentence into word
    training=[sentence.split() for sentence in training]
    test=[sentence.split() for sentence in test]
    #build a dictionary and check if word appear once or more than once 
    word_dict={}
    for sentence in training:
        for word in sentence:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1

    #for test data, if the word didn't appear in training data, replace with <unk>  
    test=[[word if word in word_dict else "<unk>" for word in sentence] for sentence in test]
    
    #after complete three tasks, join the sentnce back together
    # test = "\n".join([" ".join(sentence) for sentence in test]) #output is line by line with padding and lowercase
    
    return test

def test_preprocessWOSS():
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        trainingWOSS = data.readlines() #read each line into a list

    with open ("test.txt","r", encoding='UTF8') as data:
        testWOSS = data.readlines() #read each line into a list

    #pad <s> and </s>
    trainingWOSS = [sentence.lower() + " </s> " for sentence in trainingWOSS]
    testWOSS = [sentence.lower() + " </s> " for sentence in testWOSS]

    #split sentence into word
    trainingWOSS=[sentence.split() for sentence in trainingWOSS]
    testWOSS=[sentence.split() for sentence in testWOSS]
    
    #build a dictionary and check if word appear once or more than once 
    word_dict={}
    for sentence in trainingWOSS:
        for word in sentence:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1

    #for test data, if the word didn't appear in training data, replace with <unk>  
    testWOSS=[[word if word in word_dict else "<unk>" for word in sentence] for sentence in testWOSS]

    #after complete three tasks, join the sentnce back together
    # testWOSS = "\n".join([" ".join(sentence) for sentence in testWOSS])
    # print(testWOSS)
    return testWOSS

def unigram(training_result):
    training_result=training_result.split(' ')

    unigram_words={}
    
    #split sentence into each word
    for word in training_result:      
        if word in unigram_words:
            unigram_words[word]+=1
        else:
            unigram_words[word]=1
        

    #count total number of words(aka. total number of values) in the dictionary
    total_count=sum(unigram_words.values()) 

    #calculate unigram MLE
    unigram_MLE={}
    for word, count in unigram_words.items(): #key:word, value: count. key-value pair
        unigram_MLE[word] = count / total_count #unigram is defined as count(Wi)/count(total # of words in corpus)
   
    return unigram_MLE[word]
    # for word, MLE in unigram_MLE.items():
    #     print(f"{word}: {MLE}")
    
def bigram(training_result):
    #a dict to store the total counts of unigram
    unigram_words={}
    #a dict to store the total counts of bigram
    bigram_words={}

    #loop through the entire corpus
    for sentence in training_result:
        for i in range(len(sentence)-1):
            #selects the ith and (i+1)th words to form a bigram
            bigram=sentence[i:i+2]
            bigram_words.setdefault(tuple(bigram),0) 
            bigram_words[tuple(bigram)] += 1
            unigram_words.setdefault(bigram[0],0) #if the first word never seen, set this key's value to 0
                                                #If key is already exist, returns its value.  
            unigram_words[bigram[0]]+=1

    #calculate bigram MLE
    bigram_MLE={}
    for bigram, count in bigram_words.items(): #key:bigram, value: count. key-value pair
        #get the first word in the tuple, so that it can be used to calculate each unigram probability
        previous_word=bigram[0]
        MLE=count / unigram_words[previous_word]

        bigram_MLE[bigram]=MLE
        
    resultList=[]
    for bigram, MLE in bigram_MLE.items():
        resultList.append(MLE)
        #print (f"{bigram[0]} {bigram[1]}: {MLE}")
    
    return resultList

def add_one_bigram(training_result):
    #a dict to store the total counts of unigram
    unigram_words={} #if a key not found, use lambda to create a default value 0
    #a dict to store the total counts of bigram
    bigram_words={}

    #loop through the entire corpus
    # for sentence in training_result:
    for sentence in training_result:
        for i in range(len(sentence)-1):
            #selects the ith and (i+1)th words to form a bigram
            bigram=tuple(sentence[i:i+2])
            if bigram not in bigram_words:
                bigram_words[bigram] = 1
            else:
                bigram_words[bigram] += 1

            # Increment the unigram count
            if sentence[i] not in unigram_words:
                unigram_words[sentence[i]] = 1
            else:
                unigram_words[sentence[i]]+=1

            # Increment the count of the end of sentence token
        if sentence[-1] not in unigram_words:
            unigram_words[sentence[-1]] = 1
        else:
            unigram_words[sentence[-1]] += 1
    #loop through everyword in text file
    # for i in range(len(training_result)-1):

    addone_MLE={}
    #calculate bigram add one smoothing probabilities
    for bigram_addOne, count in bigram_words.items():
        #count of first word in bigram
        count_unigram=unigram_words[bigram_addOne[0]]
        MLE=(count + 1) / (count_unigram + len(unigram_words))

        addone_MLE[bigram_addOne]=MLE

    resultList=[]
    for bigram_addOne, MLE in addone_MLE.items():
        resultList.append(MLE)
        #print (f"{bigram[0]} {bigram[1]}: {MLE}")
    return resultList

    # for bigram_addOne, MLE in addone_MLE.items():
    #     print (f"{bigram_addOne[0]} {bigram_addOne[1]}: {MLE}")


def Question_1(training_result):
    unique_words=set() #use set to store unique words because set can't contain duplicate words

    for sentence in training_result:
        for word in sentence:
            if word !="<s>":
                unique_words.add(word)

    length=len(unique_words)
    print("Question 1. How many word types (unique words) are there in the training corpus?")
    print("There are "+str(length)+ " unique words in the training corpus.")
    print(" ")

def Question_2(training_result):
    # token_dict={}
    # for sentence in training_result:
    #     for word in sentence:
    #         if word in token_dict:
    #             token_dict[word]+=1
    #         else:
    #             token_dict[word]=1
    
    # count=0
    # for key in token_dict:
    #     if key !="<s>":
    #         count+=token_dict[key]
    
    token_count=0
    for sentence in training_result:
        for word in sentence:
            if word != "<s>":
                token_count+=1

    print("Question 2. How many word tokens are there in the training corpus?")
    print("There are "+str(token_count)+ " word tokens in the training corpus.")
    print(" ")

def Question_3():
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        training = data.readlines() #read each line into a list

    with open ("test.txt","r", encoding='UTF8') as data:
        test = data.readlines() #read each line into a list

    #pad <s> and </s>
    training = [sentence.lower() + " </s>" for sentence in training]
    test = [sentence.lower() + " </s>" for sentence in test]

    training=[sentence.split() for sentence in training]
    test=[sentence.split() for sentence in test]
    
    #calculate the unique words appear in test but not in training
    training_unique=set() #use set to store unique words because set can't contain duplicate words
    test_unique=set()

    for sentence in training:
        for word in sentence:
            training_unique.add(word)

    for sentence in test:
        for word in sentence:
            test_unique.add(word)
   
    uniqueWordNotInT_percentage = (len(test_unique-training_unique)/len(test_unique))*100

    #calculate percentage of words in test but not in training without counting <s>
    #build a training dictionary
    training_dict={}
    for sentence in training:
        for word in sentence:
            if word in training_dict:
                training_dict[word]+=1
            else:
                training_dict[word]=1

    test_dict={}
    for sentence in test:
        for word in sentence: #word is the key, which here is each word from test data, while vaule is numerical number
            if word in test_dict:
                test_dict[word]+=1
            else:
                test_dict[word]=1
    
    wordNotInT=0
    for word in test_dict:
        if word not in training_dict:
            wordNotInT+=test_dict[word]
            
    count_total=0
    for sentence in test:
        for word in sentence:
            count_total+=1

    wordNotInT_percentage = (wordNotInT / count_total)*100

    print("Question 3. What percentage of word tokens and word types in the test corpus did not occur in training (before you mapped the unknown words to <unk> in training and test data)?")
    print("There are "+str(uniqueWordNotInT_percentage)+ "%"+" unique words in the test corpus but not in training corpus.")
    print("There are "+str(wordNotInT_percentage)+ "% word tokens in the test corpus but not in training corpus.")
    print(" ")

def Question_4(training_resultWOSS, test_resultWOSS):    
    trainingBigram_counts = defaultdict(int)
    testBigram_counts = defaultdict(int)
    #loop through the entire corpus
    for sentence in training_resultWOSS:
        for i in range(1, len(sentence)):
            #selects the ith and (i+1)th words to form a bigram
            ith_word=sentence[i]
            previous_word=sentence[i-1]
            #create a tuple for a bigram word set, set default value of bigram key to 0, the tuple is the key
            # trainingWord_counts[ith_word]+=1
            #build a tuple for each pair and put them in bigram_counts dictionary
            trainingBigram_counts[(previous_word,ith_word)] += 1

    for sentence in test_resultWOSS:    
        for i in range(1, len(sentence)):
            ith_word=sentence[i]
            previous_word=sentence[i-1]
            #create a tuple for a bigram word set, set default value of bigram key to 0, the tuple is the key
            # testWord_counts[ith_word]+=1
            #build a tuple for each pair and put them in bigram_counts dictionary
            testBigram_counts[(previous_word,ith_word)] += 1
    #calculate percertage of unique bigrams in test but not in training
    training_biset=set(trainingBigram_counts.keys())
    test_biset=set(testBigram_counts.keys())
    uniqueBiNotInT_percentage = (len(test_biset-training_biset)/len(test_biset))*100

    #calculate percertage of bigrams in test but not in training
    biNotInT=0
    for tupleKey in testBigram_counts:
        if tupleKey not in trainingBigram_counts:
            biNotInT+=testBigram_counts[tupleKey]       
    count_total=sum(testBigram_counts.values())
    biNotInT_percentage = (biNotInT / count_total)*100
       
    print("Question 4. What percentage of bigrams in the test corpus did not occur in training?")
    print("There are "+str(uniqueBiNotInT_percentage)+ "%"+" unique bigrams in the test corpus but not in training corpus.")
    print("There are "+str(biNotInT_percentage)+ "%" + " bigrams in the test corpus but not in training corpus.")
    print(" ")

def Question_5(Qsentence):
    with open ("train-Spring2023.txt","r", encoding='UTF8') as data:
        training = data.readlines() #read each line into a list
    training=[sentence.split() for sentence in training]

    Qsentence_words=Qsentence.split()

    word_dict={}
    for sentence in training:
        for word in sentence:
            if word in word_dict:
                word_dict[word]+=1
            else:
                word_dict[word]=1
    
    for word in Qsentence_words:
        if word not in word_dict:
            word="<unk>"

    Qsentence_dict={}
    for word in Qsentence_words:
        if word in Qsentence_dict:
            Qsentence_dict[word]+=1
        else:
            Qsentence_dict[word]=1

    #calculate log probability under unigram
    totalProbUni = 0
    for word in Qsentence_dict:
        eachProb = math.log(Qsentence_dict[word] / sum(Qsentence_dict.values()), 2)
        totalProbUni = totalProbUni+eachProb

    #alculate log probability under bigram
    bigram_counts = {('<s>', 'i'): 1, ('i', 'look'): 1, ('look', 'forward'): 1, ('forward', 'to'): 1, ('to', 'hearing'): 1, ('hearing', 'your'): 1, ('your', 'reply'): 1, ('reply', '.'): 1, ('.', '</s>'): 1}
    # compute bigram probabilities
    # if key not found, return 0
    eachProb1 = math.log(bigram_counts.get(('<s>', 'i'), 0) / 1, 2)
    eachProb2 = math.log(bigram_counts.get(('i', 'look'), 0) / 1, 2)
    eachProb3 = math.log(bigram_counts.get(('look', 'forward'), 0) / 1, 2)
    eachProb4 = math.log(bigram_counts.get(('forward', 'to'), 0) / 1, 2)
    eachProb5 = math.log(bigram_counts.get(('to', 'hearing'), 0) / 1, 2)
    eachProb6 = math.log(bigram_counts.get(('hearing', 'your'), 0) / 1, 2)
    eachProb7 = math.log(bigram_counts.get(('your', 'reply'), 0) / 1, 2)
    eachProb8 = math.log(bigram_counts.get(('reply', '.'), 0) / 1, 2)
    eachProb9 = math.log(bigram_counts.get(('.', '</s>'), 0) / 1, 2)
    totalProbBi = eachProb1 + eachProb2 + eachProb3 + eachProb4 + eachProb5 + eachProb6 + eachProb7 + eachProb8 + eachProb9

    #calculate log probability under bigram add one
    bigramAddOne_counts = {('<s>', 'i'): 2, ('i', 'look'): 2, ('look', 'forward'): 2, ('forward', 'to'): 2, ('to', 'hearing'): 2, ('hearing', 'your'): 2, ('your', 'reply'): 2, ('reply', '.'): 2, ('.', '</s>'): 2}
    eachProbAO1 = math.log(bigramAddOne_counts.get(('<s>', 'i'), 0) / (1 + 10), 2)
    eachProbAO2 = math.log(bigramAddOne_counts.get(('i', 'look'), 0) / (1 + 10), 2)
    eachProbAO3 = math.log(bigramAddOne_counts.get(('look', 'forward'), 0) / (1 + 10), 2)
    eachProbAO4 = math.log(bigramAddOne_counts.get(('forward', 'to'), 0) / (1 + 10), 2)
    eachProbAO5 = math.log(bigramAddOne_counts.get(('to', 'hearing'), 0) / (1 + 10), 2)
    eachProbAO6 = math.log(bigramAddOne_counts.get(('hearing', 'your'), 0) / (1 + 10), 2)
    eachProbAO7 = math.log(bigramAddOne_counts.get(('your', 'reply'), 0) / (1 + 10), 2)
    eachProbAO8 = math.log(bigramAddOne_counts.get(('reply', '.'), 0) / (1 + 10), 2)
    eachProbAO9 = math.log(bigramAddOne_counts.get(('.', '</s>'), 0) / (1 + 10), 2)
    totalProbBiAO = eachProbAO1 + eachProbAO2 + eachProbAO3 + eachProbAO4 + eachProbAO5 + eachProbAO6 + eachProbAO7 + eachProbAO8 + eachProbAO9

    print("Question 5. What is the log probability of the sentence under unigram, bigram and bigram add-one model?")
    print("The log probability of the sentence under unigram model is: " + str(totalProbUni))
    print("The log probability of the sentence under bigram model is: " + str(totalProbBi))
    print("The log probability of the sentence under bigram add-one model is: " + str(totalProbBiAO))
    print(" ")

    return totalProbUni, totalProbBi, totalProbBiAO

def Question_6(result1, result2, result3):
    l_uni = result1 / 10
    l_uniPerplexity = math.pow(2, -l_uni)

    l_bi = result2 / 10
    l_biPerplexity = math.pow(2, -l_bi)

    l_biAO = result3 / 10
    l_biAOPerplexity = math.pow(2, -l_biAO)

    print("Question 6. What is the perplexity of the sentence under unigram, bigram and bigram add-one model?")
    print("The perplexity of the sentence under unigram model is: " + str(l_uniPerplexity))
    print("The perplexity of the sentence under bigram model is: " + str(l_biPerplexity))
    print("The perplexity of the sentence under bigram add-one model is: " + str(l_biAOPerplexity))
    print(" ")

def Question_7(test_result):
    # test_result_new=test_result.splitlines()
    # test_result_new=[sentence.split() for sentence in test_result]

    test_dict={}
    for sentence in test_result:
        for word in sentence:
            if word in test_dict:
                test_dict[word]+=1
            else:
                test_dict[word]=1
    
    #calculate log probability under unigram
    totalProbUni = 0
    for word in test_dict:
        eachProb = math.log(test_dict[word] / sum(test_dict.values()), 2) #each individual probablity log
        totalProbUni = totalProbUni+eachProb #sigma of all probability log
    #calculate perplexity under unigram
    l_uni_test = totalProbUni / sum(test_dict.values())
    l_uniPerplexity_test = math.pow(2, -l_uni_test)

    #calculate log probability and perplexity under bigram
    totalBiP=0
    for eachP in bigram(test_result):
        totalBiP=totalBiP+math.log(eachP,2)
    l_bi_test = totalBiP / sum(test_dict.values())
    l_biPerplexity_test = math.pow(2, -l_bi_test)
    
    #calculate log probability and perplexity under bigram add-one
    totalBiAOP=0
    for eachP in add_one_bigram(test_result):
        totalBiAOP=totalBiAOP+math.log(eachP,2)
    l_biAO_test = totalBiAOP / sum(test_dict.values())
    l_biAOPerplexity_test = math.pow(2, -l_biAO_test)


    print("Question 7. What is the perplexity of the entire test corpus under unigram, bigram and bigram add-one model?")
    print("The perplexity of the entire test corpus under unigram model is: " + str(l_uniPerplexity_test))
    print("The perplexity of the entire test corpus under bigram model is: " + str(l_biPerplexity_test))
    print("The perplexity of the entire test corpus under bigram add-one model is: " + str(l_biAOPerplexity_test))
    print(" ")


training_result= training_preprocess()
training_resultWOSS = training_preprocess_WOSS()
test_result=test_preprocess()
test_resultWOSS=test_preprocessWOSS()

Question_1(training_result)
Question_2(training_resultWOSS)
Question_3()
Question_4(training_resultWOSS, test_resultWOSS)

logProdResult = Question_5("<s> i look forward to hearing your reply . </s>")

result1=logProdResult[0]
result2=logProdResult[1]
result3=logProdResult[2]
Question_6(result1, result2, result3)

Question_7(test_result)