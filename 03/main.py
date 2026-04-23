import re

# exo 3 :
# 

# read data.
def readInput(path='02\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
l = [ re.findall('mul([0-9]{1,},[0-9]{1,})', line) for line in l ]

total = 0
for line in l:
    for m in line:
        values = re.findall('[0-9]{1,}', m)
        total += int(values[0]) * int(values[1])

print(total)

# fix : return zero.