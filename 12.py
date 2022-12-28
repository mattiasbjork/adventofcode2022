class Node:
    def __init__(self, letter: str):
        self.letter = letter
        elevation_letter = {'S': 'a', 'E': 'z'}.get(letter, letter)
        self.elevation = ord(elevation_letter) - ord('a')
        self.adjacent: list[Node] = []


def find_minimum_steps_to_end(start_node: Node) -> int:
    steps = {start_node: 0}
    queue = [start_node]
    # Breadth-first search
    while len(queue) > 0:
        node = queue.pop(0)
        for next_node in node.adjacent:
            if next_node.elevation > node.elevation + 1 or next_node in steps:
                continue
            steps[next_node] = steps[node] + 1
            if next_node.letter == 'E':
                return steps[next_node]
            queue.append(next_node)


filename = 'inp.txt'
nodes = {}
for row, line in enumerate(open(filename).read().splitlines()):
    for col, symbol in enumerate(line):
        nodes[(row, col)] = Node(symbol)
for (row, col), n in nodes.items():
    for node_pos in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if node_pos in nodes:
            n.adjacent.append(nodes[node_pos])

# First star
print(next(find_minimum_steps_to_end(n) for n in nodes.values() if n.letter == 'S'))

# Second star
start_nodes = (find_minimum_steps_to_end(n) for n in nodes.values() if n.letter == 'a')
print(min(s for s in start_nodes if s is not None))
