'''
There are n gas stations along a circular route, where the
amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank
at one of the gas stations.

Given two integer arrays gas and cost, return the starting
gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique.

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas.
Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough
to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough
gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas.
Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit
of gas but you only have 3.
Therefore, you can't travel around the circuit once no
matter where you start.
'''
'''
You can solve this with a single loop through the stations.
You'll need to keep track of three things:

   1. start_station: The index of your candidate starting
      station. Initialize to 0.
   2. total_tank: The sum of gas[i] - cost[i] for all stations.
      This tells you if a solution is possible at all.
      Initialize to 0.
   3. current_tank: The gas in your tank from the current
      start_station. If this ever drops below zero, it means
      your current start_station is invalid. Initialize to 0.

  Algorithm:

   1. Iterate through the gas stations from i = 0 to n-1.
   2. For each station i:
       * Update total_tank by adding gas[i] - cost[i].
       * Update current_tank by adding gas[i] - cost[i].
       * If current_tank drops below 0, it means you can't
         reach station i+1 from the current start_station.
           * Based on the "Greedy Leap" insight, set the new
             start_station to i + 1.
           * Reset current_tank to 0 to start fresh from
             this new station.
   3. After the loop, if total_tank is greater than or equal
      to 0, it means a solution exists, and the start_station
      you found is the one. Return start_station.
   4. If total_tank is negative, no solution is possible.
      Return -1.
'''


def gas_station_loop(gas: list, cost: list) -> int:
    total_gas = 0
    current_gas = 0
    start_station = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        if current_gas < 0:
            start_station = i + 1
            current_gas = 0
    if total_gas >= 0:
        return start_station
    return -1


def tests():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    res = gas_station_loop(gas, cost)
    print(f"1st test case result is {res}")
    assert res == 3
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    res = gas_station_loop(gas, cost)
    print(f"2nd test case result is {res}")
    assert res == -1


tests()
