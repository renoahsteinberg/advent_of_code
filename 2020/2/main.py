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
       
        # obv the bounds need to be <= and >=
        # bad commit for that!
        if cnt <= bounds[1] and cnt >= bounds[0]:
            valid_passwords += 1

    return valid_passwords


def part2(inp):
    # exactly ONE of these positions must contain the letter, other occurences are irrelevant
    # No concept of the "index zero"
    valid_passwords = 0

    for pwg in inp:
        indices = list(map(int, pwg[0].split('-')))
        letter = pwg[1][0]
        password = pwg[2]

        # Using XOR for "exaclty one" in case two occurences of the same letter on both indices
        if (password[indices[0] - 1] == letter)^(password[indices[1] - 1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/2/inp", "r") as f:
        inp = [s.split() for s in f.readlines()]
    print(part1(inp))
    print(part2(inp))
