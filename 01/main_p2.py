
import re

# exo 1 (p2):
# take the left number one by one, and sum the amount of time it figure theme self on right list.

# read data.
def readInput(path='01\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
left_int = [ int(re.search('^[0-9]{1,}', e).group(0)) for e in l ]
right_int = [ int(re.search('[0-9]{1,}$', e).group(0)) for e in l ]

sum_int = 0
for li in left_int:
    sum_int += len([ None for ri in right_int if ri == li ]) * li

print(sum_int)