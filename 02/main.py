import re

# exo 2:
# you have a data, many line of many digit deparate by space (lvls).
# check the line who is "not valide" (thos who has a least one interval of more than 3 or less than 1, OR switching from increasing to decreasing).

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

def isLineValid(line: list) -> bool:
    values = re.findall('[0-9]{1,}', line)
    values = [ int(e) for e in values ]
    last_element = values[0]
    del values[0]
    is_increasing = values[0] > values[1]
    for e in values:
        dif = e - last_element
        current_is_increase = last_element > e

        # check all increase (or not).
        if is_increasing ^ current_is_increase:
            return False

        dif = abs(dif)
        if dif < 1 or dif > 3:
            return False

    return True

l = list(readInput())
l_valide = len([ None for line in l if isLineValid(line)])
print(l_valide)
