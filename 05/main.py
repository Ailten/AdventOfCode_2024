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


l = readInput()
l = [
    [(1, 2), (2, 3), (3, 4)],
    [
        [1,3,2],
        [3,1,2],
        [2,1,3],
    ]
]
rules = l[0]
lines = l[1]
total = 0
for li in lines:
        
    print('--')
    print(li)

    while True:

        is_a_change = False
        for i in range(1, len(li)):
            i_minus = i - 1
            if not compareTwoNum(li[i_minus], li[i], rules):
                is_a_change = True
                (li[i_minus], li[i]) = (li[i], li[i_minus])

        if not is_a_change:
            break
        
    print(li)

    # get middle line.
    total += li[len(li) // 2]

print(total)


# 10436  (x) to height

# TODO: re create a list of "ordered value" based on rules, and use it as rules, instead of picking the exact rules array.
# to catch the index value of eatch num in the array ref.



