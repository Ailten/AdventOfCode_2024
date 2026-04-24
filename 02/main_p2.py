import re
import math

# exo 2:
# same, but one error by line can be allow, if the number wo

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

def isLineValid(line: list, is_has_jocker: bool=False) -> int:
    
    values = re.findall('[0-9]{1,}', line)
    values = [ int(e) for e in values ]
    last_element = values[0]
    is_increasing = values[0] < values[1]
    for i in range(1, len(values)):
        e = values[i]
        dif = e - last_element
        current_is_increase = last_element < e

        # check all increase (or not).
        if is_increasing != current_is_increase:
            if is_has_jocker:
                if i == 1 and isLineValid(line[1:]) != 0:
                    return 0
                is_has_jocker = False
                continue
            return 1

        dif = abs(dif)
        if dif < 1 or dif > 3:
            if is_has_jocker:
                if i == 1 and isLineValid(line[1:]) != 0:
                    return 0
                is_has_jocker = False
                continue
            return 2
        
        last_element = e

    return 0

l = list(readInput())
l_valide = len([ None for line in l if isLineValid(line, True) == 0])
print(l_valide)

# 332
# 373 to low
# 998 to height
# 764 to height  # FIXME, still not valide.