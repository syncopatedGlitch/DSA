"""Hash Map Implementation with Linear Probing

This module implements a hash map (hash table) using linear probing for collision resolution.
A hash map is a data structure that provides efficient key-value storage and retrieval
using a hash function to map keys to array indices.

Linear Probing Collision Resolution:
- When a collision occurs (two keys hash to the same index), linear probing searches
  for the next available slot by incrementally checking subsequent array positions
- Simple and cache-friendly approach
- Can suffer from clustering where consecutive occupied slots form clusters

Key Features:
- Dynamic resizing to maintain load factor
- Lazy deletion using tombstone markers
- Average O(1) time complexity for basic operations
- Handles collisions gracefully

Operations:
- Insert/Update key-value pairs
- Retrieve values by key
- Delete key-value pairs
- Resize when load factor exceeds threshold

Time Complexities (Average Case):
- Insert: O(1)
- Search: O(1)
- Delete: O(1)
- Worst case: O(n) when many collisions occur
"""

from typing import Any


class Node:
    def __init__(self, k: Any, v: Any):
        self.key = k
        self.val = v
        self.is_deleted = False


class HashMap:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0
        self.load_factor_threshold = 0.5

    def __hash(self, key: Any) -> int:
        return hash(key) % (self.capacity)

    def __resize(self):
        # Double capacity when load factor exceeds threshold
        print("################### RESIZING ###################")
        old_keys = []
        old_vals = []
        for node in self.data:
            if node is not None and not node.is_deleted:
                old_keys.append(node.key)
                old_vals.append(node.val)
        self.capacity *= 2
        self.size = 0
        self.data = [None] * self.capacity
        for i in range(len(old_keys)):
            node = Node(old_keys[i], old_vals[i])
            self.add(node.key, node.val)

    def add(self, key, val):
        ''' Add a key value pair in the hash map'''
        # ensuring there is enough capacity for an insert so you dont have
        # to check that condition later in the method
        if (self.size + 1) / self.capacity > self.load_factor_threshold:
            self.__resize()
        node = Node(key, val)
        address = self.__hash(key)
        probes = 0
        # linear probing
        while self.data[address] is not None and probes < (self.capacity):
            if self.data[address] and self.data[address].key == key:
                self.data[address].val = val
                print(f"Overriding existing node at address {address}. Key, value are: {key}:{val}")
                return
            address = (address + 1) % (self.capacity)
            probes += 1
        # Safety check - should never happen with proper load factor management
        if probes > self.capacity:
            raise Exception("Unexpected: table appears full despite load factor check")
        # while loop exits when an empty slot is found
        # so address would be pointing to that empty slot
        self.data[address] = node
        print(f"Added node at address {address}. Key, value are: {key}:{val}")
        self.size += 1

    def get(self, key):
        '''get the value associated with a key from the hashmap'''
        address = self.__hash(key)
        probes = 0
        while probes < self.capacity:
            current = self.data[address]
            if current is None:
                print(f"Key: {key} not present in hashmap")
                return None
            if current.key == key and not current.is_deleted:
                print(f"Key: {key} found at address {address}. Value: {current.val}")
                return current.val
            address = (address + 1) % self.capacity
            probes += 1
        # key not found after checking all slots
        print(f"Key: {key} not present in hashmap")
        return None

    def exists(self, key):
        '''Check if a key exists in the hashmap'''
        address = self.__hash(key)
        probes = 0
        while probes < self.capacity:
            current = self.data[address]
            if current is None:
                print(f"Key: {key} not present in hashmap")
                return False
            if current.key == key and not current.is_deleted:
                print(f"Key: {key} found at address {address}. Value: {current.val}")
                return True
            address = (address + 1) % self.capacity
            probes += 1
        # key not found after checking all slots
        print(f"Key: {key} not present in hashmap")
        return False

    def pop(self, key) -> Any:
        '''Remove a key from a dict and return its value'''
        address = self.__hash(key)
        probes = 0
        while probes < self.capacity:
            current = self.data[address]
            if current is None:
                print(f"Key: {key} not present in hashmap")
                return None
            if current.key == key and not current.is_deleted:
                self.data[address].is_deleted = True
                print(f"Key: {key} found at address {address}. Value: {current.val}")
                return current.val
            address = (address + 1) % self.capacity
            probes += 1
        print(f"Key: {key} not present in hashmap")
        return None

    def display(self):
        """Display the hash map contents (for debugging)"""
        for i, current in enumerate(self.data):
            if current:
                status = "(DELETED)" if current.is_deleted else ""
                val_str = "None" if current.val is None else str(current.val)
                print(f"Index {i}: [{current.key}: {val_str}]{status}")


def tests():
    mp = HashMap(10)
    mp.add("a", 1)
    print("mp is:")
    mp.display()
    mp.add("b", 2)
    print("mp is:")
    mp.display()
    mp.add("c", 3)
    print("mp is:")
    mp.display()
    mp.add("d", 4)
    print("mp is:")
    mp.display()
    mp.add("e", 5)
    print("mp is:")
    mp.display()
    mp.add("f", 6)
    print("map is: ")
    mp.display()
    mp.add("d", 5)
    print("mp is:")
    mp.display()
    res = mp.get("a")
    assert res == 1
    print("mp is:")
    mp.display()
    res1 = mp.exists("b")
    assert res1 is True
    print("mp is:")
    mp.display()
    res1 = mp.exists("h")
    assert res1 is False
    print("mp is:")
    mp.display()
    res2 = mp.pop("a")
    assert res2 == 1
    print("after removing a, map is:")
    mp.display()
    res3 = mp.exists("a")
    assert res3 is False
    print("mp is:")
    res4 = mp.pop("b")
    assert res4 == 2
    print("after removing b, map is:")
    mp.display()
    res3 = mp.exists("b")
    assert res3 is False
    print("mp is:")
    mp.display()


if __name__ == "__main__":
    tests()
    print("All tests passed!")
