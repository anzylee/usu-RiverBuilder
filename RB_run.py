import os
from riverbuilder.core import river

dir = "site316"
case_name = "site316_5x_cleanbed"
os.chdir(dir)

fname = case_name + "/" + case_name + ".txt"
outfolder = case_name + "/" + case_name
log = ""
river.buildRiver(fname, outfolder, log)

