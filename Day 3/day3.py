from rich import print
import rich.traceback

rich.traceback.install()

area = [i for i in open("Day 3\input.txt", "r")]

trees1 = 0
xCoord = 0

for n in range(0, len(area)):
    if area[n][xCoord % len(area[0].strip())] == '#':
        trees1 += 1
    xCoord += 3


print(f"Part 1 Answer: [green]{trees1}")