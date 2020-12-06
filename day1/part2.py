#!/usr/bin/env/python3

from itertools import combinations

# read in all the numbers
with  open("input.txt") as f:
    lines = list(map(int,f.read().splitlines()))

#get all the pairs
all_pairs = list(combinations(lines,3))
for (x,y,z) in all_pairs:
    if x+y+z == 2020:
        print(x*y*z)
        exit()
