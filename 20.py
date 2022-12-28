from collections import deque


def get_grove_coordinates(file: str, decryption_key=1, mix_amount=1):
    initial_sequence = [int(line)*decryption_key for
                        line in open(file).readlines()]
    length = len(initial_sequence)
    indices = deque([i for i in range(length)])
    for _ in range(mix_amount):
        for current_index in range(length):
            steps = initial_sequence[current_index]
            index_to_remove = indices.index(current_index)
            del indices[index_to_remove]
            indices.rotate(-steps)
            indices.insert(index_to_remove, current_index)
    final_sequence = [initial_sequence[i] for i in indices]
    i = final_sequence.index(0)
    return sum(final_sequence[(i+n) % length]
               for n in [1000, 2000, 3000])


filename = 'inp.txt'
# First star
print(get_grove_coordinates(filename))
# Second star
print(get_grove_coordinates(filename, decryption_key=811589153, mix_amount=10))
