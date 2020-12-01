from rich import print

# input file
file = open("Day 1\input.txt", "r")

# variables
nums = []
num1 = 0
num2 = 0
num3 = 0

# feedback settings
feedback = False

# get from file
for i in file:
    nums.append(int(i))

# loop through each one
for x in nums:
    for n in nums:
        for z in nums:
            # feedback printing for loop updates
            if feedback:
                print(f"[magenta]Adding [green]{x} [magenta]and [green]{n} [magenta]to get [green]{x+n}")

            # set vars if their sum is 2020
            if x + n + z == 2020:
                num1 = x
                num2 = n
                num3 = z

# print final answer
print(f"[magenta]The answer is: [green]{num1*num2*num3}")