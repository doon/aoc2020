#!/usr/bin/env python3
import re


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


def validate_between(val: str, start: int, end: int) -> bool:
    return start <= int(val) <= end


def validate_height(height: str) -> bool:
    valid = re.compile(r"(\d+)(cm|in)")
    matches = valid.match(height)
    if matches:
        (hgh, unit) = matches.groups()
        if unit == "cm":
            return validate_between(hgh, 150, 193)
        else:
            return validate_between(hgh, 59, 76)
    else:
        return False


def validate_ecl(color: str) -> bool:
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return color in valid_colors


def validate_pid(pid: str) -> bool:
    valid = re.compile(r"^\d{9}$")
    return bool(valid.match(pid))


def validate_hcl(hair: str) -> bool:
    valid = re.compile(r"^#[0-9a-f]{6}$")
    return bool(valid.match(hair))


def validate(passport) -> bool:
    return all(
        [
            validate_between(passport["byr"], 1920, 2002),
            validate_between(passport["iyr"], 2010, 2020),
            validate_between(passport["eyr"], 2020, 2030),
            validate_height(passport["hgt"]),
            validate_ecl(passport["ecl"]),
            validate_pid(passport["pid"]),
            validate_hcl(passport["hcl"]),
        ]
    )


for passport in passports:
    # first validate all the keys are here
    if all(k in passport for k in required_keys):
        if validate(passport):
            valid = valid + 1

print(f"Of {len(passports)} passports, {valid} are valid\n")
