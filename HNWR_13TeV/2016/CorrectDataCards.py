import ROOT as r
import sys
import datetime
import subprocess
import os
import copy
import sets
import collections
import math
import array

print "STARTING"

with open('datacardFiles.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    fileName = line.strip()
    print fileName

    with open('Ingredients/'+fileName) as f:
	datacardLines = f.read().splitlines()

    outputFileName = 'Ingredients_ReBin/'+fileName
    outputFile = open(outputFileName, "w+")

    for singleLine in datacardLines:
	if "shapes" in singleLine: 
	    correctedLine = singleLine.replace("Ingredients", "Ingredients_ReBin")
	elif "Stat" in singleLine: continue
	else: correctedLine = singleLine
	
	outputFile.write(correctedLine)
	outputFile.write("\n")

#    if "Combined" in fileName:
#    	outputFile.write("Lumi lnN 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025\n")
#    else:
#        outputFile.write("Lumi lnN 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025 1.025\n")
    outputFile.write("* autoMCStats 0 0 1\n")

outputFile.close()
