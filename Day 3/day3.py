from rich import print
import rich.traceback
import math

rich.traceback.install()

area = [i for i in open("Day 3\input.txt", "r")]


def get_slope(area, deltaX, deltaY):
    trees = 0
    xCoord = 0

    for n in range(0, len(area), deltaY):
        if area[n][xCoord % len(area[0].strip())] == '#':
            trees += 1
        xCoord += deltaX

    return trees


deltas = [(1,1), (3,1), (5,1), (7,1), (1,2)]
pt2 = []
for x in deltas:
    pt2.append(get_slope(area, x[0], x[1]))


print(f"Part 1 Answer: [green]{get_slope(area, deltas[1][0], deltas[1][1])}")
print(f"Part 2 Answer: [green]{math.prod(pt2)}")