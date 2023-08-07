# Minimum Operations

## Description

This repository contains a Python script that solves the "Minimum Operations" problem. Given a number `n`, the script calculates the fewest number of operations needed to result in exactly `n` H characters in a text file. The text editor can execute only two operations: Copy All and Paste.

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## How to Use

1. Clone this repository to your local machine.
2. Change into the project directory:

```bash
cd 0x02-minimum_operations
```

Run the Python script with the desired input to find the minimum number of operations required. For example:

```
./0-main.py
```
Example

Given n = 12, the script will output:

Min # of operations to reach 12 char: 7

### Author
> Jonathan Boomni