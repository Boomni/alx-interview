# 0x01. Lockboxes

## Project Overview

This project covers a Python algorithm problem involving locked boxes. The goal is to implement a method called `canUnlockAll(boxes)` that determines if all the boxes can be opened.

> This is possibly a coding  interview question. :)

## Project Details

### Description

You have `n` number of locked boxes in front of you, each sequentially numbered from 0 to n - 1, and each box may contain keys to the other boxes. Your task is to implement a method `canUnlockAll(boxes)` that determines if all the boxes can be opened.

### Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The code should be documented
- The code should use the PEP 8 style (version 1.7.x)
- All files must be executable

### Tasks

#### 0. Lockboxes

You need to implement a method `canUnlockAll(boxes)` that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

#### Example Usage

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False

## Project Author

> Jonathan Boomni

