filename = 'inp.txt'
elves = [sum(map(int, e.split('\n'))) for e in open(filename).read().split('\n\n')]
print(max(elves))  # First star
print(sum(sorted(elves)[-3:]))  # Second star
