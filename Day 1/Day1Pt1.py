from rich import print

# input file
file = open("Day 1\input.txt", "r")

# variables
three = []
four = []
num1 = 0
num2 = 0

# feedback settings
feedback = False

# get from file
for i in file:
    if len(i) == 5:
        three.append(int(i.strip()))
    else:
        four.append(int(i.strip()))

# loop through each one
for x in three:
    for n in four:
        # feedback for loops
        if feedback:
            print(f"[magenta]Adding [green]{x} [magenta]and [green]{n} [magenta]to get [green]{x+n}")

        # set vars if their sum is 2020
        if x + n == 2020:
            num1 = x
            num2 = n
            break

# return answer
print(f"[magenta]The answer is: [green]{num1*num2}")