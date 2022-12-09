from re import match


def get_number_of_overlaps(file: str, must_fully_contain: bool):
    count = 0
    for line in open(file).readlines():
        x0, x1, y0, y1 = map(int, match(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups())
        if must_fully_contain:
            condition = x0 <= y0 <= y1 <= x1 or y0 <= x0 <= x1 <= y1
        else:
            condition = x0 <= y1 <= x1 or y0 <= x1 <= y1
        if condition:
            count += 1
    return count


filename = 'inp.txt'

# First star
print(get_number_of_overlaps(filename, must_fully_contain=True))

# Second star
print(get_number_of_overlaps(filename, must_fully_contain=False))
