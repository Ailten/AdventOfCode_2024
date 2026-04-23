import re
import math

# exo 2:
# you have a data, many line of many digit deparate by space (lvls).
# check the line who is "not valide" (thos who has a least one interval of more than 3 or less than 1, OR switching from increasing to decreasing).

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

def isLineValid(line: list) -> int:
    values = re.findall('[0-9]{1,}', line)
    values = [ int(e) for e in values ]
    last_element = values[0]
    del values[0]
    is_increasing = values[0] > values[1]
    for e in values:
        dif = e - last_element
        current_is_increase = last_element > e

        # check all increase (or not).
        if is_increasing != current_is_increase:
            return 1

        dif = abs(dif)
        if dif < 1 or dif > 3:
            return 2

    return 0

l = list(readInput())
l = l[:6]  # FIXME: first row return "gap over range" but it should return "decrease not allow"
l_valide = ([ f'{line} -> {isLineValid(line)}' for line in l ])  # if isLineValid(line) == 0
print('\n'.join(l_valide))

# 3 ? x
