
# guard patrol.
# now count eatch empty spot can be replace by an obstacl to create guard infinit loop.

# read data.
def readInput(path='06\\input.txt'):
    with open(path, 'r') as f:
        for l in f:
            yield l.strip()



def findGuardPos(map: list[str]) -> tuple[int, int]:

    char_search = '^'

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == char_search:
                return (x, y)
            
    raise Exception('no guard found')



def gardWalkCount(map: list[str], guard: dict) -> int:
    direction = [(0,-1), (1,0), (0,1), (-1,0)]

    cellules_obs_loop = { guard['pos'] }
    while True:

        new_pos_guard = (
            guard['pos'][0] + direction[guard['facing']][0],
            guard['pos'][1] + direction[guard['facing']][1]
        )

        if (
            (new_pos_guard[0] < 0) or
            (new_pos_guard[0] >= len(map[0])) or
            (new_pos_guard[1] < 0) or
            (new_pos_guard[1] >= len(map))
        ):
            break

        char_at_pos = map[new_pos_guard[1]][new_pos_guard[0]]
        if char_at_pos == '#':

            # verify loop.  (TODO: try eatch rectangle in a direction, to verify if can create a new loop block).
            #pos_loop_a = guard['pos']
            #for yl in range()


            guard["facing"] = ( guard["facing"] + 1 ) % len(direction)
            continue

        guard['pos'] = new_pos_guard

    return len(cellules_obs_loop) - 1



map = list(readInput())
guard_pos = findGuardPos(map)
guard = {
    "facing": 0,
    "pos": guard_pos
}
print(gardWalkCount(map, guard))

# 5444 (V)