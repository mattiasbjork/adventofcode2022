from collections import deque


def num_of_characters(file: str, marker_length: int):
    buffer = deque(maxlen=marker_length)
    for num, character in enumerate(open(file).read(), start=1):
        buffer.append(character)
        if len(buffer) == len(set(buffer)) == marker_length:
            return num


filename = 'inp.txt'
print(num_of_characters(filename, 4))  # First star
print(num_of_characters(filename, 14))  # Second star
