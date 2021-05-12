#Author: Gentry Atkinson
#Organization: Texas University
#Data: 11 May, 2021
#Divide the raw data into labeled 3 seconds segments by centering 150 sample
#  instances on a Perceptually Important Point. The first and las ~15 seconds
#  will be removed from every record.

from fastpip import pip
import os
import pandas
import numpy as np

files = os.listdir('raw_data')

if __name__ == "__main__":
    print('Raw files: ', files)
    att_file = open('all_attributes.csv', 'w+')
    lab_file = open('clean_labels.csv', 'w+')
    class_file = open('classes.txt', 'w+')
    class_file.write('0\tdog')
    class_file.write('1\thuman')
    class_file.close()

    d_counter = 0
    h_counter = 0
    total_counter = 0

    for file in files:
        att = pandas.read_csv('raw_data/'+file)
        num_segments = len(att['ax'])//150
        print('Segments in ', file, ': ', num_segments)
        print('Keys: ', att.keys())
        print('Number of samples: ', len(att['time']))

        instance_acc = [np.linalg.norm([att['ax'][i], att['ay'][i], att['az'][i]]) for i in range(len(att['time']))]
        instance_gyro = [np.linalg.norm([att['wx'][i], att['wy'][i], att['wz'][i]]) for i in range(len(att['time']))]
        instance_mag = [np.linalg.norm([att['Bx'][i], att['By'][i], att['Bz'][i]]) for i in range(len(att['time']))]
        print('Number of acc values: ', len(instance_acc))

        pips = pip([(i, j) for i,j in enumerate(instance_acc)], num_segments+2, distance='vertical')
        pips = pips[1:-1] #remove start and end points

        for p in pips:
            if p[0]<75:
                att_file.write(', '.join(str(i) for i in instance_acc[:150]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_gyro[:150]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_mag[:150]) + '\n')
            elif len(instance_acc) - p[0] < 76:
                att_file.write(', '.join(str(i) for i in instance_acc[-150:]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_gyro[-150:]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_mag[-150:]) + '\n')
            else:
                att_file.write(', '.join(str(i) for i in instance_acc[p[0]-75:p[0]+75]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_gyro[p[0]-75:p[0]+75]) + '\n')
                att_file.write(', '.join(str(i) for i in instance_mag[p[0]-75:p[0]+75]) + '\n')

            total_counter += 1

            if 'dog' in file:
                lab_file.write('0\n')
                d_counter += 1
            elif 'human' in file:
                lab_file.write('1\n')
                h_counter += 1

    att_file.close()
    lab_file.close()

    print('Total counter: ', total_counter)
    print('Total dog walks: ', d_counter)
    print('Total human wallks: ', h_counter)
    print('Total lines of attributes: ')
    os.system('cat all_attributes.csv | wc -l')
    print('Total lines of labels: ')
    os.system('cat clean_labels.csv | wc -l')
