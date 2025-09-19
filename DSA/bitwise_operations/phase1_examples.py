# Phase 1: The Fundamentals

# Introduction to Binary Representation
print(f"The binary representation of 13 is: {bin(13)}")

# Core Bitwise Operators

a = 13  # Binary: 1101
b = 10  # Binary: 1010

print(f"a = {a} ({bin(a)}), b = {b} ({bin(b)})")

# 1. AND (&)
# The result for a bit is 1 only if both corresponding bits are 1.
result_and = a & b
print(f"a & b: {result_and} ({bin(result_and)})")  # Expected: 8 (1000)

# 2. OR (|)
# The result for a bit is 1 if at least one of the corresponding bits is 1.
result_or = a | b
print(f"a | b: {result_or} ({bin(result_or)})")   # Expected: 15 (1111)

# 3. XOR (^)
# The result for a bit is 1 only if the corresponding bits are different.
result_xor = a ^ b
print(f"a ^ b: {result_xor} ({bin(result_xor)})")   # Expected: 7 (0111)
# 4. NOT (~)
# Inverts all the bits. Follows the formula ~x = -x - 1.
result_not_a = ~a
print(f"~a: {result_not_a}")  # Expected: -14
result_not_b = ~b
print(f"~b: {result_not_b}")  # Expected: -11
