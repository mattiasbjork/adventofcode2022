class Knot:
    def __init__(self, tails_to_add=0):
        self.x = self.y = 0
        self.tail = None
        if tails_to_add > 0:
            self.tail = Knot(tails_to_add-1)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other: 'Knot'):
        return self.x == other.x and self.y == other.y

    def _vector(self, other: 'Knot'):
        return self.x - other.x, self.y - other.y

    def _direction(self, other: 'Knot'):
        return tuple(n // abs(n) if n != 0 else n
                     for n in self._vector(other))

    def _distance(self, other: 'Knot') -> int:
        return max(abs(n) for n in self._vector(other))

    def move(self, delta_x: int, delta_y: int):
        self.x, self.y = self.x + delta_x, self.y + delta_y
        if self.tail and self._distance(self.tail) > 1:
            self.tail.move(*self._direction(self.tail))

    def last_tail(self):
        if self.tail is None:
            return self
        return self.tail.last_tail()


filename = 'inp.txt'
first_star = True

head = Knot(tails_to_add=1 if first_star else 9)
tail = head.last_tail()
visited = set()

direction = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
for pos, steps in [line.split() for line in open(filename).readlines()]:
    x, y = direction.get(pos)
    for _ in range(int(steps)):
        head.move(x, y)
        visited.add(tail)
print(len(visited))
