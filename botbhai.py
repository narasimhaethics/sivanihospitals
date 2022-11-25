import full_elizabot
import nltk
from nltk.stem.lancaster import LancasterStemmer
import json
import sys
from pprint import pprint


import re
import random

from six.moves import input

stemmer = LancasterStemmer()


class_name = []
class_values = []


default_response=['i am still learning']

honchi_response = ['  HONCHI Provides open source technology support .Honchi is a tech driven company,which makes large enterprises,SMEs and startups to help in achieve niche technology like DevOps MicroServices AI']

devops_response=[' 1. Build - continuous integration and testing 2. Release - continuous delivery and deployment 3. Operate - continuous operations 4. Monitor']


services_response=['1.devops 2.microservices 3.Ai']

honchilocation=[' 113, Vayu Business Center,Kanka Towers, Dollars Colony Main road, J.P Nagar, 4th Phase, Dollar Layout, Phase 4,JP Nagar, Bangalore,Karnataka - 560078 ']

ceo=['Sanskriti Gupta']


microservices = ['Our microservice architecture is a method of developing software applications as a suite of independently deployable, small, modular services in which each service runs a unique process and communicates through a well-defined. To make scalable microservices we use “Dockers” and “kubernetes.']


ai = [' HONCHI SOLUTION PVT LTD Artificial Intelligence as a 360 degree service. We help companies with developing a range of AI solutions that learn and think like humans using Natural Language Processing (NLP), Speech Recognition and Machine Learning feature HONCHI has core ability to integrate artificial intelligence using cognitive technology and semantic technology with any of your current and future business modules, solutions or third party applications across a full spectrum of industries, from Big Data, Business Intelligence, Analytics, IT Technology and others. We enable organization to connect artificial intelligence with your day to day working environment.']

training_data = []



training_data.append({"class":"ai", "sentence":"what is ai??"})
training_data.append({"class":"ai", "sentence":"artificial intelligence"})
training_data.append({"class":"ai", "sentence":"ai"})
training_data.append({"class":"ai", "sentence":"can you explain me about ai?"})
training_data.append({"class":"ai", "sentence":"can you tell me about ai?"})
training_data.append({"class":"ai", "sentence":"what is the process in ai??"})



training_data.append({"class":"microservices", "sentence":"what is microservices??"})
training_data.append({"class":"microservices", "sentence":"microservices"})
training_data.append({"class":"microservices", "sentence":"explain me about microservices?"})
training_data.append({"class":"microservices", "sentence":"tell me about microservices?"})
training_data.append({"class":"microservices", "sentence":"what is the process in microservices??"})


training_data.append({"class":"ceo", "sentence":"who is the ceo of your company"})
training_data.append({"class":"ceo", "sentence":"who is the ceo of honchi"})
training_data.append({"class":"ceo", "sentence":"tell me who is the director of honchi"})
training_data.append({"class":"ceo", "sentence":"director"})
training_data.append({"class":"ceo", "sentence":"ceo"})



training_data.append({"class":"honchilocation", "sentence":"where is your company"})
training_data.append({"class":"honchilocation", "sentence":"location of honchi"})
training_data.append({"class":"honchilocation", "sentence":"location"})
training_data.append({"class":"honchilocation", "sentence":"tell me the location of your company"})
training_data.append({"class":"honchilocation", "sentence":"can you guide through me the location of your company"})


training_data.append({"class":"services", "sentence":"list all the services provided by the company"})
training_data.append({"class":"services", "sentence":"services"})
training_data.append({"class":"services", "sentence":"what services do you provide?"})
training_data.append({"class":"services", "sentence":"tell me about your services?"})
training_data.append({"class":"services", "sentence":"can you tell me about your services"})
training_data.append({"class":"services", "sentence":"what different kind of services do you provide ??"})

training_data.append({"class":"devops", "sentence":"what is devops??"})
training_data.append({"class":"devops", "sentence":"devops"})
training_data.append({"class":"devops", "sentence":"explain me about devops?"})
training_data.append({"class":"devops", "sentence":"tell me about devops?"})
training_data.append({"class":"devops", "sentence":"what is the process in devops??"})

training_data.append({"class":"honchi", "sentence":"what is honchi ??"})
training_data.append({"class":"honchi", "sentence":"honchi"})
training_data.append({"class":"honchi", "sentence":"can you tell me about honchi solutions ??"})
training_data.append({"class":"honchi", "sentence":"explain me what is honchi??"})
training_data.append({"class":"honchi", "sentence":"what is your company name"})
training_data.append({"class":"honchi", "sentence":"just tell me about your company name"})


training_data.append({"class":"bot","sentence":"Hi"})
training_data.append({"class":"bot","sentence":"Tell me about you"})
training_data.append({"class":"bot","sentence":"Tell me"})
training_data.append({"class":"bot","sentence":"Greetings!"})
training_data.append({"class":"bot","sentence":"Hi, How is it going?"})
training_data.append({"class":"bot","sentence":"How are you doing?"})
training_data.append({"class":"bot","sentence":"Nice to meet you."})
training_data.append({"class":"bot","sentence":"How do you do?"})
training_data.append({"class":"bot","sentence":"Hi, nice to meet you."})
training_data.append({"class":"bot","sentence":"It is a pleasure to meet you."})
training_data.append({"class":"bot","sentence":"Top of the morning to you!"})
training_data.append({"class":"bot","sentence":"What's up?"})
training_data.append({"class":"bot","sentence":"can you please tell me about yourself"})



##print ("%s sentences of training data" % len(training_data))


#sentence = input()
sentence = sys.stdin.readline()


corpus_words = {}
class_words = {}

classes = list(set([a['class'] for a in training_data]))
for c in classes:
    
    class_words[c] = []


for data in training_data:

    for word in nltk.word_tokenize(data['sentence']):

        if word not in ["?", "'s"]:

            stemmed_word = stemmer.stem(word.lower())

            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1


            class_words[data['class']].extend([stemmed_word])


################print ("Corpus words and counts: %s \n" % corpus_words)

################print ("Class words: %s" % class_words)




def calculate_class_score(sentence, class_name, show_details=True):
    score = 0

    for word in nltk.word_tokenize(sentence):

        if stemmer.stem(word.lower()) in class_words[class_name]:

            score += 1
            
            if show_details:
                pass
                #print ("   match: %s" % stemmer.stem(word.lower() ))
    return score






##sentence = "what types of services your company provide?? "


for c in class_words.keys():
    class_name.append(c)
    class_values.append(calculate_class_score(sentence, c))        
    #print ("Class: %s  Score: %s \n" % (c, calculate_class_score(sentence, c)))




def calculate_class_score(sentence, class_name, show_details=True):
    score = 0

    for word in nltk.word_tokenize(sentence):

        if stemmer.stem(word.lower()) in class_words[class_name]:

            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                pass
               # print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score




def classify(sentence):
    high_class = None
    high_score = 0

    for c in class_words.keys():

        score = calculate_class_score_commonality(sentence, c, show_details=False)

        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score





#print (class_values)
#print (class_name)


########print(class_values[class_name.index('bot')])


if sum(class_values)==0:

        full_elizabot.demo(sentence)
    



else:
	
    

    jok=max(class_values)
    koj=class_values.index(jok)

    if(jok == class_values[class_name.index('bot')]):
        full_elizabot.demo(sentence)

    else:
        if (class_name[koj]=="honchi"):
            print (honchi_response)
    
        if (class_name[koj]=="services"):
            print (services_response)
    
        if (class_name[koj]=="devops"):
            print (devops_response)


        if (class_name[koj]=="bot"):
            full_elizabot.demo(sentence)

        if (class_name[koj]=="honchilocation"):
            print (honchilocation) 

        if (class_name[koj]=="ceo"):
            print (ceo)

        if (class_name[koj]=="microservices"):
            print (microservices)

        if (class_name[koj]=="ai"):
            print (ai)


    
  
#############if(jok==0):
#########    print ("i am still in learning phase")
##########    class_name = "bot"
##############else:











