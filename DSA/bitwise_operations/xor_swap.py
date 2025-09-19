def demonstrate_xor_swap():
    """
    Demonstrates swapping the values of two integer variables using
    the XOR bitwise operator without needing a third temporary variable.

    The XOR swap algorithm is a classic interview trick based on the
    properties of XOR:
    1. x ^ x = 0
    2. x ^ 0 = x
    3. x ^ y = y ^ x (Commutative)
    4. (x ^ y) ^ z = x ^ (y ^ z) (Associative)
    """
    a = 13  # Binary: 1101
    b = 10  # Binary: 1010

    print("--- Before Swap ---")
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    print("\nPerforming 3-step XOR swap...\n")

    # Step 1: a becomes the XOR of the original a and b
    # a' = a ^ b
    a = a ^ b
    # a is now 7 (0111)

    # Step 2: b becomes the XOR of the new a and the original b
    # b' = a' ^ b = (a ^ b) ^ b = a ^ (b ^ b) = a ^ 0 = a (the original a)
    b = a ^ b
    # b is now 13 (1101)

    # Step 3: a becomes the XOR of the new a and the new b
    # a'' = a' ^ b' = (a ^ b) ^ a = (a ^ a) ^ b = 0 ^ b = b (the original b)
    a = a ^ b
    # a is now 10 (1010)

    print("--- After Swap ---")
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")


if __name__ == "__main__":
    demonstrate_xor_swap()
