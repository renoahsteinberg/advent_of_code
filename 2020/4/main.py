#!/usr/bin/env python

def part1(inp):
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID) (tread cid as optional)

    valid = 0

    for passport in inp:
        cnt = 0
        for val in passport:
            if val[:3] != 'cid':
                cnt += 1

        valid += 1 if cnt == 7 else 0

    return valid


def part2(inp):
    # byr 4 digits between 1920-2002
    # iyr 4 digits between 2010-2020
    # eyr 4 digits between 2020-2030
    # hgt number followed by
    # - cm between 150-193 
    # - in between 59-76
    # hcl valid hex color followed by 
    # ecl one of amb blu brn gry grn hzl oth
    # pid 9 digits including leading zeroes
    # cid ignored

    valid = 0

    for passport in inp:
        valid = True
        for val in passport:
            pass

if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/4/inp", "r") as f:
        inp = f.read().strip().split("\n\n")
        inplist = [passport.replace("\n", " ").split() for passport in inp]


    print(part1(inplist))
