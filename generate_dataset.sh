#!/usr/bin/env bash

#Author: Gentry Atkinson
#Organization: Texas University
#Data: 13 May, 2021
#Segment the raw data with clean labels, generate 6 noisy label sets, and then
#  make a few visuals.

echo Segmenting Data
python3 divide_signals.py
echo Generating NCAR
python3 add_ncar.py
echo Generating NAR
python3 add_nar.py
echo Generating NNAR
python3 add_nnar.py
echo Generating Plots
python3 visualizer.py
