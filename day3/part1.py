#!/usr/bin/env python3

# input is ...##..###..##
# repeats if we go out of bounds

with open("input.txt") as f:
    lines = f.read().splitlines()

x: int = 0
y: int = 0
trees: int = 0
bottom: int = len(lines)

while y < bottom:
    # if we go off the right side it repeats
    l = len(lines[y])
    if x >= l:
        x = x - l

    if not lines[y][x] == ".":
        trees = trees + 1
    y = y + 1
    x = x + 3
print(trees)
