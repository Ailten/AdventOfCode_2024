import re
import math

# exo 2:
# same, but one error by line can be allow, if the number wo

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

#def isLineValid(line: list, is_has_jocker: bool=False) -> int:
#    
#    values = re.findall('[0-9]{1,}', line)
#    values = [ int(e) for e in values ]
#
#    if is_has_jocker:
#        if isLineValid(' '.join([ str(e) for e in values[:1] + values[2:] ])) == 0:
#            return 0
#        if isLineValid(' '.join([ str(e) for e in values[1:] ])) == 0:
#            return 0
#        if isLineValid(' '.join([ str(e) for e in values[:-1] ])) == 0:
#            return 0
#    
#    last_element = values[0]
#    is_increasing = values[0] < values[1]
#    for i in range(1, len(values)):
#        e = values[i]
#        dif = e - last_element
#        current_is_increase = last_element < e
#
#        # check all increase (or not).
#        if is_increasing != current_is_increase:
#            if is_has_jocker:
#                is_has_jocker = False
#                continue
#            return 1
#
#        dif = abs(dif)
#        if dif < 1 or dif > 3:
#            if is_has_jocker:
#                is_has_jocker = False
#                continue
#            return 2
#        
#        last_element = e
#
#    return 0



def isLineValid(line: str, is_jocker: bool=False):
    values = re.findall('[0-9]{1,}', line)
    values = [ int(e) for e in values ]

    is_increase = values[0] < values[1]

    for i in range(1, len(values)):
        dif = abs(values[i] - values[i-1])
        if dif < 1 or dif > 3:
            if is_jocker:
                if isLineValid(' '.join([ str(e) for e in values[:i]+values[i+1:] ])):
                    return True
                if isLineValid(' '.join([ str(e) for e in values[:i+1]+values[i+2:] ])):
                    return True
                if i <= 2 and isLineValid(' '.join([ str(e) for e in values[1:] ])):
                    return True
                if i <= 2 and isLineValid(' '.join([ str(e) for e in values[:1]+values[2:] ])):
                    return True
            return False

        is_current_incr = values[i-1] < values[i]
        if is_current_incr != is_increase:
            if is_jocker:
                if isLineValid(' '.join([ str(e) for e in values[:i]+values[i+1:] ])):
                    return True
                if isLineValid(' '.join([ str(e) for e in values[:i+1]+values[i+2:] ])):
                    return True
                if i <= 2 and isLineValid(' '.join([ str(e) for e in values[1:] ])):
                    return True
                if i <= 2 and isLineValid(' '.join([ str(e) for e in values[:1]+values[2:] ])):
                    return True
            return False
        
    return True
    



l = list(readInput())
l = [
    '1 1 2 3 4 5',
    '1 2 3 4 5 5',
    '5 1 2 3 4 5',
    '1 4 3 2 1',
    '1 6 7 8 9',
    '1 2 3 4 3',
    '9 8 7 6 7',
    '7 10 8 10 11'
]
l_valide = [ f'{line}' for line in l if isLineValid(line, True) ]
print(len(l_valide))

# 332
# 373 to low
# 998 to height
# 764 to height  # FIXME, still not valide.
# 375 x (?)
# 381 x (?)
# 397 x
# 388 x
# 393
# 397 x

# (expect 398)