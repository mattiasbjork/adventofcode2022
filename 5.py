from re import match, finditer
from collections import defaultdict, deque

filename = 'inp.txt'
stacks = defaultdict(deque)
first_star = True

for line in open(filename).readlines():
    if move_command := match(r'move (\d+) from (\d+) to (\d+)', line):
        amount, source, destination = map(int, move_command.groups())
        if amount == 1 or first_star:
            for _ in range(amount):
                stacks[destination].append(stacks[source].pop())
        else:
            d = deque(stacks[source].pop() for _ in range(amount))
            while len(d) > 0:
                stacks[destination].append(d.pop())
    else:
        for number, space in enumerate(finditer(r'(.{4})+?|(.{3}$)', line), start=1):
            if crate := match(r'.*?\[(\S)].*?', space.group(0)):
                stacks[number].appendleft(crate.group(1))

print(''.join(stacks[i].pop() for i in range(1, len(stacks)+1)))
