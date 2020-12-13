#!/usr/bin/env python3

import typing as t


def get_all(group: t.List[t.Set[str]]) -> t.Set[str]:
    answered = group[0]
    for g in group[1:]:
        answered = answered.intersection(g)
    return answered


# get test data
with open("input.txt") as f:
    lines = f.read().splitlines()

group: t.List[t.Set[str]] = []
groups: t.List[t.Set[str]] = []


for line in lines:
    if line == "":
        groups.append(get_all(group))
        group = []
    else:
        group.append(set(list(line)))

# add the final group
group.append(set(list(line)))
groups.append(get_all(group))

print(sum([len(g) for g in groups]))
