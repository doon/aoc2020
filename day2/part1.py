#!/usr/bin/env python3

def check_password(policy:str, password:str) -> bool:
    (count,letter)  = policy.strip().split()
    (s,f) = count.split("-")
    return int(s) <= password.count(letter) <= int(f)
   


# input is form x-y ?: password
with open("input.txt") as f:
    lines = f.read().splitlines()
valid_passwords = 0

for line in lines: 
    (policy, password) = line.split(":")
    if(check_password(policy,password)):
        valid_passwords = valid_passwords + 1
   
print(valid_passwords)