import re
import math

# exo 2:
# same, but one error by line can be allow, if the number wo

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()


def isLineValid(line: str, is_jocker: bool=False) -> bool:
    values = re.findall('[0-9]{1,}', line)
    values = [ int(e) for e in values ]

    if is_jocker:
        if isLineValid(' '.join([ str(e) for e in values[1:] ])):
            return True
        if isLineValid(' '.join([ str(e) for e in values[:-1] ])):
            return True

    is_increase = values[0] < values[1]

    for i in range(1, len(values)):
        dif = abs(values[i] - values[i-1])
        if dif < 1 or dif > 3:
            if is_jocker:
                if isLineValid(' '.join([ str(e) for e in values[:i]+values[i+1:] ])):
                    return True
                if isLineValid(' '.join([ str(e) for e in values[:i-1]+values[i:] ])):
                    return True
            return False

        is_current_incr = values[i-1] < values[i]
        if is_current_incr != is_increase:
            if is_jocker:
                if isLineValid(' '.join([ str(e) for e in values[:i]+values[i+1:] ])):
                    return True
                if isLineValid(' '.join([ str(e) for e in values[:i-1]+values[i:] ])):
                    return True
            return False
        
    return True
    



l = list(readInput())
l_valide = [ f'{line}' for line in l if isLineValid(line, True) ]
print(len(l_valide))

