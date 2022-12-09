class PriorityCounter:
    def __init__(self, num_of_groups: int):
        self.num_of_groups = num_of_groups
        self.lines = []
        self.priority = 0

    def add_badge(self, letter: str):
        priority = ord(letter)
        priority -= 96 if ord(letter) >= ord('a') else 38
        self.priority += priority

    def add_line(self, line: str):
        self.lines.append(line)
        if len(self.lines) == self.num_of_groups:
            unique_letter = set.intersection(*(set(line) for line in self.lines)).pop()
            self.lines = []
            self.add_badge(unique_letter)


def priority_sum(file: str, split_rucksack: bool):
    p = PriorityCounter(2 if split_rucksack else 3)
    for line in open(file).read().splitlines():
        if split_rucksack:
            middle_index = len(line) // 2
            p.add_line(line[:middle_index])
            p.add_line(line[middle_index:])
        else:
            p.add_line(line)
    return p.priority


filename = 'inp.txt'
# First star
print(priority_sum(filename, split_rucksack=True))

# Second star
print(priority_sum(filename, split_rucksack=False))
