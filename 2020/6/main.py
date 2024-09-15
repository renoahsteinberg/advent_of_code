#!/usr/bin/env python


def part1(inp):
    amnt_answers = 0
    for group in inp:
        answerset = set()
        for answer in group:
            for letter in answer:
                answerset.add(letter)
        amnt_answers += len(answerset)
    return amnt_answers


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/6/inp", "r") as f:
        inp = [x.split() for x in f.readlines()]
        inplist, tmplist, i = [], [], 0
        while i < len(inp):
            if not inp[i]:
                inplist.append(tmplist)
                tmplist = []
            tmplist += inp[i]
            i += 1
        inplist.append(tmplist)

    print(part1(inplist))

