import re

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

def compareTwoNum(a, b, rules) -> bool:
    r = next(( r for r in rules if (r[0] == a or r[1] == a) and (r[0] == b or r[1] == b) ), None)
    if r == None:
        return True
    if r[0] == a:
        return True
    return False


def buildRulesArr(arr: list, is_recurcive: bool=False):
    r = [arr[0][0], arr[0][1]]
    del arr[0]

    while len(arr) != 0:
        is_find = False
        under = next(( e for e in arr if e[1] == r[0] ), None)
        if under != None:
            r = [under[0]] + r
            arr.remove(under)
            is_find = True
        upper = next(( e for e in arr if e[0] == r[len(r)-1] ), None)
        if upper != None:
            r.append(upper[1])
            arr.remove(upper)
            is_find = True

        if not is_find:
            break

    if is_recurcive:
        return r

    while len(arr) > 0:
        arr_copy = arr.copy()

        sub_r = buildRulesArr(arr, is_recurcive=True)
        i_start = next(( i for i in range(len(r)) if r[i] == sub_r[0]), None)
        i_end = next(( i for i in range(len(r)) if r[i] == sub_r[len(sub_r)-1]), None)

        if i_start == None or i_end == None:
            arr = arr_copy[1:] + arr_copy[:1]
            continue

        sub_r_range = r[i_start:i_end+1]
        if len(set(sub_r_range) - set(sub_r)) == 0:  # all previous range contain new range (and more).
            r = r[:i_start] + sub_r + r[i_end+1:]
        elif len(set(sub_r) - set(sub_r_range)) == 0:  # all replace is already fit (and less).
            continue
        else:
            arr = arr_copy[1:] + arr_copy[0:1]
            continue

    return r




l = readInput()
#l = [
#    [(1, 2), (2, 3), (3, 4), (5,7), (6,8), (7,9), (5,8), (5,6), (8,9), (7,8), (4,5), (6,7), (7,8)],
#    [
#        [1,3,2],
#        [3,1,2],
#        [2,1,3],
#    ]
#]
rules = l[0]
lines = l[1]
r = buildRulesArr(list(rules))
r_dico = { r[i]:i for i in range(len(r)) }

total = 0
for li in lines:
    
    li.sort(key=lambda li_e: r_dico[li_e])

    # get middle line.
    total += li[len(li) // 2]

print(total)


# 10436  (x) to height
# 11027  (x) to height.

# TODO: re create a list of "ordered value" based on rules, and use it as rules, instead of picking the exact rules array.
# to catch the index value of eatch num in the array ref.



