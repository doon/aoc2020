#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.read().splitlines()

# break into array of passports
passports = []
tmp = {}
for line in lines:
    if line == "":
        # store what we have and put into passports
        passports.append(tmp)
        tmp = {}
    else:
        # parse the line into k:v pairs
        tmp.update(dict(x.split(":") for x in line.split()))

# if tmp is not empty, include it.
if tmp is not {}:
    passports.append(tmp)

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid: int = 0

for passport in passports:
    if all(k in passport for k in required_keys):
        valid = valid + 1

print(f"Of {len(passports)} passports, {valid} are valid\n")
