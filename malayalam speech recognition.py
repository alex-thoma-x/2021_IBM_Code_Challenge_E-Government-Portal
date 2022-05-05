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
def trans(query):
    from googletrans import Translator
    translator = Translator()
    result = translator.translate(query,dest='en', src='auto')
    return result


query=MAL()
text=trans(query)
print(text.text)


