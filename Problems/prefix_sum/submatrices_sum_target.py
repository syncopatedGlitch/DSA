from typing import List
'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i][j] <= 1000
-10^8 <= target <= 10^8
'''

'''
The problem is hard in 2D. What if we could convert it into a series of 1D problems?

Let's think about a simpler, related 1D problem: "Given an array, find the number of
subarrays that sum to a target `k`." (This is LeetCode #561: "Subarray Sum Equals K").

How is that solved efficiently?
1. You iterate through the array, calculating the current_sum (prefix sum) as you go.
2. At each position, you have current_sum. You need to find if there was a previous
    prefix sum, prev_sum, such that current_sum - prev_sum = k.
3. Rearranging this gives prev_sum = current_sum - k.
4. You can use a hash map to store the frequencies of all the prefix sums you've seen
    so far. For each current_sum, you just look up how many times you've seen
    current_sum - k and add that to your total count. Then, you update the map with the
    current_sum. This gives a brilliant O(N) solution.
The main idea for the 2D problem is to apply this exact 1D technique over and over.
Step 3: Applying the 1D Solution to the 2D Matrix
How can we create 1D arrays from our 2D matrix?
Imagine "squashing" the matrix between a top_row and a bottom_row.
Let's fix two rows, say r1 (the top boundary) and r2 (the bottom boundary). We can now
create a temporary 1D array where each element arr[c] is the sum of all numbers in the
original matrix's column c from r1 to r2.

Matrix:
[ [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9] ]
Let's fix r1 = 0 and r2 = 1.
The "squashed" 1D array would be:
arr[0] = matrix[0][0] + matrix[1][0] = 1 + 4 = 5
arr[1] = matrix[0][1] + matrix[1][1] = 2 + 5 = 7
arr[2] = matrix[0][2] + matrix[1][2] = 3 + 6 = 9
So, our 1D array is [5, 7, 9].

Now, any submatrix that exists entirely between `r1` and `r2` corresponds to a subarray
in this new 1D array. The sum of the submatrix is equal to the sum of the corresponding
subarray.

So, for the fixed rows r1 and r2, we can just solve the 1D "Subarray Sum Equals K"
problem on this generated 1D array!

Putting it all together with the optimization:

The most efficient implementation of this idea is:

1. Initialize count = 0.
2. Let M be the number of rows and N be the number of columns.
3. Iterate r1 from 0 to M-1:
    * Create a 1D array col_sums of size N, filled with zeros. This array will store
        the sum of columns for the current slice.
    * Iterate r2 from r1 to M-1:
        * // Update the column sums for the new, thicker slice
        * For c from 0 to N-1:
            * col_sums[c] += matrix[r2][c]
        *
        * // Now col_sums represents the 1D "squashed" array for rows r1 to r2.
        * // Solve the 1D problem on col_sums with the target.
        * Initialize a hash map prefix_sum_freq = {0: 1}.
        * Initialize current_sum = 0.
        * For each s in col_sums:
            * current_sum += s
            * count += prefix_sum_freq.get(current_sum - target, 0)
            * prefix_sum_freq[current_sum] = prefix_sum_freq.get(current_sum, 0) + 1

4. Return count.

This approach has a time complexity of O(M² * N), which is a huge improvement and
passes the time limits. If N is smaller than M, you can iterate through columns first
for a complexity of O(N² * M).
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        count = 0
        for r1 in range(rows):
            col = [0] * columns
            for r2 in range(r1, rows):
                for c in range(columns):
                    col[c] += matrix[r2][c]
                prefix_map = {0: 1}
                current_sum = 0
                for num in col:
                    current_sum += num
                    prefix_sum = current_sum - target
                    count += prefix_map.get(prefix_sum, 0)
                    prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        return count


def tests():
    test_cases = [
        # Provided examples
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
        ([[1, -1], [-1, 1]], 0, 5),
        ([[904]], 0, 0),

        # Additional test cases
        # All elements are the target
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 9),

        # No solution possible
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 100, 0),

        # Complex case with positive and negative numbers
        ([[1, 2, -1], [-2, 3, 0], [2, -1, 1]], 2, 6),

        # Single row matrix
        ([[1, 2, 3, -3, 2, 1]], 3, 5),

        # Single column matrix
        ([[1], [2], [3], [-3], [2], [1]], 3, 5)
    ]

    sol = Solution()
    for i, (matrix, target, expected) in enumerate(test_cases):
        result = sol.numSubmatrixSumTarget(matrix, target)
        print(f"Test Case {i+1}: matrix={matrix}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected
        print("-" * 20)
        pass
    print("All tests passed.")


if __name__ == '__main__':
    tests()
