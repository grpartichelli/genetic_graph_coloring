#!/bin/bash

SEEDS=(123456 212392 310293 429312 523123)
DIR_POP="../data/population03.txt"

for seed in "${SEEDS[@]}"
do
    echo $seed >> $DIR_POP
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb07 {} 0.5 0.5 0.5 600 1000000 $seed ::: 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 >> $DIR_POP
done
exit 0
