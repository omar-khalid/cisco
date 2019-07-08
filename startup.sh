#!/bin/bash

export PYTHONPATH=/usr/local/lib/python3.5/site-packages

OUTPUT=raw
if [ "$2" ]
then
    OUTPUT=$2
fi

python movie_rating.py rating $1 --output $OUTPUT
