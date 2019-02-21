#!/bin/bash


python $1.py 
pdflatex $1.tex

rm *.aux *.log *.vscodeLog

evince $1.pdf

