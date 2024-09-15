#!/usr/bin/env python


def part1(inp):
    # first 7 letters (row)
    # last 3 letters (column)

    # f(front), b(back), r(right), l(left)

    max = 0
    
    for k in inp:
        row = k[:8]
        col = k[7:]
        
        lr, rr = 0, 127
        lc, rc = 0, 7
        for i in k:
            midrow = (lr + rr) // 2
            midcol = (lc + rc) // 2

            if i == 'B':
                lr = midrow
            elif i == 'F':
                rr = midrow
            elif i == 'R':
                lc = midcol
            elif i == 'L':
                rc = midcol

            uniqueid = midrow *8 + midcol
            if uniqueid >= max:
                max = uniqueid

    return max


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/5/inp", "r") as f:
        inp = [r.strip() for r in f.readlines()]

    print(part1(inp))   
