#!/usr/bin/env python3

import typing as t

# get test data
with open("input.txt") as f:
    lines = f.read().splitlines()

group: t.List[str] = []
groups: t.List[t.Set[str]] = []

for line in lines:
    if line == "":
        groups.append(set(group))
        group = []
    else:
        group.extend(list(line))

# add the final group
group.extend(list(line))
groups.append(set(group))

print(sum([len(g) for g in groups]))
