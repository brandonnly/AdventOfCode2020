from rich import print
import rich.traceback
import re

rich.traceback.install()

inputText = [i for i in open("Day 4\input.txt", "r")]

passports = []
temp = {}

# add all files to dictionary
for x in inputText:
    line = x.strip().split(" ")

    # check if valid passport and continue
    if '' in line:
        if 'byr' in temp and 'iyr' in temp and 'eyr' \
            in temp and 'hgt' in temp and 'hcl' in temp \
                and 'ecl' in temp and 'pid' in temp:
            passports.append(temp)
        temp.clear()
        continue

    # add to temp passport until new line
    for n in line:
        key = n[0:3]
        value = n[4:]

        # set key value if valid
        if valid(key, value):
            temp[key] = value

def valid(key, value):
    valid = False

    if key == "byr":
        valid = 1920 <= int(value) <= 2020
    elif key == "iyr":
        if 2010 <= int(value) <= 2020: valid = True
    elif key == "eyr":
        if 2020 <= int(value) <= 2030: valid = True
    elif key == "eyr":
        if 2020 <= int(value) <= 2030: valid = True
    elif key == "hgt":
        if value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193: valid = True
        if value[-2:] == "in" and 59 <= int(value[:-2]) <= 76: valid = True
    elif key == "hcl":
        if re.compile(r"^#[0-9a-f]{6}$").match(value): valid = True
    elif key == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            valid = True
    elif key == "pid":
        if re.compile(r"^\d{9}$").match(value): valid = True

    return valid

# ADD 1 IF LAST PASS IS INVALID - I HAVE NO CLUE WHY
print(f"Part 1 Answer: {len(passports)}")