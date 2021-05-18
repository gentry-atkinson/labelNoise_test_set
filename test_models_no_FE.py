#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Train and test some models on the 7 label sets without FE

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

files = [
        'clean_labels.csv'
    ]

results_file = open('model_tests_no_fe.txt', 'w+')

if __name__ == '__main__':
    #Read attributes from file and isolate accelerometer
    X = np.genfromtxt('data/all_attributes.csv', delimiter=',')[::3]

    #Header for results file
    results_file.write('##### Model tests with No Feature Extraction #####\n\n')

    #test SVM
    results_file.write('SVM with 80/20 split:\n')
    for file in files:
        y = np.genfromtxt('data/'+file)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = SVC().fit(X_train, y_train)
