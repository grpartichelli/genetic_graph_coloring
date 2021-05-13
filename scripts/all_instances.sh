#!/bin/bash

DIR_INST="../data/tunado.txt"
DIR_NC="../data/no_crossover.txt"
DIR_NM="../data/no_mutation.txt"

parallel -j 10 -k --bar python ../main.py {} 30 0.25 0.475 0.675 1800 10000000 123456 ::: ../cmb/cmb01 ../cmb/cmb02 ../cmb/cmb03 ../cmb/cmb04 ../cmb/cmb05 ../cmb/cmb06 ../cmb/cmb07 ../cmb/cmb08 ../cmb/cmb09 ../cmb/cmb10 >> $DIR_INST
parallel -j 10 -k --bar python ../main.py {} 30 0.25 0.000 0.675 1800 10000000 123456 ::: ../cmb/cmb01 ../cmb/cmb02 ../cmb/cmb03 ../cmb/cmb04 ../cmb/cmb05 ../cmb/cmb06 ../cmb/cmb07 ../cmb/cmb08 ../cmb/cmb09 ../cmb/cmb10 >> $DIR_NC
parallel -j 10 -k --bar python ../main.py {} 30 0.25 0.475 0.000 1800 10000000 123456 ::: ../cmb/cmb01 ../cmb/cmb02 ../cmb/cmb03 ../cmb/cmb04 ../cmb/cmb05 ../cmb/cmb06 ../cmb/cmb07 ../cmb/cmb08 ../cmb/cmb09 ../cmb/cmb10 >> $DIR_NM
