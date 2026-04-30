import re
import copy

# exo 05.
# order pages.
# take many line of number, and a block of many line of combinaison of 2 number (for set order).
# re make the first block in order, and sum all middle number of eatch line.

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

#def compareTwoNum(a, b, rules) -> bool:
#    r = next(( r for r in rules if (r[0] == a or r[1] == a) and (r[0] == b or r[1] == b) ), None)
#    if r == None:
#        return True
#    if r[0] == a:
#        return True
#    return False
#
#
#def buildRulesArr(arr: list, is_recurcive: bool=False):
#    r = [arr[0][0], arr[0][1]]
#    del arr[0]
#
#    while len(arr) != 0:
#        print(r)
#
#        is_find = False
#        under = next(( e for e in arr if e[1] == r[0] ), None)
#        if under != None:
#            r = [under[0]] + r
#            arr.remove(under)
#            is_find = True
#        upper = next(( e for e in arr if e[0] == r[len(r)-1] ), None)
#        if upper != None:
#            r.append(upper[1])
#            arr.remove(upper)
#            is_find = True
#
#        if not is_find:
#            break
#
#    if is_recurcive:
#        return r
#
#    while len(arr) > 0:
#        arr_copy = arr.copy()
#
#        sub_r = buildRulesArr(arr, is_recurcive=True)
#        i_start = next(( i for i in range(len(r)) if r[i] == sub_r[0]), None)
#        i_end = next(( i for i in range(len(r)) if r[i] == sub_r[len(sub_r)-1]), None)
#
#        if i_start == None or i_end == None:
#            arr = arr_copy[1:] + arr_copy[:1]
#            continue
#
#        sub_r_range = r[i_start:i_end+1]
#        if len(set(sub_r_range) - set(sub_r)) == 0:  # all previous range contain new range (and more).
#            r = r[:i_start] + sub_r + r[i_end+1:]
#        elif len(set(sub_r) - set(sub_r_range)) == 0:  # all replace is already fit (and less).
#            continue
#        else:
#            arr = arr_copy[1:] + arr_copy[0:1]
#            continue
#
#    return r


def total(lines: list, rules: list):
    
    total = 0

    for line in lines:
        line_un_sort = copy.deepcopy(line)

        is_ordered = True
        for i in range(0, len(line) - 1):
            for j in range(i+1, len(line)):
                v_i = line[i]
                v_j = line[j]

                rule_find = next([ r for r in rules if (
                    (r[1] == line[i] and r[0] == line[j])
                ) ].__iter__(), None)
                if rule_find == None:
                    continue
                else:
                    is_ordered = False
                    break

            if not is_ordered:
                break
        
        if is_ordered:
            total += line[len(line) // 2]

    return total


    





l = readInput('05\\input.txt')
rules = l[0]
lines = l[1]


print(total(lines, rules))


# 10436  (x) to height
# 11027  (x) to height.
# 4872 (V)



