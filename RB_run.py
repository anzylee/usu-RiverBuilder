import os
from riverbuilder.core import river
#import riverbuilder

dir = "site316"
os.chdir(dir)

fname = "site316_5x_roughbed.txt"
outfolder = "site316_5x_roughbed"
log = "site316_roughbed"
river.buildRiver(fname, outfolder, log)