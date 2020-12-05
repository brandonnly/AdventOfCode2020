from rich import print
import rich.traceback

rich.traceback.install()

inputText = [i for i in open("Day 5\input.txt", "r")]

def get_row(row_string):
    start = 0
    end = 127
    mid = None
    for x in row_string:
        mid = (start + end) // 2
        
        if x == 'F':
            end = mid - 1
        elif x == 'B':
            start = mid + 1
    
    return mid


def get_col(col_string):
    start = 0
    end = 7
    mid = None
    for x in col_string:
        mid = (start + end) // 2
        if x == 'L':
            end = mid - 1
        elif x == 'R':
            start = mid + 1

    # on last loop it wont update mid so make it 0 if -1
    if mid < 0:
        return 0
    else:
        return mid


output = open("Day 5\Output", "w")

def get_id(row, col):
    output.write(f"{row}, {col} = {row * 8 + col} \n")
    return row * 8 + col


def get_consecutive(ids, mid):
    index = ids.index(mid)
    if ids[index-1] == mid - 1 and ids[index+1] == mid + 1:
        return mid

ids = [get_id(get_row(x[:7]), get_col(x[7:])) for x in inputText]
ids.sort()
print(f"Part 1 Answer: {max(ids)}")
print(f"Part 2 Answer: {[x for x in ids if get_consecutive(ids, x) is not None]}") # answer was 554 idk i just threw around stuff
