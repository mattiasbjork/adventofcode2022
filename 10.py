import re

filename = 'inp.txt'

signal_strength = 0
crt = ''
crt_width = 40
cycle = 0
x = 1

for line in open(filename).readlines():
    add_x = 0  # noop
    if m := re.match(r'addx (-?\d+)', line):
        add_x = int(m.group(1))
    for _ in range(1 if add_x == 0 else 2):
        crt += '#' if cycle % crt_width in [x-1, x, x+1] else '.'
        cycle += 1
        if (cycle + 20) % crt_width == 0:
            signal_strength += cycle * x
    x += add_x

# First star
print(signal_strength)

# Second star
for row_index in range(len(crt) // crt_width):
    start_pixel = row_index * crt_width
    print(crt[start_pixel: start_pixel + crt_width])
