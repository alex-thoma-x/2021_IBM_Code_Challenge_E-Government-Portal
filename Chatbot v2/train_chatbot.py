import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random

with open('intents.json','r') as jsonfile:
    print(jsonfile)
    intents = json.load(jsonfile)

#creating lists
words=[]
classes = []
documents = []
#ignore these words
ignore_words = ['?', '!']

for intent in intents['intents']:
    for pattern in intent['patterns']:

        #tokenization technique
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #adding documents
        documents.append((w, intent['tag']))

        # append the tags into "classes" list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatization technique
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
# this way we can remove duplicates
words = sorted(list(set(words)))
# now sort the "classes" list
classes = sorted(list(set(classes)))

print (len(documents), "documents")
# classes are categories of intents
print (len(classes), "classes", classes)
# print all words after apply the two techniques
print (len(words), "unique lemmatized words", words)

#this will save our 'words' list into new file named 'words.pkl'
pickle.dump(words,open('words.pkl','wb'))

#this will save our 'classes' list into new file named 'classes.pkl'
pickle.dump(classes,open('classes.pkl','wb'))

# creating training data
training = []
# empty array for output
output_empty = [0] * len(classes)
# training set
for doc in documents:
    # initialize the list "bag"(which is going to be bag of words)
    bag = []
    # creating list for tokens of pattern(words)
    pattern_words = doc[0]
    # lemmatization
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # if the word is found in current pattern then append 1 in the bag of words array otherwise append 0
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # only for current tag, output will be 1. Otherwise 0
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffling the efatures
random.shuffle(training)
training = np.array(training)
# spliting the data into x and y . X - patterns, Y - intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

#Compile this Keras model with SGD optimizer.
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fit the model with 200 epochs
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
#save the model in .h5 format
model.save('chatbot_model.h5', hist)
#print the statment when the model training is finished
print("model created")