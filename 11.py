import re
from collections import deque
from math import prod, lcm
from typing import Optional, Tuple


class Monkey:
    item_value_lcm: Optional[int] = None

    def __init__(self, items_held: list[int], operation: str, divisor: int,
                 monkey_num_if_true: int, monkey_num_if_false: int):
        self.items_held = deque(items_held)
        self.operation = operation
        self.divisor = divisor
        self.monkey_num_if_true = monkey_num_if_true
        self.monkey_num_if_false = monkey_num_if_false
        self.inspection_counter = 0

    def inspect(self) -> Tuple[int, int]:
        self.inspection_counter += 1
        old = self.items_held.pop()
        item_level = eval(self.operation)
        if self.item_value_lcm:
            item_level %= self.item_value_lcm
        else:
            item_level //= 3
        if item_level % self.divisor == 0:
            return self.monkey_num_if_true, item_level
        return self.monkey_num_if_false, item_level


filename = 'inp.txt'
first_star = True

monkeys = {}
for m in re.finditer(r'Monkey (\d+):'
                     r'\s*Starting items: (.+)'
                     r'\s*Operation: new = (.+)'
                     r'\s*Test: divisible by (\d+)'
                     r'\s*If true: throw to monkey (\d+)'
                     r'\s*If false: throw to monkey (\d+)',
                     open(filename).read(), re.MULTILINE):
    num = int(m.group(1))
    items = [int(i) for i in m.group(2).split(',')]
    args = map(int, m.groups()[3:])
    monkeys[num] = Monkey(items, m.group(3), *args)

if not first_star:
    Monkey.item_value_lcm = lcm(*(m.divisor for m in monkeys.values()))

for n in range(20 if first_star else 10_000):
    for m in monkeys.values():
        while len(m.items_held) > 0:
            monkey_num, item = m.inspect()
            monkeys[monkey_num].items_held.append(item)

print(prod(sorted(m.inspection_counter for m in monkeys.values())[-2:]))
