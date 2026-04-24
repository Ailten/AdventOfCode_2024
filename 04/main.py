
# exo 04.
# find word 'xmas' on every direction in a grid of letter.

# read data.
def readInput(path='04\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
word_search = 'XMAS'
match_count = 0
len_y = len(l)
len_x = len(l[0])
for y in range(len_y - len(word_search) + 1):
    is_last_y = y == len_y - len(word_search)
    for x in range(len_x - len(word_search) + 1):
        is_last_x = x == len_x - len(word_search)
        
        str_try = l[y][x] + l[y][x+1] + l[y][x+2] + l[y][x+3]
        if str_try == word_search:
            match_count += 1
        str_try = str_try[::-1]
        if str_try == word_search:
            match_count += 1
            
        str_try = l[y][x] + l[y+1][x] + l[y+2][x] + l[y+3][x]
        if str_try == word_search:
            match_count += 1
        str_try = str_try[::-1]
        if str_try == word_search:
            match_count += 1
            
        str_try = l[y][x] + l[y+1][x+1] + l[y+2][x+2] + l[y+3][x+3]
        if str_try == word_search:
            match_count += 1
        str_try = str_try[::-1]
        if str_try == word_search:
            match_count += 1
            
        str_try = l[y][x+3] + l[y+1][x+2] + l[y+2][x+1] + l[y+3][x]
        if str_try == word_search:
            match_count += 1
        str_try = str_try[::-1]
        if str_try == word_search:
            match_count += 1

        if is_last_y:
            for y_sup in range(1, 4):
                str_try = l[y+y_sup][x] + l[y+y_sup][x+1] + l[y+y_sup][x+2] + l[y+y_sup][x+3]
                if str_try == word_search:
                    match_count += 1
                str_try = str_try[::-1]
                if str_try == word_search:
                    match_count += 1

        if is_last_x:
            for x_sup in range(1, 4):
                str_try = l[y][x+x_sup] + l[y+1][x+x_sup] + l[y+2][x+x_sup] + l[y+3][x+x_sup]
                if str_try == word_search:
                    match_count += 1
                str_try = str_try[::-1]
                if str_try == word_search:
                    match_count += 1



print(match_count)

# 2519 (x) to low.
# 2543