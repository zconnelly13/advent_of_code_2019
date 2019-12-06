# from collections import defaultdict


with open('input.txt') as fp:
    lines = fp.readlines()
    lines[0] = lines[0].split(',')
    lines[1] = lines[1].split(',')

"""
lines = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4'],
]
"""

"""
lines = [
    ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
]
"""

spots_hit = {}

x = 0
y = 0
steps = 0
for move in lines[0]:
    # parse input
    direction = move[0]
    amount = int(move[1:])

    # get new points
    if direction == 'R':
        points = [(x+i, y) for i in range(1, amount+1)]
        x += amount
    if direction == 'L':
        points = [(x-i, y) for i in range(1, amount+1)]
        x -= amount
    if direction == 'U':
        points = [(x, y+i) for i in range(1, amount+1)]
        y += amount
    if direction == 'D':
        points = [(x, y-i) for i in range(1, amount+1)]
        y -= amount

    # apply them to the map
    for point in points:
        steps += 1
        spots_hit[point] = (steps, 0)

x = 0
y = 0
steps = 0
for move in lines[1]:
    # parse input
    direction = move[0]
    amount = int(move[1:])

    # get new points
    if direction == 'R':
        points = [(x+i, y) for i in range(1, amount+1)]
        x += amount
    if direction == 'L':
        points = [(x-i, y) for i in range(1, amount+1)]
        x -= amount
    if direction == 'U':
        points = [(x, y+i) for i in range(1, amount+1)]
        y += amount
    if direction == 'D':
        points = [(x, y-i) for i in range(1, amount+1)]
        y -= amount

    # apply them to the map
    for point in points:
        steps += 1
        if spots_hit.get(point) is not None:
            spots_hit[point] = (spots_hit[point][0], steps)


# Part I
# print(min([abs(k[0]) + abs(k[1]) for k, v in spots_hit.items() if v >= 2]))

# Part II
print(min([sum(v) for v in spots_hit.values() if v[1] != 0]))
