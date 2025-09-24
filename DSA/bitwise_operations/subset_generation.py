def generate_subsets(nums):
    """
    Generates all possible subsets (the power set) from a list of distinct integers
    using a bitmasking approach.

    The core idea is to map each integer from 0 to 2^n - 1 to a unique subset.
    For each integer (the 'mask'), its binary representation determines which
    elements from the input list to include in the subset.

    If the j-th bit is set in the mask, the j-th element of `nums` is included.

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of lists, where each inner list is a unique subset of `nums`.
    """
    n = len(nums)
    # There will be 2^n subsets. We can calculate this as 1 << n.
    num_subsets = 1 << n

    all_subsets = []

    # Loop through all possible masks, from 0 to 2^n - 1.
    for i in range(num_subsets):
        # i is our bitmask for the current subset.
        current_subset = []

        # Check each bit of the mask to decide which elements to include.
        for j in range(n):
            # j represents the j-th bit position (and the j-th element index).
            # Check if the j-th bit is set in i.
            # (i >> j) & 1 is a standard way to get the j-th bit.
            if (i >> j) & 1:
                current_subset.append(nums[j])

        all_subsets.append(current_subset)

    return all_subsets


# --- Example ---
if __name__ == "__main__":
    input_nums = [1, 2, 3]
    power_set = generate_subsets(input_nums)

    print(f"The input list is: {input_nums}")
    print(f"The generated power set is:")
    # Sorting for consistent output display
    power_set.sort(key=len)
    print(power_set)

    # Expected: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    # (order may vary before sorting)
