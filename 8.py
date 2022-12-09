class Forest:
    def __init__(self, file: str):
        self.trees = []
        for tree_line in open(file).read().splitlines():
            self.trees.append([int(t) for t in tree_line])
        self.width = len(self.trees[0])
        self.height = len(self.trees)

    def north(self, row: int, col: int):
        return reversed([self.trees[r][col] for r in range(0, row)])

    def south(self, row: int, col: int):
        return [self.trees[r][col] for r in range(row+1, self.height)]

    def west(self, row: int, col: int):
        return reversed([self.trees[row][c] for c in range(0, col)])

    def east(self, row: int, col: int):
        return [self.trees[row][c] for c in range(col+1, self.width)]

    def tree_lines(self, row: int, col: int):
        return [x(row, col) for x in [self.north, self.south, self.east, self.west]]

    def is_visible(self, row: int, col: int):
        if not (0 < row < self.height-1 and 0 < col < self.width-1):
            return True  # On the edge
        return any(all(n < self.trees[row][col] for n in t) for t in self.tree_lines(row, col))

    def get_scenic_score(self, row: int, col: int):
        scenic_score = 1
        for treeline in self.tree_lines(row, col):
            count = 1
            for count, tree in enumerate(treeline, 1):
                if tree >= self.trees[row][col]:
                    break
            scenic_score *= count
        return scenic_score

    def get_highest_scenic_score(self):
        return max([self.get_scenic_score(r, c) for r in range(self.height) for c in range(self.width)])

    def get_number_of_visible_trees(self):
        return [self.is_visible(r, c) for r in range(self.height) for c in range(self.width)].count(True)


filename = 'inp.txt'
f = Forest(filename)

# First star
print(f.get_number_of_visible_trees())

# Second star
print(f.get_highest_scenic_score())
