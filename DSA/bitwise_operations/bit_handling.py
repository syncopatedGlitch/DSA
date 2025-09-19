def update_bit(number, i, bit_value):
    """
    Updates the i-th bit of a number to a given value (0 or 1).

    Args:
        number: The integer to modify.
        i: The bit position to update (0-indexed from the right).
        bit_value: The new value for the bit (must be 0 or 1).

    Returns:
        The new number with the i-th bit updated.
    """
    # First, create a mask to clear the i-th bit.
    # 1 << i creates a mask like 00100.
    # ~ (1 << i) inverts it to 11011, which has a 0 at the i-th position.
    mask = ~(1 << i)

    # Clear the i-th bit by ANDing with the mask.
    # This ensures the i-th bit is 0, and all other bits are unchanged.
    cleared_number = number & mask

    # Now, create the value to place at the i-th bit.
    # bit_value (0 or 1) is shifted to the i-th position.
    value_to_place = bit_value << i

    # OR the cleared number with the value to place.
    # If bit_value was 1, this sets the i-th bit.
    # If bit_value was 0, this does nothing, leaving the cleared bit as 0.
    result = cleared_number | value_to_place

    return result

# --- Examples ---


# Example 1: Clear the 3rd bit of 13 (1101)
# Expected output: 5 (0101)
num1 = 13
pos1 = 3
val1 = 0
result1 = update_bit(num1, pos1, val1)
print(f"Updating bit {pos1} of {num1} ({bin(num1)})\
      to {val1} -> {result1} ({bin(result1)})")


# Example 2: Set the 2nd bit of 10 (1010)
# Expected output: 14 (1110)
num2 = 10
pos2 = 2
val2 = 1
result2 = update_bit(num2, pos2, val2)
print(f"Updating bit {pos2} of {num2} ({bin(num2)})\
      to {val2} -> {result2} ({bin(result2)})")

# Example 3: Set a bit that is already set (should not change)
# Set the 3rd bit of 13 (1101) to 1
# Expected output: 13 (1101)
num3 = 13
pos3 = 3
val3 = 1
result3 = update_bit(num3, pos3, val3)
print(f"Updating bit {pos3} of {num3} ({bin(num3)})\
      to {val3} -> {result3} ({bin(result3)})")

# Example 4: Clear a bit that is already clear (should not change)
# Clear the 1st bit of 13 (1101) to 0
# Expected output: 13 (1101)
num4 = 13
pos4 = 1
val4 = 0
result4 = update_bit(num4, pos4, val4)
print(f"Updating bit {pos4} of {num4} ({bin(num4)})\
      to {val4} -> {result4} ({bin(result4)})")
