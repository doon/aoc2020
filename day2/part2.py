#!/usr/bin/env python3

def check_password(policy:str, password:str) -> bool:
    (count,letter)  = policy.strip().split()
    (x,y) = count.split("-")
    # policy is password[x] == letter XOR password[y] == letter
    # python is 0 based so need to subtract 1 
    idx1,idx2 = int(x)-1, int(y)-1
    
    # remove WS
    password = password.strip()
    return (password[idx1] == letter) ^ (password[idx2] == letter)
   


# input is form x-y ?: password
with open("input.txt") as f:
    lines = f.read().splitlines()
valid_passwords = 0

for line in lines: 
    (policy, password) = line.split(":")
    if(check_password(policy,password)):
        valid_passwords = valid_passwords + 1
   
print(valid_passwords)