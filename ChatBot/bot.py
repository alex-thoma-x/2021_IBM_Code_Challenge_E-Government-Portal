import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
import json
import random

intents = json.loads(open('intents.json').read())
model = load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


def clean_up_sentence(sentence):
    # tokenization of the sentence
    sentence_words = nltk.word_tokenize(sentence)
    # lematization of the words
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    # passing to values to get cleaned sentence
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:


                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    # return array of nag of words
    return (np.array(bag))


# function for prediction
def predict_class(sentence, model):
    # filtering the prediction based on threshold value
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]

    # setting threshold value
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort on the basis of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list



def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

#function to return the response as output in the window
def chatbot_response(msg):
    ints = predict_class(msg, model)
    print(ints)
    res = getResponse(ints, intents)

    return res




import speech_recognition as sr

def MAL():
    r = sr.Recognizer()
    with sr.Microphone() as source:


        print('Listening')
        r.pause_threshold = 0.7
        #for noise cancellation
        r.adjust_for_ambient_noise(source)
        #time for recording
        audio = r.listen(source,phrase_time_limit=4)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='ml-In')

            #Displaying the recognized text in Malayalam
            print("The Text is='", Query, "'")
            return Query

        #To raise exception if no speech was recognized or no audio was played
        except Exception as e:
            print(e)
            print("we didnt get you")
            return "None"
        return Query


#function for translating malayalam into english
from googletrans import Translator
def trans(query):
    translator = Translator()
    result = translator.translate(query,dest='en', src='auto')
    return result

i=True

from playsound import playsound
from gtts import gTTS
import os
while i is True:
    query=MAL()
    text=trans(query)
    if (text.text == "Exit"):
        break
    print(text.text)
    p=chatbot_response(text.text)
    translator = Translator()
    result = translator.translate(p, dest='ml', src='en')
    print(result.text)
    mal1=gTTS(result.text,lang='ml')
    isFile = os.path.isfile('v.mp3')
    if(isFile):
        os.remove("v.mp3")
    mal1.save("v.mp3")
    playsound("v.mp3")

