def count_set_bits(n):
    """
    Counts the number of set bits (1s) in the binary representation of an integer.
    This implementation uses the Brian Kernighan's algorithm.

    The core of the algorithm is the expression `n & (n - 1)`, which clears
    the least significant set bit. The loop continues until the number becomes 0,
    and the number of iterations equals the number of set bits.

    Args:
        n: A non-negative integer.

    Returns:
        The number of set bits in the integer's binary representation.
    """
    if n < 0:
        # The logic for negative numbers depends on the assumed bit-length.
        # For simplicity in interviews, this is often constrained to non-negative integers.
        print("This function is designed for non-negative integers.")
        return 0

    count = 0
    while n > 0:
        # This operation clears the least significant '1' bit.
        n = n & (n - 1)
        count += 1
    return count

# --- Examples ---

# Example 1: 13 is 1101 in binary
num1 = 13
result1 = count_set_bits(num1)
print(f"The number of set bits in {num1} ({bin(num1)}) is: {result1}") # Expected: 3

# Example 2: 7 is 0111 in binary
num2 = 7
result2 = count_set_bits(num2)
print(f"The number of set bits in {num2} ({bin(num2)}) is: {result2}") # Expected: 3

# Example 3: 16 is 10000 in binary
num3 = 16
result3 = count_set_bits(num3)
print(f"The number of set bits in {num3} ({bin(num3)}) is: {result3}") # Expected: 1

# Example 4: 0 is 0 in binary
num4 = 0
result4 = count_set_bits(num4)
print(f"The number of set bits in {num4} ({bin(num4)}) is: {result4}") # Expected: 0

# Example 5: A larger number
num5 = 2147483647 # 2^31 - 1, all 31 bits are set
result5 = count_set_bits(num5)
print(f"The number of set bits in {num5} is: {result5}") # Expected: 31
