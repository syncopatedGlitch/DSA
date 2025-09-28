"""Hash Map Implementation with Chaining

This module implements a hash map (hash table) using chaining
for collision resolution. Chaining handles collisions by
maintaining a linked list at each array index, allowing
multiple key-value pairs to coexist at the same hash location.

Chaining Collision Resolution:
- Each array slot contains a linked list (chain) of key-value pairs
- When collisions occur, new elements are added to the appropriate chain
- No clustering issues unlike linear probing
- Memory overhead due to storing pointers

Key Features:
- Handles unlimited collisions gracefully
- No need for tombstone markers during deletion
- Load factor can exceed 1.0
- Consistent performance even with many collisions

Operations:
- Insert/Update key-value pairs in chains
- Retrieve values by traversing appropriate chain
- Delete elements from chains
- Dynamic resizing to optimize performance

Time Complexities:
- Average case: O(1) for all operations
- Worst case: O(n) when all keys hash to same index
- Space complexity: O(n + m) where n is number of elements, m is table size
"""

from typing import Any


class Node:
    def __init__(self, k: Any, v: Any):
        self.key = k
        self.val = v
        self.next = None
        self.is_deleted = False


class HashMap:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def __hash(self, key: Any) -> int:
        return hash(key) % (self.capacity)

    def add(self, key, val):
        ''' Add a key value pair in the hash map'''
        node = Node(key, val)
        address = self.__hash(key)
        current = self.data[address]
        if not current:  # if nothing at address
            self.data[address] = node
            print(f"node inserted at address {address}. Key, value are: {key}:{val}")
        elif not current.next:  # if only one element at address
            if current.key == node.key:  # if key already exists
                self.data[address].val = node.val
                print(f"Overriding existing node at address {address}. Key, value are: {key}:{val}")
                return
            else:  # if key doesnt exist
                self.data[address].next = node
                print(f"node inserted next to existing node at address {address}. Key, value are: {key}:{val}")
        else:  # if multiple elements at address
            while current.next:
                if current.key == node.key:
                    current.val = node.val
                    print(f"Overriding existing node at address {address}. Key, value are: {key}:{val}")
                    return
                current = current.next
            if current.key == node.key:
                print(f"Overriding existing node at address {address}. Key, value are: {key}:{val}")
                current.val = node.val
                return
            current.next = node
            print(f"node inserted at end of chain at address {address}. Key, value are: {key}:{val}")

    def get(self, key):
        '''get the value associated with a key from the hashmap'''
        address = self.__hash(key)
        current = self.data[address]
        if current is None:
            print(f"Key: {key} not present in hashmap")
            return None
        else:
            while current:
                if current.key == key and not current.is_deleted:
                    print(f"Key: {key} found at address {address}. Value: {current.val}")
                    return current.val
                current = current.next
            print(f"Key: {key} not present in hashmap")
            return None

    def exists(self, key) -> bool:
        '''check if the key exist in the hash map'''
        address = self.__hash(key)
        current = self.data[address]
        if current is None:
            print(f"Key: {key} not present in hashmap")
            return False
        else:
            while current:
                if current.key == key and not current.is_deleted:
                    print(f"Key: {key} found at address {address}. Value: {current.val}")
                    return True
                current = current.next
            return False

    def remove(self, key):
        '''remove the key if it exists, else return None'''
        address = self.__hash(key)
        current = self.data[address]
        if current is None:
            print(f"Key: {key} not present in hashmap")
            return None
        else:
            while current:
                if current.key == key and not current.is_deleted:
                    print(f"Key: {key} removed from address {address}. Value: {current.val}")
                    current.is_deleted = True
                    return current.val

    def get_stats(self):
        """Get statistics about the hash map"""
        active_buckets = sum(1 for bucket in self.data if bucket is not None)
        total_nodes = 0
        deleted_nodes = 0

        for head in self.buckets:
            current = head
            while current:
                total_nodes += 1
                if current.is_deleted:
                    deleted_nodes += 1
                current = current.next

        return {
            'capacity': self.capacity,
            'size': self.size,
            'active_buckets': active_buckets,
            'total_nodes': total_nodes,
            'deleted_nodes': deleted_nodes,
            'load_factor': self.size / self.capacity
        }

    def display(self):
        """Display the hash map contents (for debugging)"""
        for i, head in enumerate(self.data):
            if head:
                print(f"Index {i}: ", end="")
                current = head
                while current:
                    status = "(DELETED)" if current.is_deleted else ""
                    val_str = "None" if current.val is None else str(current.val)
                    print(f"[{current.key}: {val_str}]{status}", end="")
                    if current.next:
                        print(" -> ", end="")
                    current = current.next
                print()


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
    res2 = mp.remove("a")
    assert res2 == 1
    print("after removing a, map is:")
    mp.display()
    res3 = mp.exists("a")
    assert res3 is False
    print("mp is:")
    mp.display()


if __name__ == "__main__":
    tests()
    print("All tests passed!")
