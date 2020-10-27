#############################################################################################
# RB_run.py runs
#   Written by Anzy Lee, Postdoctoral Scholar, Utah State University
#   Date: 10/21/2020
#############################################################################################
import os
from riverbuilder.core import river

#############################################################################################
# Input: dir, case_name, fname, outfolder, log
dir = "site316"                     # The name of directory 
case_name = "site316_5x_cleanbed"
os.chdir(dir)

fname = case_name + "/" + case_name + ".txt"
outfolder = case_name + "/" + case_name
log = ""

river.buildRiver(fname, outfolder, log)

