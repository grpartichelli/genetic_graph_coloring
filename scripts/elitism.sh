#!/bin/bash

SEEDS=(123456 212392 310293 429312 523123)
DIR_ELI="../data/elitism.txt"

for seed in "${SEEDS[@]}"
do
    echo $seed >> $DIR_ELI
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb07 20 {} 0.8 0.3 900 100000000 $seed ::: 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 >> $DIR_ELI
done
exit 0
