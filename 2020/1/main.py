def part1(nums, target):
    # find the number-pair that adds up to 2020 in O(n)
    # similar to the two-sum problem on LeetCode
    
    hash_table = {}

    for i in range(len(nums)):
        if nums[i] in hash_table.keys():
            return nums[hash_table[nums[i]]] * nums[i]

        hash_table[target - nums[i]] = i
    return 0


def part2(nums, target):
    # find the number-triplet that adds up to 2020
    # similar to the three-sum problem on LeetCode
    # probably solvable with a two pointer approach / binary search
    # nums[0] + nums[1] + nums[2] = target
    
    nums = sorted(nums)

    for i in range(len(nums)-1):
        new_target = target - nums[i]
        left = i+1
        right = len(nums)-2
        while left <= right:
            if (nums[left] + nums[right]) == new_target:
                return nums[left] * nums[right] * nums[i]
            elif (nums[left] + nums[right]) > new_target:
                right -= 1
            else:
                left += 1
    return 0


if __name__ == "__main__":
    with open("/home/clay/projects/advent_of_code/2020/input", "r") as f:
        nums = list(map(int, [x.rstrip() for x in f.readlines()]))
        
    # nums = [1721,979,366,299,675,1456]

    print(part1(nums, 2020))
    print(part2(nums, 2020))
