from re import match
from typing import Optional, Dict, List
from itertools import chain


class Dir:
    def __init__(self, parent: Optional['Dir'] = None):
        self._parent = parent
        self._children: Dict[str, Dir] = {}
        self._file_sizes = 0

    @property
    def size(self) -> int:
        return self._file_sizes + sum(c.size for c in self._children.values())

    def get_dir_sizes(self) -> List[int]:
        return [self.size, *chain.from_iterable([[s for s in c.get_dir_sizes()]
                                                 for c in self._children.values()])]

    def add_dir(self, name: str):
        self._children[name] = Dir(parent=self)

    def add_file(self, file_size: int):
        self._file_sizes += file_size

    def cd(self, dir_name: str) -> 'Dir':
        if dir_name == '..':
            return self._parent
        return self._children[dir_name]


head = Dir()
curr_dir = head
for line in open('inp.txt').readlines():
    if cmd := match(r'\$\s*cd\s*(\S+)?', line):
        curr_dir = head if cmd.group(1) == '/' else curr_dir.cd(cmd.group(1))
    if dir_content := match(r'(\d+|dir)\s*(\S+)', line):
        if dir_content.group(1) == 'dir':
            curr_dir.add_dir(dir_content.group(2))
        else:
            curr_dir.add_file(int(dir_content.group(1)))

# First star
print(sum(dir_size for dir_size in head.get_dir_sizes()
          if dir_size <= 100_000))

# Second star
print(min(dir_size for dir_size in head.get_dir_sizes()
          if 70_000_000 - head.size + dir_size >= 30_000_000))
