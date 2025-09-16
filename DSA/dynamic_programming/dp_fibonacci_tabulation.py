
def fib_tab(n):
    """
    Calculates the nth Fibonacci number using tabulation (bottom-up DP).
    """
    # 1. Create a table to store results, size n+1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # table = [0] * (n + 1)

    # 2. Initialize base cases
    # table[1] = 1
    n_minus_2 = 0
    n_minus_1 = 1
    # 3. Iterate and fill the table from the bottom up
    for i in range(2, n + 1):
        # table[i] = table[i - 1] + table[i - 2]
        n_current = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = n_current

    # 4. The result is the last entry in the table
    return n_current


# Example usage:
n = 10
print(f"The {n}th Fibonacci number is: {fib_tab(n)}")
