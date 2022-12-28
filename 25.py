symbol_to_number = {'0': 0, '1': 1, '2': 2, '=': -2, '-': -1}
number_to_symbol = list(symbol_to_number)
base = len(symbol_to_number)


def decode_snafu(snafu: str) -> int:
    decimal_number = 0
    for i, c in enumerate(reversed(snafu)):
        decimal_number += symbol_to_number[c] * base**i
    return decimal_number


def encode_snafu(decimal_number: int) -> str:
    def to_subtract(decimal_index: int):
        return sum(int(2 * base**(p-1)) for p in range(decimal_index+1))
    s = number_to_symbol[decimal_number % base]
    i = 1
    while (threshold := base**i - to_subtract(i)) <= decimal_number:
        num = (decimal_number + (threshold - 1)) // (base**i)
        s += number_to_symbol[num % base]
        i += 1
    return ''.join(reversed(s))


filename = 'inp.txt'
numbers = [decode_snafu(line) for line in
           open(filename).read().splitlines()]
print(encode_snafu(sum(numbers)))
