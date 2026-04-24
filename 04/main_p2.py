
# exo 04 (p2).
# same but search about "mas cros" as :
# M.S
# .A.
# M.S

def readInput(path='04\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()

l = list(readInput())
word_search = 'MAS'
center_letter = word_search[len(word_search)//2]
match_count = 0
len_y = len(l)
len_x = len(l[0])
for y in range(1, len_y - 1):
    for x in range(1, len_x - 1):
        char = l[y][x]
        if char != center_letter:
            continue

        corner_char = [
            l[y-1][x-1],
            l[y-1][x+1],
            l[y+1][x-1],
            l[y+1][x+1]
        ]

        is_one_diago = (
            corner_char[0] == word_search[0] and corner_char[3] == word_search[2]
            or
            corner_char[0] == word_search[2] and corner_char[3] == word_search[0]
        )
        if_secon_diago = (
            corner_char[1] == word_search[0] and corner_char[2] == word_search[2]
            or
            corner_char[1] == word_search[2] and corner_char[2] == word_search[0]
        )
        if is_one_diago and if_secon_diago:
            match_count += 1

print(match_count)

# 1848 (x) to low.
# 1930