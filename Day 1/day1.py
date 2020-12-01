from rich import print

# input file
file = open("Day 1\input.txt", "r")

# data
nums = [int(i) for i in file]
pt1Num1 = None
pt1Num2 = None
pt2Num1 = None
pt2Num2 = None
pt2Num3 = None

# loop through each one
for x in nums:
    for n in nums:
        # part 1 
        if x + n == 2020:
            pt1Num1 = x
            pt2Num2 = n
        for z in nums:
            # part 2
            if x + n + z == 2020:
                num1 = x
                num2 = n
                num3 = z

# print final answer
print(f"[magenta]Part 1 answer: [green]{num1*num2}")
print(f"[magenta]Part 2 answer: [green]{num1*num2*num3}")