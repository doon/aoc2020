#!/usr/bin/env python3

from math import prod

# input is ...##..###..##
# repeats if we go out of bounds

with open("input.txt") as f:
    lines = f.read().splitlines()


def compute_tree_collisions(slope_x: int, slope_y: int):

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
        y = y + slope_y
        x = x + slope_x

    return trees


# print the product of all collisions
print(
    prod(
        [
            compute_tree_collisions(1, 1),
            compute_tree_collisions(3, 1),
            compute_tree_collisions(5, 1),
            compute_tree_collisions(7, 1),
            compute_tree_collisions(7, 2),
        ]
    )
)
