#!/usr/bin/env python3

import typing as t

valid: dict[str, t.Tuple[int, int, int]] = {
    "BFFFBBFRRR": (70, 7, 567),
    "FFFBBBFRRR": (14, 7, 119),
    "BBFFBBFRLL": (102, 4, 820),
}


def split_list(l: t.List[int]) -> t.Tuple[t.List[int], t.List[int]]:
    half = len(l) // 2
    return l[:half], l[half:]


def find_seat(seat_string: str) -> t.Tuple[int, int, int]:
    rows = list(range(0, 128))
    cols = list(range(0, 8))
    for row in seat_string[0:7]:
        if row == "F":
            rows = split_list(rows)[0]
        else:
            rows = split_list(rows)[1]
    for col in seat_string[7:]:
        if col == "L":
            cols = split_list(cols)[0]
        elif col == "R":
            cols = split_list(cols)[1]

    r = rows[0]
    c = cols[0]
    s = r * 8 + c
    return (r, c, s)


for (seatstr, tup) in valid.items():
    seat = find_seat(seatstr)
    if seat == tup:
        print(f"{seatstr} good")
    else:
        print(f"{seatstr} bad\ngot {seat}\nexpected {tup}\n")

with open("input.txt") as f:
    lines = f.read().splitlines()

max: int = 0
for line in lines:
    seat_idx = find_seat(line)[2]
    if seat_idx > max:
        max = seat_idx

print(f"Max Seat = {max}")