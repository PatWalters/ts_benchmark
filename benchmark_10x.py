#!/usr/bin/env python

import sys
from glob import glob
import subprocess
import os

ts_command = "/Users/pwalters/software/TS/ts_main.py"
rws_command = "/Users/pwalters/software/TS_Enhanced/src_multiprocess/ts_main.py"
ga_command = "/Users/pwalters/software/TS/ga_sampling.py"

os.chdir("docking")
ts_json_list = glob("ts*_0*.json")
rws_json_list = glob("rws*_0*.json")
#ga_json_list = glob("ga*_0*.json")
for ts_json_file in ts_json_list:
    subprocess.run([ts_command, ts_json_file])
for rws_json_file in rws_json_list:
    subprocess.run([rws_command, rws_json_file])
#for ga_json_file in ga_json_list:
#    subprocess.run([ga_command, ga_json_file])
    
os.chdir("..")

os.chdir("rocs")
ts_json_list = glob("ts*_0*.json") 
rws_json_list = glob("rws*_0*.json")
#ga_json_list = glob("ga*_0*.json")
for ts_json_file in ts_json_list:
    subprocess.run([ts_command, ts_json_file])
for rws_json_file in rws_json_list:
    subprocess.run([rws_command, rws_json_file])
#for ga_json_file in ga_json_list:
#    subprocess.run([ga_command, ga_json_file])
    
os.chdir("..")    
    
    
    
