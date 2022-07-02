#!/bin/bash

for dir in */
do
    cd $dir
    echo -n "Checking ${dir%*/} ... "
    files=0
    for lang in py go
    do
        for sol in *.${lang}
        do
            # Check if file exists
            [ -f "$sol" ] || break
            case $lang in 
            py)
                # Execute Python file
                python3 "$sol"
                ;;
            go)
                # Execute Go file
                go run "$sol"
                ;;
            esac

            # If execution failure, exit
            if [[ $? -ne 0 ]]
            then
                exit 1
            fi
            let files++
        done
    done
    echo "Done. Checked ${files} solutions."
    cd ..
done
