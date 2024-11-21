# Interleaving String Analyzer

## Overview
A Python script to determine if one string can be formed by interleaving two other strings, with advanced substring tracking capabilities.

## Key Features
- Validates string interleaving possibilities
- Counts potential interleaving methods
- Uses dynamic programming algorithm
- Supports file-based input/output processing

## Requirements
- Python 3.x
- Standard Python libraries

## Usage
```bash
python assignment3.py <input_file>
```

### Input File
Create a text file with three lines:
1. First source string (s1)
2. Second source string (s2)
3. Target interleaved string (s3)

### Example Input
```
abc
def
adbecf
```

## Algorithm Details
- Dynamic programming for efficient processing
- Backtracking to explore interleaving combinations
- Constraints on substring distribution
- Time complexity: O(m*n)
- Space complexity: O(m*n)

## Output
Generates an output file showing:
- Interleaving possibility
- Number of interleaving methods
- Example substring splits

## Limitations
- Performance may decrease with very long strings
- Assumes valid input strings
- Returns first valid interleaving method if multiple exist

## Potential Applications
- String manipulation
- Pattern matching
- Sequence analysis

## Error Handling
- Validates input file arguments
- Checks string length compatibility
- Provides usage instructions



## Author
Siva Rama Krishna Prasad Changala
```
