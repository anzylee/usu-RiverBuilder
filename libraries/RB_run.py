#############################################################################################
# RB_run.py runs
#   Written by Anzy Lee, Postdoctoral Scholar, Utah State University
#   Date: 10/21/2020
#############################################################################################
import os
from riverbuilder.core import river
import matplotlib.pyplot as plt

#############################################################################################
# Input: dir, case_name
dir = "../samples/site316"                     # The name of directory you want to set
                                    # as a current working directory
case_name = "site316_v3"   # Name for the case

#############################################################################################
# Optional inputs: fname, outfolder, log
os.chdir(dir)
fname = case_name + "/" + case_name + ".txt"
outfolder = case_name + "/" + case_name
log = case_name + "/" + case_name + "_log.txt"
#############################################################################################
# Run RiverBuilder
river.buildRiver(fname, outfolder, log)

#plt.close('all')
plt.close(2)
plt.close(3)
plt.close(4)
plt.close(5)
plt.axis('scaled')