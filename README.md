# ts_benchmark

A set of benchmarks for Thompson Sampling and related methods. The benchmark has two combinatorial libraries constisting of 1 million molecules each.
- amide - 1000 x 1000
- quinazoline - 100 x 100 x 100
For both libraries results are reported for docking into 2zdt from the pdb.  ROCS scores are TanimotoCombo based on the queries in the data directory. 

Steps for running the benchmark

1. build_db.py - this builds the databases required to run the benchmarks.  This only needs to be done once.
2. benchmark.py - this runs the docking and ROCS benchmarks, change **ts_command** and **rws_command** to fit your environment. 
3. ts_analysis.ipynb - this performs the analsysis of the results

