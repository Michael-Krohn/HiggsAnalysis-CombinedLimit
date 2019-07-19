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

with open('workspaceFiles.txt') as f:
    lines = f.read().splitlines()

binBoundaries = [800, 1000, 1200, 1400, 1600, 1800, 2000, 8000]
binBoundariesArray = array.array('d', binBoundaries)

binBoundaries_Resolved = [800, 1000, 1200, 1400, 1600, 2000, 2400, 2800, 3200, 3600, 4000, 8000]
binBoundariesArray_Resolved = array.array('d', binBoundaries_Resolved)
for line in lines:
    fileName = line.strip()
    print fileName

    tfile = r.TFile.Open('Ingredients/'+fileName)

    outputFileName = 'Ingredients_ReBin/'+fileName
    outputFile = r.TFile(outputFileName, "RECREATE")

    for key in tfile.GetListOfKeys():
      print key.GetName()

      if "Boosted" in fileName:

    	if "WR" in key.GetName():
	    temp = tfile.Get(key.GetName())
            temp2 = temp.Rebin(6 ,key.GetName(), binBoundariesArray)
	    temp2.SetDirectory(0)
#	    temp2.Scale(.001)
#	    temp.Rebin(4 ,key.GetName(), binBoundariesArray)

	    temp2.Write()

    	else:
	    temp = tfile.Get(key.GetName())
            temp2 = temp.Rebin(6 ,key.GetName(), binBoundariesArray)
            temp2.SetDirectory(0)
#            temp.Rebin(4 ,key.GetName(), binBoundariesArray)
            temp2.Write()

      else:

        if "WR" in key.GetName():
            temp = tfile.Get(key.GetName())
            temp2 = temp.Rebin(11 ,key.GetName(), binBoundariesArray_Resolved)
            temp2.SetDirectory(0)
#            temp2.Scale(.001)
#           temp.Rebin(4 ,key.GetName(), binBoundariesArray)

            temp2.Write()

        else:
            temp = tfile.Get(key.GetName())
            temp2 = temp.Rebin(11 ,key.GetName(), binBoundariesArray_Resolved)
            temp2.SetDirectory(0)
#            temp.Rebin(4 ,key.GetName(), binBoundariesArray)
            temp2.Write()



outputFile.Write()
outputFile.Close()
