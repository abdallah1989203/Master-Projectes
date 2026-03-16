#!/bin/bash

# Set the root directory path
root_dir="/data/yolds"

# Loop over all directories starting with "00233_"
for dir in $root_dir/00233_*; do
    # Check if it's a directory
    if [ -d "$dir" ]; then
        # Go to the "labels" subdirectory
        labels_dir="$dir/labels"
        # Check if the "labels" subdirectory exists
        if [ -d "$labels_dir" ]; then
            # Loop over all text files in the "labels" subdirectory
            for file in $labels_dir/*.txt; do
                # Check if the file contains a negative number
                if grep -q "-" $file; then
                    echo "Negative number found in file: $file"
                fi
            done
        fi
    fi
done
