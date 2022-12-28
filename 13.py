import json
from typing import List, Union
from itertools import zip_longest
from functools import cmp_to_key
from math import prod


def compare(left: Union[List, int, None],
            right: Union[List, int, None]) -> int:
    if left is None:
        return -1
    if right is None:
        return 1
    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip_longest(left, right):
            if (res := compare(a, b)) != 0:
                return res
        return 0
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if left < right:
        return -1
    if left > right:
        return 1
    return 0


filename = 'inp.txt'
pairs = [[json.loads(line) for line in lines.split('\n')]
         for lines in open(filename).read().split('\n\n')]

# First star
print(sum(n for n, pair in enumerate(pairs, 1) if
          compare(*(p for p in pair)) == -1))

# Second star
packets = [p for pair in pairs for p in pair]
decoder_keys = [[[2]], [[6]]]
packets.extend(decoder_keys)
packets.sort(key=cmp_to_key(compare))
print(prod(packets.index(i) + 1 for i in decoder_keys))
