
# Using a dictionary as a cache
memo = {}

def fib_memo(n):
    """
    Calculates the nth Fibonacci number using memoization (top-down DP).
    """
    # 1. Is the result already in our cache?
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 1:
        return n

    # 2. If not, compute it recursively
    result = fib_memo(n - 1) + fib_memo(n - 2)
    
    # 3. Store the result in the cache before returning
    memo[n] = result
    return result

# Example usage:
n = 10
print(f"The {n}th Fibonacci number is: {fib_memo(n)}")

# The cache will be populated after the call
print(f"Cache content: {memo}")
