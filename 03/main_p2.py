
import re

# exo 3 :
# same, but if there is a patern 'do()' or 'don't()' do not sum the mult after a don't.

# read data.
def readInput(path='03\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
arr2 = [ re.findall('(mul[(][0-9]{1,}[,][0-9]{1,}[)]|do[(][)]|don\'t[(][)])', line) for line in l ]

total = 0
is_do = True
for arr1 in arr2:
    for e in arr1:

        if e == 'do()' or e == 'don\'t()':
            if e == 'do()' and not is_do:
                is_do = True
            if e == 'don\'t()' and is_do:
                is_do = False
            continue

        if not is_do:
            continue

        values = re.findall('[0-9]{1,}', e)
        total += int(values[0]) * int(values[1])

print(total)
