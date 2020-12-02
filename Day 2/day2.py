from rich import print
import rich.traceback
import re

rich.traceback.install()

# input data
passwords = [i for i in open("Day 2\input.txt", "r")]
valid1 = 0
valid2 = 0

# loop through paswords
for x in passwords:
    # split string
    string = re.split('-| |:', x.strip())
    # get from string
    mini = int(string[0])
    maxi = int(string[1])
    char = string[2]
    pw = string[4]

    # PART 1
    if pw.count(char) >= mini and pw.count(char) <= maxi:
        valid1 += 1

    # PART 2
    if pw[mini-1] == char and not pw[maxi-1] == char \
        or not pw[mini-1] == char and pw[maxi-1] == char:
        valid2 += 1

# return answer
print(f"Part 1 Answer: [green]{valid1}")
print(f"Part 2 Answer: [green]{valid2}")