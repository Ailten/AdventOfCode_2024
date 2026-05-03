
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
            current_index_facing = guard['facing']

            yl = 1
            while True:
                yl_eval = guard['pos'][1] + yl * (
                    1 if (current_index_facing == 1) else
                    -1 if (current_index_facing == 3) else
                    0
                )
                if yl_eval > len(map):
                    break

                # TODO: verify if the pos is out of a first rock.

                xl = 1
                while True:
                    xl_eval = guard['pos'][0] + xl * (
                        1 if (current_index_facing == 0) else
                        -1 if (current_index_facing == 2) else
                        0
                    )
                    if xl_eval > len(map[yl]):
                        break

                    # TODO: verify if the pos is out of a first rock.

                    # do eval rectangle.
                    rectangle_pos = [
                        guard['pos'],
                        (xl_eval, yl_eval),
                        (guard['pos'][0], yl_eval),
                        (xl_eval, guard['pos'][1])
                    ]
                    rectangle_pos.sort(key=lambda p: p[0]*10000+p[1])
                    count_rock = 0
                    pos_empty_rock = None
                    for iii in range(4):
                        pos_rock = (
                            rectangle_pos[iii][0] + direction[][0],
                            rectangle_pos[iii][1] + direction[][1]
                        )
                        if map[pos_rock[1]][pos_rock[0]] == '#':
                            count_rock += 1
                        else:
                            pos_empty_rock = pos_rock
                    if count_rock == 3:
                        pass  # find a rect valid (maybe).


                yl += 1

            # still WIP.


            if guard['facing'] == 0 or guard['facing'] == 2:
                yl = 1
                while True:
                    yl_eval = pos_loop_a[1] + yl * next_direction[1]
                    if yl_eval >= len(map):
                        break
                    if map[yl_eval][guard['pos'][0]] == '#':  # find second rock.
                        pos_loop_b = map[yl_eval][guard['pos'][0]]

                    yl += 1
            else:


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