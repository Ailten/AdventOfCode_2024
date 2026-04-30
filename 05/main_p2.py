import re
import copy

# exo 05.
# order pages.
# same, but take only those who is not ordered, order it, and sum the midle number.

def readInput(path='05\\input.txt'):
    output = [ set(), [] ]
    with open(path, 'r') as f:
        is_first_block = True
        for l in f:
            l = l.strip()
            if l == '':
                is_first_block = False
                continue
            if is_first_block:
                num = [ int(n) for n in re.findall('[0-9]{1,}', l) ]
                output[0] |= { ( num[0], num[1] ) }
            else:
                num = [ int(n) for n in re.findall('[0-9]{1,}', l) ]
                output[1].append(num)
    return output


def total(lines: list, rules: list):
    
    total = 0

    for line in lines:
        line_un_sort = copy.deepcopy(line)

        while True:
            is_swap = False
            for i in range(0, len(line) - 1):
                for j in range(i+1, len(line)):

                    rule_find = next([ r for r in rules if (
                        (r[0] == line[i] and r[1] == line[i+1]) or
                        (r[1] == line[i] and r[0] == line[i+1])
                    ) ].__iter__(), None)
                    if rule_find == None:
                        continue
                    if rule_find[0] == line[i+1] and rule_find[1] == line[i]:
                        (line[i], line[i+1]) = (line[i+1], line[i])
                        is_swap = True
        
            if not is_swap:
                break

        if line_un_sort != line:
            total += line[len(line) // 2]

    return total


    





l = readInput()
rules = l[0]
lines = l[1]


print(total(lines, rules))


# 5564 (V)



