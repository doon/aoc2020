#!/usr/bin/env/python3

from itertools import combinations

# read in all the numbers
with  open("input.txt") as f:
    lines = list(map(int,f.read().splitlines()))

#get all the pairs
all_pairs = list(combinations(lines,2))
for (x,y) in all_pairs:
    if x+y == 2020:
        print(x*y)
        exit()
