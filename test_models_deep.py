#Author: Gentry Atkinson
#Organization: Texas University
#Data: 24 May, 2021
#Train and test some models on the 7 label sets on keras models

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from os import listdir
from tensorflow.keras.utils import to_categorical
from utils.build_simple_dnn import get_trained_dnn

files = [i for i in listdir('data') if 'label' in i]

results_file = open('model_tests_deep.txt', 'w+')

if __name__ == '__main__':
    #Read attributes from file and isolate accelerometer
    X = np.genfromtxt('data/all_attributes.csv', delimiter=',')[::3]

    #Header for results file
    results_file.write('##### Model tests with Keras Models #####\n\n')

    #test SVM
    results_file.write('4 hidden layer NN and with 80/20 split:\n')
    results_file.write('FILE\t\t\t\t\t\tACC\n')
    for file in files:
        print('Reading ', file)
        y = to_categorical(np.genfromtxt('data/'+file))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = get_trained_dnn(X_train, y_train)
        y_pred = model.predict(X_test)
        print(y_test)
        results_file.write('{}{}{}\n'.format(file, '\t\t\t' if len(file) < 24  else '\t', accuracy_score(np.argmax(y_test, axis=-1), np.argmax(y_pred, axis=-1))))

    results_file.close()
