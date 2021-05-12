#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Generate two Noise at Random label sets, 5% and 10%

import numpy as np
from random import randint
import os

if __name__ == "__main__":
    clean_labels = np.genfromtxt('clean_labels.csv')
    low_noise_labels = open('nar_labels_5percent.csv', 'w+')
    high_noise_labels = open('nar_labels_10percent.csv', 'w+')

    total_counter = 0
    l_flipped_coutner = 0
    h_flipped_counter = 0

    for l in clean_labels:


    low_noise_labels.close()
    high_noise_labels.close()

    #sanity checks
    print('Total labels processed: ', total_counter)
    print('Low noise labels flipped: ', l_flipped_coutner)
    print('High noise labels flipped: ', h_flipped_counter)
    print('Lines written to low noise file: ')
    os.system('cat nar_labels_5percent.csv | wc -l')
    print('Lines written to high noise file: ')
    os.system('cat nar_labels_10percent.csv | wc -l')
