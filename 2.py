class Player:
    ROCK, PAPER, SCISSORS = 1, 2, 3

    outcomes = {ROCK:     {ROCK: 3, PAPER: 0, SCISSORS: 6},
                PAPER:    {ROCK: 6, PAPER: 3, SCISSORS: 0},
                SCISSORS: {ROCK: 0, PAPER: 6, SCISSORS: 3}}

    shape_from_symbol = {'X': ROCK,     'A': ROCK,
                         'Y': PAPER,    'B': PAPER,
                         'Z': SCISSORS, 'C': SCISSORS}

    points_from_symbol = {'X': 0, 'Y': 3, 'Z': 6}

    def __init__(self, symbol: str):
        self.shape = self.shape_from_symbol.get(symbol)
        self.points = self.points_from_symbol.get(symbol)

    def get_points_vs(self, opponent: 'Player', symbol_means_shape=True) -> int:
        if symbol_means_shape:
            return self.shape + self.outcomes[self.shape][opponent.shape]
        else:
            shape = [shape for shape, outcome in self.outcomes.items()
                     if outcome[opponent.shape] == self.points].pop()
            return shape + self.points


def get_points(file: str, symbol_means_shape: bool) -> int:
    points = 0
    for line in open(file).readlines():
        opponent, me = map(Player, line.split())
        points += me.get_points_vs(opponent, symbol_means_shape)
    return points


filename = 'inp.txt'
# First star
print(get_points(filename, symbol_means_shape=True))
# Second star
print(get_points(filename, symbol_means_shape=False))
