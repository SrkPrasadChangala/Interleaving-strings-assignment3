#!/bin/bash

# Loop through all Output files containing "Output" in their name
for output_file in *Output*.txt
do
  # Construct the corresponding input file name by replacing "Output" with "Input"
  input_file="${output_file/Output/Input}"

  # Check if the corresponding input file exists
  if [[ -f "$input_file" ]]; then
    echo "Contents of $input_file:"
    cat "$input_file"
    echo "----------------------------------------"
    echo "Contents of $output_file:"
    cat "$output_file"
    echo "========================================"
  else
    echo "Input file for $output_file not found."
    echo "========================================"
  fi
done

