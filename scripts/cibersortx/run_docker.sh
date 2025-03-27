#!/bin/bash

# 设置输入和输出目录路径
DATA_DIR="/mnt/d/Data/cibersortx/Fig2ab-NSCLC_PBMCs"
OUT_DIR="/mnt/d/Data/cibersortx/Fig2ab-NSCLC_PBMCs/outdir3"
refsample="Fig2ab-NSCLC_PBMCs_scRNAseq_refsample.txt"
mixtures="Fig2b-WholeBlood_RNAseq.txt"

if [ ! -d "$DATA_DIR" ]; then
  echo "Error: Directory $DATA_DIR does not exist."
  exit 1
fi

if [ ! -d "$OUT_DIR" ]; then
  echo "Error: Directory $OUT_DIR does not exist."
  exit 1
fi

docker run -v $DATA_DIR:/src/data -v $OUT_DIR:/src/outdir cibersortx/fractions \
    --username yhu39@jhmi.edu --token  d4af24aca695fee2b98b888d388418a6 \
    --single_cell TRUE --refsample $refsample --fraction 0 --verbose TRUE \
    --QN FALSE --filter FALSE --replicates 5 --sampling 0.5 --k.max 999