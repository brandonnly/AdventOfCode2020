from rich import print
import rich.traceback

rich.traceback.install()

inputText = [i for i in open("Day {DAY_NUM}\input.txt", "r")]