#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Train and test some models on the 7 label sets with FE

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from os import listdir
from utils.ts_feature_toolkit import get_features_from_one_signal

files = [i for i in listdir('data') if 'label' in i]

results_file = open('model_tests_with_fe.txt', 'w+')

if __name__ == '__main__':
    #Read attributes from file and isolate accelerometer
    X = [get_features_from_one_signal(i) for i in np.genfromtxt('data/all_attributes.csv', delimiter=',')[::3]]

    print('Number of instances: ', len(X))
    print('Size of feature vector: ', len(X[0]))


    #Header for results file
    results_file.write('##### Model tests with No Feature Extraction #####\n\n')

    #test SVM
    results_file.write('SVM with rbf kernel and with 80/20 split:\n')
    results_file.write('FILE\t\t\t\t\t\tACC\n')
    for file in files:
        print('Reading ', file)
        y = np.genfromtxt('data/'+file)
        print('Number of dog instances: ', sum(y==0))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = SVC(kernel='rbf').fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results_file.write('{}{}{}\n'.format(file, '\t\t\t' if len(file) < 24  else '\t', accuracy_score(y_test, y_pred)))

    #test Tree
    results_file.write('\nTree with 80/20 split:\n')
    results_file.write('FILE\t\t\t\t\t\tACC\n')
    for file in files:
        print('Reading ', file)
        y = np.genfromtxt('data/'+file)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = tree.DecisionTreeClassifier().fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results_file.write('{}{}{}\n'.format(file, '\t\t\t' if len(file) < 24  else '\t', accuracy_score(y_test, y_pred)))

    #test KNN
    results_file.write('\nKNN with K=3 and 80/20 split:\n')
    results_file.write('FILE\t\t\t\t\t\tACC\n')
    for file in files:
        print('Reading ', file)
        y = np.genfromtxt('data/'+file)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results_file.write('{}{}{}\n'.format(file, '\t\t\t' if len(file) < 24  else '\t', accuracy_score(y_test, y_pred)))

    #test KNN again
    results_file.write('\nKNN with K=7 and 80/20 split:\n')
    results_file.write('FILE\t\t\t\t\t\tACC\n')
    for file in files:
        print('Reading ', file)
        y = np.genfromtxt('data/'+file)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = KNeighborsClassifier(n_neighbors=7).fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results_file.write('{}{}{}\n'.format(file, '\t\t\t' if len(file) < 24  else '\t', accuracy_score(y_test, y_pred)))

    results_file.close()
