#!/usr/bin/env python3

import typing as t


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


seats: t.List[int]

with open("input.txt") as f:
    lines = f.read().splitlines()
# get all the filled seats
seats = set([find_seat(line)[2] for line in lines])
# get all the seats
allseats = set(range(0, 128 * 8))
# get the unfilled seats
missing_seats = list(allseats - seats)

for idx, seat_id in enumerate(missing_seats):
    try:
        if (
            missing_seats[idx - 1] != seat_id - 1
            and missing_seats[idx + 1] != seat_id + 1
        ):
            # the seat_ids on both sides of us filled
            print(f"my seat is {seat_id}")
    except IndexError:
        continue
