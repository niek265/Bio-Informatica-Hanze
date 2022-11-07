# SNP_severity_calculator
Calculates severity scores for SNPs at a given position in a multi fasta protein alignment file.

## Installation
This script was created in Python 3.10, it needs to be installed. 

## Input
The program takes a multiple sequence alignment file. 
This can be created using a program like Muscle.

## Required Packages
The following Python packages are required:
- numpy
- blosum
- pandas

## Usage
To use the SNP Severity Check, use `python3 SNP_severity_calculator` in the terminal followed by the arguments you want to use.
Use `--help` for more information

```
usage: snp_severity_calculator.py [-h] [-p Position] [-matrix {45,50,62,80,90}] [--all] F

Calculates severity scores for SNPs at given positions of a multiple sequence alignment.

positional arguments:
  F                     Path to the multiple sequence alignment file to be loaded (MultiFasta only).

options:
  -h, --help            show this help message and exit
  -p Position           Position for the SNP to trigger a mutation.
  -matrix {45,50,62,80,90}
                        BLOSUM matrix to use when calculating scores. Options: 45,50,62,80 and 90.(Default: 62)
  --all                 Generates the scores for all positions and prints them to the console with the data.(Default: False)
  ```

## Examples:  
Only calculate the score for position one in the alignment
> $python3 SNP_severity_calculator.py msa.txt -p 1

Calculate scores for all positions and save them to CSV
> $python3 SNP_severity_calculator.py msa.txt --all

