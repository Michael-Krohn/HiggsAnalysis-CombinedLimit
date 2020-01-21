#!/usr/bin/env python

import os
import argparse
import datetime

parser = argparse.ArgumentParser(description='SKFlat Command')
parser.add_argument('-i', dest='Logdir')
args = parser.parse_args()

if not args.Logdir:
  parser.error('-i : log directory name should be given')

Logdir = args.Logdir

os.system('ls -1 '+Logdir+'/job_*.log > tmp.txt')
lines = open('tmp.txt').readlines()
os.system('rm tmp.txt')

n_job = len(lines)
for i in range(0,n_job):
  lines_log = open(lines[i].strip('\n')).readlines()

  CardUsed = ""
  for k in range(0,len(lines_log)):
    j = len(lines_log)-1-k
    line = lines_log[k]
    if "Input datacard" in line:
      CardUsed = line.split()[2]
      break

  CardUsed = CardUsed.split('/')[-1].replace('.txt','')
  #print CardUsed

  Expected_Central = ""
  Expected_1sdUp = ""
  Expected_1sdDn = ""
  Expected_2sdUp = ""
  Expected_2sdDn = ""
  Obs = ""

  for k in range(0,len(lines_log)):
    j = len(lines_log)-1-k
    line = lines_log[k]
    if "Expected 50.0%" in line:
      Expected_Central = line.split()[4]
    if "Expected 84.0%" in line:
      Expected_1sdUp = line.split()[4]
    if "Expected 16.0%" in line:
      Expected_1sdDn = line.split()[4]
    if "Expected 97.5%" in line:
      Expected_2sdUp = line.split()[4]
    if "Expected  2.5%" in line:
      Expected_2sdDn = line.split()[4]

  # CardUsed = card_EE_Combined_WR5000_N4200
  words = CardUsed.split('_')
  cardinfo = 'MuMu\tResolved\t'+words[1]+'\t'+words[3]+'\t'

  #if Expected_Central=="":
  #  print cardinfo

  print cardinfo+'\t'+Expected_Central+'\t'+Expected_1sdUp+'\t'+Expected_1sdDn+'\t'+Expected_2sdUp+'\t'+Expected_2sdDn


'''
 -- AsymptoticLimits ( CLs ) --
Observed Limit: r < 546.5518
Expected  2.5%: r < 1.1521
Expected 16.0%: r < 1.5664
Expected 50.0%: r < 2.2344
Expected 84.0%: r < 3.2497
Expected 97.5%: r < 4.5513

Done in 0.00 min (cpu), 0.00 min (real)
'''
