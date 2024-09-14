#!/usr/bin/env python

def part1(inp):
    # always go 3 right and 1 down
    length = len(inp[0]) - 1 # assuming that len is universal
    
    amt_trees = 0

    for idx in range(len(inp)):
        current_idx = (idx * 3) % length 
        # modulo len, because when increments of 3 is bigger than the len of string, we jump back to the start
        # idx * 3 because each 3 increment per iteration
        # i use idx as a way to go 1 down each iteration
        if inp[idx][current_idx] == '#':
            amt_trees += 1

    return amt_trees


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/3/inp", "r") as f:
        inp = f.readlines()

    print(part1(inp))
