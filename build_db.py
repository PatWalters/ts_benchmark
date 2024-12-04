#!/usr/bin/env python

import sys

import pandas as pd
from sqlitedict import SqliteDict
from tqdm.auto import tqdm

chunksize = 1e5

for filename in sys.argv[1:]:
    print(f"processing {filename}")
    db = SqliteDict(filename.replace(".csv",".sqlite"))
    for idx, df in tqdm(enumerate(pd.read_csv(filename,chunksize=chunksize))):
        for smiles,title, score in df.values:
            db[title] = score
        db.commit()

db.close()
