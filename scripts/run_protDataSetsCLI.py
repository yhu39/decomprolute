#!/usr/local/bin/python
'''
Basic CLI to import CPTAC proteomic data
'''
import argparse
import pandas

in_path = "/Users/yingweihu/Documents/GitHub/decomprolute/protData/data/hnscc.csv"
out_path = "/Users/yingweihu/Documents/GitHub/decomprolute/protData/data/hnscc.tsv"

df=pandas.read_csv(in_path,index_col=0)

df.transpose().to_csv(path_or_buf=out_path, sep='\t')
