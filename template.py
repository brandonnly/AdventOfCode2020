from rich import print
import rich.traceback

rich.traceback.install()

input = [i for i in open("Day {DAY_NUM}\input.txt", "r")]