#!/bin/bash

for dir in */
do 
    cd $dir
    for sol in *.py
    do
        [ -f "$sol" ] || break
        python3 "$sol"
        if [[ $? -ne 0 ]]
        then
            exit 1
        fi
    done

    for sol in *.go
    do
        [ -f "$sol" ] || break
        go run "$sol"
        if [[ $? -ne 0 ]]
        then
            exit 1
        fi
    done

    cd ..
done
