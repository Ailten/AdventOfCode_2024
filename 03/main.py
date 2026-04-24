import re

# exo 3 :
# take a file text, into there are a patern 'mul(1,1)' with two number, take all the num and multiply, return the sum of all.

# read data.
def readInput(path='03\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
arr2_of_mul = [ re.findall('mul[(][0-9]{1,}[,][0-9]{1,}[)]', line) for line in l ]

total = 0
for arr1_mul in arr2_of_mul:
    for mul in arr1_mul:
        values = re.findall('[0-9]{1,}', mul)
        total += int(values[0]) * int(values[1])

print(total)