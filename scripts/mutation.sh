#!/bin/bash

SEEDS=(123456 212392 310293 429312 523123)
DIR_MUT="../data/mutation.txt"

for seed in "${SEEDS[@]}"
do
    echo $seed >> $DIR_MUT
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb07 20 0.5 0.5 {} 600 100000000 $seed ::: 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1 >> $DIR_MUT
done
exit 0
