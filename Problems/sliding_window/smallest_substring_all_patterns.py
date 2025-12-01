import math
'''
Smallest Substring Containing All Patterns
Given a string S and an array of patterns, find the smallest substring window [l, r] such that each pattern appears at least once within S[l..r]. Return the pair of indices or [-1, -1] if no such window exists.

Example

Input

S = xyzabcabczyx
patterns = ['abc', 'zyx']
Output

[6,11]
Explanation

- Identify occurrences of 'abc' at indices [3..5] and [6..8], and 'zyx' at [9..11]. 
- Combining the second 'abc' ([6..8]) with 'zyx' ([9..11]) yields the window [6,11] of length 6, which is shorter than the alternative [3,11], so the result is [6,11].
'''

'''
After finding all occurrences, you have something like:

     occurrences = [
         (3, 5, 0),   # pattern 'abc' at [3,5], pattern_id=0
         (6, 8, 0),   # pattern 'abc' at [6,8], pattern_id=0
         (9, 11, 1),  # pattern 'zyx' at [9,11], pattern_id=1
     ]
     # Sorted by start position

   Core Intuition: The "Pattern Coverage" Problem

   Think of it like this:

   You're organizing a meeting with multiple people. Each person (pattern) can arrive at
   different times (occurrences). You want to find the shortest time window where everyone
   has arrived at least once.

   The Sliding Window Mental Model

   Imagine a rubber band that stretches across the occurrences:

     Timeline of occurrences:
     [3,5]     [6,8]     [9,11]
      abc       abc       zyx

     Window: [-------------]
             left        right

   Phase 1: Expand Right - "Gather Everyone"

   Goal: Keep expanding right until all patterns are covered.

     Step 1: Add [3,5]
     Window: [[3,5]]
     Covered patterns: {0:'abc'} ❌ Missing pattern 1

     Step 2: Add [6,8]
     Window: [[3,5], [6,8]]
     Covered patterns: {0:'abc'} ❌ Still missing pattern 1

     Step 3: Add [9,11]
     Window: [[3,5], [6,8], [9,11]]
     Covered patterns: {0:'abc', 1:'zyx'} ✅ ALL COVERED!

   Phase 2: Contract Left - "Kick Out Redundants"

   Goal: Shrink from the left while maintaining coverage.

   Key Question: "Can I remove the leftmost occurrence and still have all patterns?"

     Current window: [[3,5], [6,8], [9,11]]
     Window span: [3, 11]

     Try removing [3,5]:
     Remaining: [[6,8], [9,11]]
     Covered: {0:'abc' (from [6,8]), 1:'zyx'} ✅ Still all covered!
     New span: [6, 11] ← BETTER! Save this!

     Try removing [6,8]:
     Remaining: [[9,11]]
     Covered: {1:'zyx'} ❌ Lost pattern 0!
     STOP! Can't shrink further.

   Phase 3: Continue Sliding

   After contracting, continue expanding right (if more occurrences exist), then contract
   again. Repeat until done.
'''


def findSmallestSubstringWindow(patterns, S):
    # find all individual occurence of each pattern first
    # store tuple containing (start, end, pattern_idx)
    if len(S) == 1 and len(patterns) == 1 and S == patterns[0]:
        return [0, 0]
    matches = []
    for idx, pattern in enumerate(patterns):
        length = len(pattern)
        start_indices = find_all_occurences(pattern, S)
        for start in start_indices:
            end = start + length - 1
            matches.append((start, end, pattern))
    # sort all occurence intervals by start index
    matches.sort(key=lambda x: x[0])
    # create a frequency map for all patterns so you know who is covered in the window
    # and who is left out.
    target_counts = dict(Counter(patterns))
    result = find_smallest_substring(matches, target_counts)
    return result


def find_smallest_substring(matches, target_counts):
    window_counts = {}
    required = len(target_counts)
    formed = 0
    left = 0
    min_length_window = math.inf
    result_window = [-1, -1]
    for right in range(len(matches)):
        match = matches[right]
        start, end, pattern = match
        # try to add one pattern at a time and update the formed count
        # and window_counts
        if pattern in target_counts:
            window_counts[pattern] = window_counts.get(pattern, 0) + 1
            if window_counts.get(pattern) == target_counts[pattern]:
                formed += 1
        # check if we have formed a valid window, and if yes,
        # shrink from the left until window becomes invalid
        while left <= right and required == formed:
            # squeeze the window from left removing one pattern at a time
            start_index = matches[left][0]
            end_index = matches[right][1]
            current_length = end_index - start_index + 1
            if current_length < min_length_window:
                min_length_window = current_length
                result_window[0], result_window[1] = start_index, end_index
            # store the leftmost pattern to check in the shrunk window
            leftmost_pattern = matches[left][2]
            left += 1
            # update state after moving left pointer
            if leftmost_pattern in target_counts:
                if window_counts[leftmost_pattern] == target_counts[leftmost_pattern]:
                    formed -= 1
                window_counts[leftmost_pattern] -= 1    
    return result_window


def find_all_occurences(pattern, s: str):
    i = 0
    start_indices = []
    while True:
        found_index = s.find(pattern, i)
        # find returns -1 if string isnt found
        if found_index == -1:
            break
        start_indices.append(found_index)
        i = found_index + 1
    return start_indices