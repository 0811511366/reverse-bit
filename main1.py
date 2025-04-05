def reverse_bits(n, bit_size=5):
    result = 0
    for i in range(bit_size):
        bit = (n >> i) & 1
        result |=bit << (bit_size - 1 - i)
    return result

n = 14
reverse_n = reverse_bits(n)
print(f"Initial value: {n:08b}, reversed value: {reverse_n:08b}")