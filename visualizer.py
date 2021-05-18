#Author: Gentry Atkinson
#Organization: Texas University
#Data: 12 May, 2021
#Create some "sanity check" plots for all 7 label sets using tSNE

from matplotlib import pyplot as plt
import numpy as np
from sklearn.manifold import TSNE as tsne

if __name__ == "__main__":
    attributes = np.genfromtxt('data/all_attributes.csv', delimiter=',')
    clean_labels = np.genfromtxt('data/clean_labels.csv')
    ncar_5p = np.genfromtxt('data/ncar_labels_5percent.csv')
    ncar_10p = np.genfromtxt('data/ncar_labels_10percent.csv')
    nar_5p = np.genfromtxt('data/nar_labels_5percent.csv')
    nar_10p = np.genfromtxt('data/nar_labels_10percent.csv')
    nnar_5p = np.genfromtxt('data/nnar_labels_5percent.csv')
    nnar_10p = np.genfromtxt('data/nnar_labels_10percent.csv')

    acc = [attributes[i] for i in range(0, len(attributes), 3)]
    SET_LENGTH = len(clean_labels)

    v = tsne(n_components=2, n_jobs=8).fit_transform(acc)
    colors = ['red', 'blue']
    print('Clean Plot')
    plt.figure(1)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(clean_labels[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_clean.pdf')
    print('NCAR Plots')
    plt.figure(2)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(ncar_5p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_ncar_5percent.pdf')

    plt.figure(3)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(ncar_10p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_ncar_10percent.pdf')
    print('NAR Plots')
    plt.figure(4)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(nar_5p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_nar_5percent.pdf')

    plt.figure(5)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(nar_10p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_nar_10percent.pdf')
    print('NNAR Plots')
    plt.figure(6)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(nnar_5p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_nnar_5percent.pdf')

    plt.figure(7)
    for i in range(SET_LENGTH):
        plt.scatter(v[i][0], v[i][1], c=colors[int(nnar_10p[i])], s=2, marker='.')
    plt.savefig('imgs/tsne_nnar_10percent.pdf')
