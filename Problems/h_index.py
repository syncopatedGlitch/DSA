'''
Given an array of integers citations where citations[i] is
the number of citations a researcher received for their ith
paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that
the given researcher has published at least h papers that
have each been cited at least h times.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers
in total and each of them had received 3, 0, 6, 1, 5
citations respectively.
Since the researcher has 3 papers with at least 3 citations
each and the remaining two with no more than 3 citations
each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1
'''
'''
Solution 1: The Sorting Approach (O(n log n))

This is the most intuitive "clever" solution.

1. Sort the citations array in descending order.
    * [3, 0, 6, 1, 5] becomes [6, 5, 3, 1, 0]

2. Iterate through the sorted array. The key insight is
   that after sorting, the paper's index `i` (plus one)
   can represent the count of papers, and the value
   `citations[i]` represents the minimum number of
   citations for that group of papers.

Let's trace [6, 5, 3, 1, 0]:
* i=0: We have 1 paper ([6]) with at least 6 citations.
* i=1: We have 2 papers ([6, 5]) with at least 5 citations.
* i=2: We have 3 papers ([6, 5, 3]) with at least 3 citations.
* i=3: We have 4 papers ([6, 5, 3, 1]) with at least 1 citation.

The definition of h-index is h papers with at least h
citations. Notice at i=2, we have 3 papers with at least 3
citations. This matches! The number of papers (i+1) is equal
to the citations (citations[i]). This is our h.

The Algorithm:
1. Sort citations descending.
2. Loop through the array with index i.
3. Find the first point where the number of papers
   (i + 1) is greater than the number of citations (citations[i]).
4. The h-index is the index i right before that break.

For [6, 5, 3, 1, 0]:
* i=0: 1 <= 6 (True)
* i=1: 2 <= 5 (True)
* i=2: 3 <= 3 (True)
* i=3: 4 <= 1 (False!) -> The loop breaks. The last successful
count was 3. So, h=3.

Solution 2: The "Even More Clever" Counting Approach (O(n))

If you want to avoid the O(n log n) cost of sorting, you can
use a counting method that is O(n).

1. Create a "bucket" array. Make an array (let's call it counts)
   of size n+1, where n is the number of papers. counts[i] will
   store how many papers have exactly i citations.
    * Any paper with more than n citations is treated as having
      n citations, because you can't have an h-index greater
      than the number of papers you've written.

2. Populate the buckets. Go through the citations list. For each
   citation_count, increment the appropriate bucket.
    * For [3, 0, 6, 1, 5] (n=5), the counts array
      becomes [1, 1, 0, 1, 0, 2].
    * counts[0] = 1 (one paper with 0 citations)
    * counts[1] = 1 (one paper with 1 citation)
    * counts[3] = 1 (one paper with 3 citations)
    * counts[5] = 2 (two papers with 5 or more citations)

3. Find h from the buckets. Iterate backwards from the end of
   the counts array, keeping a running total of papers.
    * Start a total = 0.
    * At i=5: total += counts[5] = 2. Is total >= 5? No (2 < 5).
    * At i=4: total += counts[4] = 2. Is total >= 4? No (2 < 4).
    * At i=3: total += counts[3] = 3. Is total >= 3? Yes.

The first time this condition is true, that i is your h-index.
So, h=3. This works because by iterating backwards, you are
guaranteed to find the maximum value of h that
satisfies the condition.
'''


def h_index(citations: list) -> int:
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            break
    return i


def tests():
    citations = [3, 0, 6, 1, 5]
    res = h_index(citations)
    print(f"1st test case h_index is {res}")
    assert res == 3
    citations = [1, 3, 1]
    res = h_index(citations)
    print(f"2nd test case h_index is {res}")
    assert res == 1


tests()
