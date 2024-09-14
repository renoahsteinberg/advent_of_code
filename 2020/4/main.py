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

    #return inp


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/4/test_input", "r") as f:
        # generate input
        # iterate over each line seperate, append each line to an array called current Passport
        # if line is empty, start new array
        
        # disgusting ahh solution

        inp = [x.split() for x in f.readlines()] 
        inplist = []
        tmplist = []
        i = 0
        while i < len(inp)-1:
            if not inp[i]:
                i += 1
                inplist.append(tmplist)
                tmplist = []
            tmplist += inp[i]
            i += 1

    print(part1(inplist))
