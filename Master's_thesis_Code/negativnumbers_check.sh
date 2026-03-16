#!/bin/bash

# Check for negative numbers in a given list of arguments
for number in "$@"
do
    if [ "$number" -lt 0 ]; then
        echo "Negative number found: $number"
    fi
done