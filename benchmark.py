#!/usr/bin/env python

from glob import glob
import subprocess
import os

ts_command = "/Users/pwalters/software/TS/ts_main.py"
rws_command = "/Users/pwalters/software/TS_Enhanced/src_multiprocess/ts_main.py"

os.chdir("docking")
ts_json_list = glob("ts*.json") 
rws_json_list = glob("rws*.json")
for ts_json_file in ts_json_list:
    subprocess.run([ts_command, ts_json_file])
for rws_json_file in rws_json_list:
    subprocess.run([rws_command, rws_json_file])
    
os.chdir("..")

os.chdir("rocs")
ts_json_list = glob("ts*.json") 
rws_json_list = glob("rws*.json")
for ts_json_file in ts_json_list:
    subprocess.run([ts_command, ts_json_file])
for rws_json_file in rws_json_list:
    subprocess.run([rws_command, rws_json_file])
    
    
    
