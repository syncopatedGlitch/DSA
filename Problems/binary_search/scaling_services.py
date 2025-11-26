from typing import List
'''
A data pipeline consists of n services connected
in series where the output of each service i
serves as input for service [i+1]
each service has variable latency and the throughput
of i service is represented by throughput[i] in messages
per min. Each service can be scaled up indedenpendently.
Scaling [i] cost scalingcost[i] and after scaling upto
x times you can get throughput of throughput[i]* (1+x)
given thruwput and scalingcost array and a budget,
determine optimal scaling configuration

# Example usage
throughput = [4, 2, 7]
scaling_cost = [12, 10, 14]
budget = 32
Expected output = 6
'''
'''
 The Algorithm Intuition

1. Define a Search Range: We search for the answer
   (the maximum possible throughput) in a range. The
   lower bound is the current minimum throughput, and
   the upper bound can be a very large number (e.g.,
   the max possible throughput if you spent the whole
   budget on the cheapest service).

2. Binary Search:
    * Pick a target_throughput in the middle of your
      current search range.
    * Check Feasibility: For this target_throughput,
      calculate the total cost needed to bring every
      service that is below this target up to the target.
    * Adjust Range:
        * If the total_cost is within your budget, it
          means this target_throughput is possible. You
          should try for an even better (higher) throughput.
          So, you store this as a potential answer and move
          your search to the upper half (low = mid + 1).
        * If the total_cost is over budget, this
          target_throughput is too ambitious. You need
          to try for a lower one. So, you move your search
          to the lower half (high = mid - 1).

3. Result: You repeat this process until the search range
   collapses. The best possible answer you found along the
   way is the optimal throughput.

This approach is highly efficient because it narrows down
the vast range of possible answers very quickly, and the
"feasibility check" at each step is a simple, fast loop through
the n services
'''


def scale_services(
        throughput: List,
        scaling_cost: List,
        budget: int
) -> int:
    result = 0
    lower = min(throughput)
    upper = max(throughput) + (2 * budget)

    while lower <= upper:
        current_tp = (lower + upper) // 2
        cost = 0
        for i in range(len(throughput)):
            scaling_factor = (current_tp / throughput[i]) - 1
            cost += (scaling_cost[i] * scaling_factor)
        if cost > budget:
            upper = current_tp - 1
        elif cost < budget:
            result = max(result, current_tp)
            lower = current_tp + 1
    return result


def tests():
    # Example 1
    throughput = [4, 2, 7]
    scaling_cost = [12, 10, 14]
    budget = 32
    expected_output = 6

    result = scale_services(throughput, scaling_cost, budget)
    assert result == expected_output
    print("--- Test Case 1 Finished ---")


if __name__ == "__main__":
    tests()
