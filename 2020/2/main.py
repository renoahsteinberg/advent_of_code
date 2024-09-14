#!/usr/bin/env python

def part1(inp):
    # lowerbound-upperbound of letter k : password string
    # inp[x] = ['lowerbound-upperbound', 'k:', 'pw']
    
    # bounds = list(map(int, inp[0].split('-')))
    # letter = inp[1][0]
    # password = inp[2]

    valid_passwords = 0

    for pwg in inp:
        bounds = list(map(int, pwg[0].split('-')))
        letter = pwg[1][0]
        password = pwg[2]
        
        cnt = 0
        for l in password:
            if l == letter:
                cnt += 1
        
        if cnt < bounds[1] and cnt > bounds[0]:
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/2/inp", "r") as f:
        inp = [s.split() for s in f.readlines()]
    print(part1(inp))
