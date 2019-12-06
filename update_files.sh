#!/bin/bash

local=$(pwd)

pathzao="${local}/output"

files=$(ls ${pathzao})

for i in $files 
do 
    aws s3 cp "${pathzao}/${i}" "s3://stockmaurofs/output/${i}"
    rm "${pathzao}/${i}"
done
