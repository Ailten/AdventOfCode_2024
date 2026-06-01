
#
#



import re

def readInput(path='07\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield [ int(n) for n in re.findall(r'[0-9]{1,}', l.strip()) ]


data = readInput()

good_result = 0

for d in data:
    result = d.pop(0)
    ope = [0] * (len(d) - 1)
    while True:

        current_result = d[0]
        id = 1
        for o in ope:
            match o:
                case 0:  # +.
                    current_result += d[id]
                case 1:  # *.
                    current_result *= d[id]
            id += 1
        if current_result == result:
            good_result += result
            break
        
        is_overange_op = True
        for i in range(len(ope)-1, -1, -1):
            if ope[i] != 1:
                ope[i] += 1
                for j in range(i+1, len(ope)):
                    ope[j] = 0
                is_overange_op = False
                break
        if is_overange_op:
            break

print(good_result)

# 416 to low.

