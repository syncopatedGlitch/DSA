'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

bool insert(int val) Inserts an item val into the set
if not present. Returns true if the item was not
present, false otherwise.

bool remove(int val) Removes an item val from the
set if present. Returns true if the item was present,
false otherwise.

int getRandom() Returns a random element from the
current set of elements (it's guaranteed that at
least one element exists when this method is called).
Each element must have the same probability of being
returned.
You must implement the functions of the class such
that each function works in average O(1) time complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert",
"getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set.
                    Returns true as 1 was inserted
                    successfully.
randomizedSet.remove(2); // Returns false as 2 does
                    not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set,
                    returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should
                    return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set,
                    returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set,
                    so return false.
randomizedSet.getRandom(); // Since 2 is the only number
                    in the set, getRandom() will always
                    return 2.
'''

import random


class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.vals.append(val)
        self.map[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        if len(self.vals) == 1:
            # Handle case where it's the only element
            self.vals = []
            self.map = {}
            return True

        index = self.map[val]
        last = len(self.vals) - 1
        last_val = self.vals[last]

        # Swap the element to remove with the last element
        self.vals[index], self.vals[last] = self.vals[last], self.vals[index]
        self.map.pop(self.vals[-1])

        # Pop the value to be removed from the map and the list
        self.map.pop(val)
        self.vals.pop()
        self.map[last_val] = index

        # Update the index of the element that was moved, but only if it wasn't the one we removed
        if last_val != val:
            self.map[last_val] = index

        return True

    def getRandom(self) -> int:
        if not self.vals:
            return False
            return -1 # Or raise an error, as per problem constraints
        rand = random.randint(0, len(self.vals) - 1)
        return self.vals[rand]


def tests():
    rs = RandomizedSet()
    assert rs.insert(1) is True
    assert rs.remove(2) is False
    assert rs.insert(2) is True
    random_val = rs.getRandom()
    assert random_val in [1, 2]
    assert rs.remove(1) is True
    assert rs.insert(2) is False
    assert rs.getRandom() == 2
    print("All tests passed!")


c = RandomizedSet()
c.insert(1)
c.remove(2)
c.remove(1)
c.insert(1)
c.insert(2)
c.insert(3)
print(f"random int is {c.getRandom()}")
tests()



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()