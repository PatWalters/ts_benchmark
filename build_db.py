#!/usr/bin/env python

import sys

import pandas as pd
from sqlitedict import SqliteDict
from tqdm.auto import tqdm
from glob import glob

chunksize = 1e5

file_list = glob("docking/*scores.csv") + glob("rocs/*scores.csv") 

for filename in file_list:
    print(f"processing {filename}")
    db = SqliteDict(filename.replace(".csv",".sqlite"))
    for idx, df in tqdm(enumerate(pd.read_csv(filename,chunksize=chunksize))):
        for smiles,title, score in df.values:
            db[title] = score
        db.commit()

db.close()
