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

with open('cards_MN.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    fileName = line.strip()
    print fileName

    name1 = fileName
    name2 = fileName.replace("Resolved", "Boosted")

    combinedName = fileName.replace("Resolved", "Combined")

    cmd = "combineCards.py Name1="+name1+" Name2="+name2+" > "+combinedName

    print cmd

    os.system(cmd)
