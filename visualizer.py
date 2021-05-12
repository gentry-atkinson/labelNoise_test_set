#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Generate two Noise Not at Random label sets, 5% and 10%

from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    attributes = np.genfromtxt('data/all_attributes.csv', delimiter=',')
    clean_labesl = np.genfromtxt('data/clean_labels.csv')
    ncar_5p = np.genfromtxt('data/ncar_labels_5percent.csv')
    ncar_10p = np.genfromtxt('data/ncar_labels_10percent.csv')
    nar_5p = np.genfromtxt('data/nar_labels_5percent.csv')
    nar_10p = np.genfromtxt('data/nar_labels_10percent.csv')
    nnar_5p = np.genfromtxt('data/nnar_labels_5percent.csv')
    nnar_10p = np.genfromtxt('data/nnar_labels_10percent.csv')
