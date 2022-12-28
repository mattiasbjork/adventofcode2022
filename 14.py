import re


def line_of_rocks(start, end):
    def direction(n0, n1):
        return -1 if n1 < n0 else 1 if n1 > n0 else 0
    rocks = set()
    delta_x = direction(start[0], end[0])
    delta_y = direction(start[1], end[1])
    x, y = start
    rocks.add(start)
    while (x, y) != end:
        x, y = delta_x + x, delta_y + y
        rocks.add((x, y))
    return rocks


# False for first star, True for second star
contains_floor = False
filename = 'inp.txt'

occupied = set()
x_max = y_max = 0
for line in open(filename).readlines():
    p0 = p1 = None
    rock_points = [tuple(map(int, m.groups()))
                   for m in re.finditer(r'(\d+),(\d+)', line)]
    while len(rock_points) > 0:
        p1 = rock_points.pop(0)
        if p0 is None:
            p0 = p1
        x_max, y_max = max(x_max, p1[0]), max(y_max, p1[1])
        occupied.update(line_of_rocks(p0, p1))
        p0 = p1
if contains_floor:
    occupied.update(line_of_rocks((0, y_max+2), (x_max+y_max, y_max+2)))


def down(p):
    return p[0], p[1]+1


def down_left(p):
    return p[0]-1, p[1]+1


def down_right(p):
    return p[0]+1, p[1]+1


def void(p):
    return p[1] > y_max+3


def reached_the_end(p):
    if contains_floor:
        return p in occupied
    return void(p)


sand_count = 0
sand = (500, 0)
while not reached_the_end(sand):
    if down(sand) not in occupied:
        sand = down(sand)
        continue
    if down_left(sand) not in occupied:
        sand = down_left(sand)
        continue
    if down_right(sand) not in occupied:
        sand = down_right(sand)
        continue
    occupied.add(sand)
    sand_count += 1
    sand = (500, 0)

print(sand_count)
