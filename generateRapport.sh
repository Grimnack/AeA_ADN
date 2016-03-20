#!/bin/sh
python Mot.py
gnuplot "occurencesARN.plot"
pdflatex rapport.tex
