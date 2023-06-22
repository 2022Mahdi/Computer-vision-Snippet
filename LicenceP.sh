#!/bin/bash

# Step 1: Count lines in each text file
wc_output=$(wc -l labels/*.txt)

# Step 2: Parse output to extract file name and line count
while read -r line; do
  file=$(echo "$line" | awk '{print \$2}')
  count=$(echo "$line" | awk '{print \$1}')

  # Step 3: Check if line count is not equal to 8
  if [ "$count" -ne 8 ]; then
    # Delete the file
    rm "$file"
  fi
done <<< "$wc_output"
