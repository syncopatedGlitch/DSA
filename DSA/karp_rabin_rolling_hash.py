"""Karp-Rabin Rolling Hash Implementation

This module implements the Karp-Rabin rolling hash algorithm, a fundamental technique
used in string matching and pattern searching. The rolling hash allows efficient
computation of hash values for sliding windows of text.

Rolling Hash Concept:
The rolling hash enables O(1) computation of hash values for consecutive substrings
by using the previous hash value instead of recalculating from scratch. This is
achieved through polynomial hashing with a mathematical relationship between
consecutive windows.

Mathematical Foundation:
For a string S[i...j], the hash is computed as:
hash(S[i...j]) = (S[i] * base^(j-i) + S[i+1] * base^(j-i-1) + ... + S[j] * base^0) % prime

Rolling Property:
To move from hash(S[i...j]) to hash(S[i+1...j+1]):
1. Remove the leftmost character: subtract S[i] * base^(j-i)
2. Shift remaining characters: multiply by base
3. Add the new rightmost character: add S[j+1]
4. Apply modulo operation to prevent overflow

Key Features:
- O(1) hash computation for sliding windows
- Configurable base (default 256 for ASCII characters)
- Large prime modulus to minimize hash collisions
- Foundation for efficient string matching algorithms

Applications:
- Substring search (Karp-Rabin algorithm)
- Duplicate detection in sliding windows
- Pattern matching in streams
- Rolling checksum calculations

Time Complexity:
- Hash computation: O(1) per slide
- String search: O(n + m) average case
- Space Complexity: O(1)
"""

class KarpRabin:
    def __init__(self, base = 256, prime = 1000000007):
        '''
        Initialize class with:
        base: defaulted to 256 for all characters including special chars
        prime: A prime number to keep hash values within range
        '''
        self.base = base
        self.prime = prime

    def search_string(self, text, pattern):
        '''
        Search a pattern in a chunk of text provided
        Return -1 if no match found
        '''

        # initialize text, pattern and their lengths
        n, m = len(text), len(pattern)

        if m > n:
            return -1

        # calculate initial hash
        pattern_hash = 0
        text_hash = 0
        base_power = 1

        for i in range(m):
            pattern_hash = (pattern_hash * self.base + ord(pattern[i])) % self.prime
            text_hash = (text_hash * self.base + ord(text[i])) % self.prime
            # We need exactly m-1 multiplications to get base^(m-1)
            # Pattern length 3 → need base² → 2 multiplications
            # Pattern length 4 → need base³ → 3 multiplications
            if i < m - 1:
                base_power = (base_power * self.base) % self.prime

        # Check first window
        if pattern_hash == text_hash and text[:m] == pattern:
            return 0

        # If initial hash doesnt match, perform rolling Hash on sliding window
        for i in range(1, n - m + 1):
            # Remove first character of previous window
            text_hash = (text_hash - ord(text[i - 1]) * base_power) % self.prime
            # Add last character of current window
            text_hash = (text_hash * self.base + ord(text[i + m - 1])) % self.prime
            # handle negative hash cases
            text_hash = (text_hash + self.prime) % self.prime
            # check match
            if pattern_hash == text_hash and text[i: i + m] == pattern:
                return i

        return -1


if __name__ == "__main__":
    # Demonstrate basic implementation
    # print("=== Basic Karp-Rabin Implementation ===")
    # demonstrate_karp_rabin()

    # Demonstrate optimized version
    print("\n=== Optimized Implementation ===")
    kr_opt = KarpRabin()

    text = "The quick brown fox jumps over the lazy dog"
    patterns = ["The", "fox", "lazy", "cat"]

    for pattern in patterns:
        print(f"Searching string {pattern} ({len(pattern)}) in text: {text} ({len(text)})")
        index = kr_opt.search_string(text, pattern)
        if index != -1:
            print(f"Pattern '{pattern}' found at index {index}")
        else:
            print(f"Pattern '{pattern}' not found")
