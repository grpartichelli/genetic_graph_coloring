#!/bin/bash

SEEDS=(123456 212392 310293 429312 523123 612372 702938 811239 919203 102938 112930 123290 139248 149302 159320)

DIR_POP="../data/population.txt"
DIR_MUT="../data/mutation.txt"
DIR_ELI="../data/elitism.txt"
DIR_CROSS="../data/crossover.txt"

for seed in "${SEEDS[@]}"
do

    echo $seed Population ...
    echo $seed >> $DIR_POP
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb04 {} 0.25 0.2 0.2 60 1000000 $seed ::: 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 100 >> $DIR_POP
    echo $seed Elitism...
    echo $seed >> $DIR_ELI
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb04 20 {} 0.2 0.2 60 100000000 $seed ::: 0 0.025 0.05 0.075 0.1 0.125 0.15 0.175 0.2 0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4 0.425 0.45 0.475 0.5 0.525 0.55 0.575 0.6 0.625 0.65 0.675 0.7 0.725 0.75 0.775 0.8 0.825 0.85 0.875 0.9 0.925 0.95 0.975 1 >> $DIR_ELI
    echo $seed Crossover...
    echo $seed >> $DIR_CROSS
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb04 20 0.25 {} 0.2 60 100000000 $seed ::: 0 0.025 0.05 0.075 0.1 0.125 0.15 0.175 0.2 0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4 0.425 0.45 0.475 0.5 0.525 0.55 0.575 0.6 0.625 0.65 0.675 0.7 0.725 0.75 0.775 0.8 0.825 0.85 0.875 0.9 0.925 0.95 0.975 1 >> $DIR_CROSS
    echo $seed Mutation...
    echo $seed >> $DIR_MUT
    parallel -j 10 -k --bar python ../main.py ../cmb/cmb04 20 0.25 0.2 {} 60 100000000 $seed ::: 0 0.025 0.05 0.075 0.1 0.125 0.15 0.175 0.2 0.225 0.25 0.275 0.3 0.325 0.35 0.375 0.4 0.425 0.45 0.475 0.5 0.525 0.55 0.575 0.6 0.625 0.65 0.675 0.7 0.725 0.75 0.775 0.8 0.825 0.85 0.875 0.9 0.925 0.95 0.975 1 >> $DIR_MUT
done
exit 0
