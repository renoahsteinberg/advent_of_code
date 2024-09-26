#!/usr/bin/env python


# So i can call the function with various slopes
def part1(inp, right, down):
    length = len(inp[0]) - 1

    amt_trees = 0
    
    idx2r = 0
    for idx in range(0, len(inp), down):
        right_idx = (idx2r * right) % length

        # modulo, so there wouldnt be an out of bounds error when right_idx is bigger than the lists length

        if inp[idx][right_idx] == '#':
            amt_trees += 1
        idx2r += 1

    return amt_trees 


def part2(inp, slopes):
    # all slopes
    # Right 1, Down 1,
    # Right 3, Down 1,
    # Right 5, Down 1,
    # Right 7, Down 1,
    # Right 1, Down 2
    solution = 1

    for slope in slopes:
        sol = part1(inp, slope[0], slope[1])
        solution = solution * sol

    return solution


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/3/inp", "r") as f:
        inp = f.readlines()

    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    print(part1(inp, 3, 1))
    print(part2(inp, slopes))
