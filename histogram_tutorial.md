# LARGEST RECTANGLE IN HISTOGRAM - COMPLETE TUTORIAL

A comprehensive guide to understanding the classic histogram problem from first principles.

---

## TABLE OF CONTENTS
1. [Understanding the Problem](#part-1-understanding-the-problem)
2. [The Core Insight](#part-2-the-core-insight)
3. [Brute Force Solution O(n²)](#part-3-brute-force-solution)
4. [The Breakthrough - Monotonic Stack](#part-4-the-breakthrough)
5. [How Stack Maintains Boundaries](#part-5-stack-boundaries)
6. [Width Calculation Explained](#part-6-width-calculation)
7. [Handling Remaining Elements](#part-7-remaining-elements)
8. [Complete Implementation](#part-8-complete-implementation)
9. [Key Takeaways](#part-9-key-takeaways)

---

## PART 1: Understanding the Problem

Imagine you're looking at a histogram (bar chart) where each bar has a certain height. Your job is to find the **LARGEST RECTANGLE** that can fit entirely under the histogram.

### Example

```
heights = [2, 1, 5, 6, 2, 3]
```

### Visual Representation

```
Height
  6 |           ▓▓▓
  5 |           ▓▓▓ ▓▓▓
  4 |           ▓▓▓ ▓▓▓
  3 |           ▓▓▓ ▓▓▓           ▓▓▓
  2 |     ▓▓▓   ▓▓▓ ▓▓▓   ▓▓▓     ▓▓▓
  1 |     ▓▓▓   ▓▓▓ ▓▓▓   ▓▓▓     ▓▓▓
  0 +---------------------------------------
      idx: 0   1   2   3   4   5
```

### What is a Valid Rectangle?

- It must be **UNDER** the histogram (can't exceed any bar's height)
- It must be **CONTINUOUS** (no gaps in width)
- It has a **FIXED HEIGHT** throughout its width

### Example Rectangles

**Rectangle 1:** Height=1, Width=6 (spans all bars)
```
Area = 1 × 6 = 6
[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]
```

**Rectangle 2:** Height=2, Width=1 (just index 0)
```
Area = 2 × 1 = 2
[■■■]
```

**Rectangle 3:** Height=5, Width=2 (indices 2 and 3)
```
Area = 5 × 2 = 10  ← MAXIMUM!
      [■■■■■■■]
```

**Why can't Rectangle 3 extend left to index 1?**
- Because height at index 1 is only 1, which is less than 5!

**Why can't Rectangle 3 extend right to index 4?**
- Because height at index 4 is only 2, which is less than 5!

---

## PART 2: The Core Insight

For **EVERY** bar at index `i` with height `h[i]`, ask this question:

> "If I use this bar's height as my rectangle's height, how WIDE can I make the rectangle?"

To answer this, you need to find:
1. How far **LEFT** can I extend while keeping all bars >= h[i]?
2. How far **RIGHT** can I extend while keeping all bars >= h[i]?

**The area for this bar = h[i] × width**

### Complete Trace Through Example

```
heights = [2, 1, 5, 6, 2, 3]
Index:     0  1  2  3  4  5
```

**Index 0, height = 2:**
- Left extension: Can't go left (we're at the start)
- Right extension: Can we include index 1? No! height[1] = 1 < 2
- Width = 1 (just itself)
- Area = 2 × 1 = **2**

**Index 1, height = 1:**
- Left extension: Can we include index 0? Yes! height[0] = 2 >= 1
  - Keep going left? No more elements
- Right extension: Can we include index 2? Yes! height[2] = 5 >= 1
  - Can we include index 3? Yes! height[3] = 6 >= 1
  - Can we include index 4? Yes! height[4] = 2 >= 1
  - Can we include index 5? Yes! height[5] = 3 >= 1
- Width = 6 (entire array!)
- Area = 1 × 6 = **6**

**Index 2, height = 5:**
- Left extension: Can we include index 1? No! height[1] = 1 < 5
- Right extension: Can we include index 3? Yes! height[3] = 6 >= 5
  - Can we include index 4? No! height[4] = 2 < 5
- Width = 2 (indices 2 and 3)
- Area = 5 × 2 = **10** ← **MAXIMUM!**

**Index 3, height = 6:**
- Left extension: Can we include index 2? No! height[2] = 5 < 6
- Right extension: Can we include index 4? No! height[4] = 2 < 6
- Width = 1 (just itself)
- Area = 6 × 1 = **6**

**Index 4, height = 2:**
- Left extension: Can we include index 3? Yes! height[3] = 6 >= 2
  - Can we include index 2? Yes! height[2] = 5 >= 2
  - Can we include index 1? No! height[1] = 1 < 2
- Right extension: Can we include index 5? Yes! height[5] = 3 >= 2
- Width = 4 (indices 2, 3, 4, 5)
- Area = 2 × 4 = **8**

**Index 5, height = 3:**
- Left extension: Can we include index 4? No! height[4] = 2 < 3
- Right extension: Can't go right (we're at the end)
- Width = 1 (just itself)
- Area = 3 × 1 = **3**

**Maximum of all areas = max(2, 6, 10, 6, 8, 3) = 10**

---

## PART 3: Brute Force Solution

Now that we understand the problem, let's code the straightforward solution.

### Algorithm

```
For each bar i:
    1. Set left = i, right = i
    2. Expand left while heights[left-1] >= heights[i]
    3. Expand right while heights[right+1] >= heights[i]
    4. Calculate area = heights[i] × (right - left + 1)
    5. Track maximum area
```

### Implementation

```python
def largestRectangleAreaBruteForce(heights):
    n = len(heights)
    max_area = 0
    
    for i in range(n):
        current_height = heights[i]
        
        # Find left boundary
        left = i
        while left > 0 and heights[left - 1] >= current_height:
            left -= 1
        
        # Find right boundary
        right = i
        while right < n - 1 and heights[right + 1] >= current_height:
            right += 1
        
        # Calculate area
        width = right - left + 1
        area = current_height * width
        max_area = max(max_area, area)
    
    return max_area
```

### Complexity Analysis

**Time Complexity:** O(n²)
- Outer loop: O(n) - iterate through each bar
- Inner loops (left and right expansion): O(n) in worst case
- Total: O(n²)

**Space Complexity:** O(1)

**When is this O(n²)?**
Consider `heights = [1, 2, 3, 4, 5]` (increasing)
- For the last bar (height=5), we expand left through all previous bars
- For each bar, we potentially scan all other bars

**Can we do better? YES!** That's where the stack comes in...

---

## PART 4: The Breakthrough - Monotonic Stack Intuition

The brute force works, but it's slow because we repeatedly scan left and right.

### Key Observation

When we're at bar `i` and we see a **SHORTER** bar than what we've seen before, this tells us something VERY important:

> **"All the taller bars we saw earlier CANNOT extend past this point!"**

This is a **BOUNDARY DISCOVERY** moment!

### Example Walkthrough

```
heights = [2, 1, 5, 6, 2, 3]
```

**Step 1:** We see bar 0 (height 2)
```
Stack: [0]
Thinking: "Bar 0 could potentially extend right..."
```

**Step 2:** We see bar 1 (height 1) - **SHORTER** than bar 0!
```
This means: Bar 0 CANNOT extend to index 1!
We now know bar 0's right boundary is index 0.
We can calculate bar 0's area right now!

Pop bar 0, calculate its area = 2 × 1 = 2
Push bar 1
Stack: [1]
```

**Step 3:** We see bar 2 (height 5) - TALLER than bar 1
```
Stack: [1, 2]
Thinking: "Bar 2 could extend right... we don't know yet"
```

**Step 4:** We see bar 3 (height 6) - TALLER than bar 2
```
Stack: [1, 2, 3]
Thinking: "Bar 3 could extend right... we don't know yet"
```

**Step 5:** We see bar 4 (height 2) - **SHORTER** than bar 3!
```
This is crucial! Both bar 3 (height 6) and bar 2 (height 5)
are taller than bar 4 (height 2).

This means BOTH bar 3 and bar 2 cannot extend to index 4!

Pop bar 3 (height 6):
  - Right boundary: index 3 (can't reach index 4)
  - Left boundary: determined by what's below it in stack (bar 2)
  - Width calculation: from index 3 to index 3 = 1
  - Area = 6 × 1 = 6

Now check if we should pop bar 2:
Bar 4 (height 2) < Bar 2 (height 5), so yes!

Pop bar 2 (height 5):
  - Right boundary: index 3 (can't reach index 4)
  - Left boundary: determined by what's below it in stack (bar 1)
  - Width: from index 2 to index 3 = 2
  - Area = 5 × 2 = 10

Now bar 4 (height 2) is not shorter than bar 1 (height 1),
so we stop popping.

Stack: [1, 4]
```

### The Magic

We discovered that bar 2 can extend from index 2 to 3 **WITHOUT** scanning left or right explicitly! The stack **REMEMBERED** the left boundary for us!

---

## PART 5: How the Stack Maintains Left Boundaries

The stack stores indices in **INCREASING** order of heights.

### When We Pop an Element

When we pop an element at index `top_idx`:
- **Right boundary:** current index `i` (because `heights[i] < heights[top_idx]`)
- **Left boundary:** the element below it in the stack!

**Why?** Because the element below it in the stack is the **FIRST** element to the left that is **SHORTER** than `heights[top_idx]`.

**If the stack becomes empty after popping:**
- It means ALL elements to the left were >= `heights[top_idx]`
- So the left boundary is index 0

### Visual Example

```
Stack state: [1, 2, 3] means indices 1, 2, 3
heights:     [?, 1, 5, 6, ...]
```

The stack being in increasing order tells us:
- Index 2 (height 5): The first smaller element to its left is at index 1
- Index 3 (height 6): The first smaller element to its left is at index 2

When we pop index 3:
- We look at what's below: index 2
- This tells us the left boundary for index 3's rectangle!

---

## PART 6: Understanding Width Calculation

This is where students often get confused. Let me explain carefully.

### When We Pop Index `h_idx` at Position `i`:

**Case 1: Stack is NOT empty after popping**
```
Stack looks like: [..., left_idx]

The rectangle spans from (left_idx + 1) to (i - 1)
Width = (i - 1) - (left_idx + 1) + 1
      = i - left_idx - 1

Example: left_idx = 1, i = 4
Rectangle spans indices 2, 3 (from left_idx+1 to i-1)
Width = 4 - 1 - 1 = 2 ✓
```

**Case 2: Stack IS empty after popping**
```
This means the popped bar's height was smaller than ALL bars to the left.
The rectangle spans from 0 to (i - 1)
Width = i

Example: i = 4, stack empty
Rectangle spans indices 0, 1, 2, 3
Width = 4 ✓
```

### Why the "-1"?

The element at `stack[-1]` is a **SMALLER** bar that acts as a boundary. It's **NOT** part of our rectangle! That's why we do `i - stack[-1] - 1` instead of `i - stack[-1]`.

---

## PART 7: Handling Remaining Elements in Stack

After we've processed all bars, some bars might still be in the stack.

### What Does This Mean?

- These bars could extend all the way to the **END** of the array!
- We never found a shorter bar to their right.

### How to Handle Them

Pop them one by one:
- **Right boundary:** `len(heights) - 1` (the last index)
- **Left boundary:** element below in stack (or 0 if stack becomes empty)
- **Width calculation:** same as before, but use `len(heights)` instead of `i`

---

## PART 8: Complete Implementation

### Clean Code with Comments

```python
def largestRectangleArea(heights):
    """
    Find the largest rectangle area in a histogram.
    
    Algorithm: Monotonic Stack (Increasing)
    - Maintain indices of bars in increasing height order
    - When a shorter bar is found, calculate areas for taller bars
    - The stack implicitly tracks left boundaries
    
    Time: O(n) - each element pushed/popped once
    Space: O(n) - stack storage
    """
    if not heights:
        return 0
    
    stack = []  # Store indices (not heights!)
    max_area = 0
    
    for i, h in enumerate(heights):
        # Pop all bars taller than current
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            
            # Calculate width
            # If stack empty: extends from 0 to i-1
            # Else: extends from (stack[-1] + 1) to (i - 1)
            width = i if not stack else i - stack[-1] - 1
            
            max_area = max(max_area, height * width)
        
        stack.append(i) 
    
    # Process remaining bars (they extend to the end)
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area
```

### Test Cases

```python
test_cases = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([1, 1], 2),
    ([2, 1, 2], 3),
    ([5, 5, 1, 5, 5], 10),
    ([1], 1),
    ([1, 2, 3, 4, 5], 9),  # Increasing
    ([5, 4, 3, 2, 1], 9),  # Decreasing
]

for heights, expected in test_cases:
    result = largestRectangleArea(heights)
    assert result == expected, f"Failed for {heights}"
```

---

## PART 9: Key Takeaways

### 1. Problem Pattern
**"Largest/smallest in a range with constraints"** → Often solved with monotonic stack

### 2. Monotonic Stack
Maintains elements in sorted order (increasing or decreasing)
- **Increasing stack:** helps find "next smaller element"
- **Decreasing stack:** helps find "next larger element"

### 3. This Problem Uses INCREASING Stack
When we pop (found a smaller element), we know:
- **Right boundary:** current position
- **Left boundary:** element below in stack

### 4. Why O(n)?
Each element enters and leaves stack **at most once**
- Total operations = 2n = O(n)
- This is called **AMORTIZED ANALYSIS**

### 5. Tricky Part: Width Calculation
```python
width = i if not stack else i - stack[-1] - 1
```
The `-1` accounts for the fact that `stack[-1]` is the SMALLER element, not part of our rectangle!

### 6. Real-World Analogy
Imagine standing in a valley between mountains. You can see:
- Left until you hit a taller mountain
- Right until you hit a taller mountain

The stack remembers the mountains (smaller bars) that block your view!

---

## Common Mistakes to Avoid

❌ Using `heights[stack[-1]]` instead of `stack[-1]` for indices

❌ Forgetting to handle remaining elements in stack after the loop

❌ Wrong width calculation (forgetting the `-1`)

❌ Using `>=` instead of `>` in the while condition
   - We want strictly increasing, so equal heights should NOT be popped

❌ Trying to modify the input array by adding dummy elements
   - Not necessary and can cause issues

---

## Practice Problems

Once you master this problem, try these variations:

1. **Maximal Rectangle** (LeetCode 85)
   - 2D version using multiple histograms

2. **Trapping Rain Water** (LeetCode 42)
   - Similar stack-based approach

3. **Sum of Subarray Minimums** (LeetCode 907)
   - Uses monotonic stack to find contribution of each element

4. **Max Area Under Histogram After Removing One Bar**
   - The variant problem we'll tackle next!

---

## Summary

The key insight is that a **monotonic increasing stack** allows us to efficiently:
1. Find when a bar's right boundary is determined (when we see a shorter bar)
2. Remember left boundaries implicitly (the element below in stack)
3. Calculate areas in O(1) time when popping

This reduces the problem from O(n²) brute force to O(n) optimal solution!

**Master this pattern—it appears in many interview questions! 🚀**
