"""Karp-Rabin String Matching Algorithm Implementation

This module implements the Karp-Rabin algorithm for efficient substring matching using
polynomial rolling hash. The algorithm achieves O(n+m) average time complexity by:

1. Computing hash values for the pattern and text windows
2. Using rolling hash to efficiently slide the window across the text
3. Verifying actual string matches only when hash values match (to handle collisions)

Key features:
- Rolling hash with polynomial base and prime modulus to minimize collisions
- Optimized version with larger prime (10^9+7) for better hash distribution
- Single match finder for first occurrence detection
"""

# class KarpRabin:
#     def __init__(self, base=256, prime=101):
#         """
#         Initialize Karp-Rabin algorithm

#         Args:
#             base: Base for polynomial rolling hash (typically 256 for ASCII)
#             prime: Prime number for modular arithmetic to avoid overflow
#         """
#         self.base = base
#         self.prime = prime

#     def search(self, text, pattern):
#         """
#         Search for pattern in text using Karp-Rabin algorithm

#         Args:
#             text: String to search in
#             pattern: String to search for

#         Returns:
#             List of starting indices where pattern is found
#         """
#         n = len(text)
#         m = len(pattern)

#         if m > n:
#             return []

#         matches = []

#         # Calculate hash of pattern and first window of text
#         pattern_hash = self._calculate_hash(pattern, m)
#         text_hash = self._calculate_hash(text, m)

#         # Precompute base^(m-1) % prime for rolling hash
#         h = 1
#         for i in range(m - 1):
#             h = (h * self.base) % self.prime

#         # Check first window
#         if pattern_hash == text_hash and self._verify_match(text, pattern, 0):
#             matches.append(0)

#         # Roll the hash over the text
#         for i in range(n - m):
#             # Remove leading character and add trailing character
#             text_hash = (self.base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % self.prime

#             # Handle negative hash values
#             if text_hash < 0:
#                 text_hash += self.prime

#             # Check if hash matches and verify actual string match
#             if pattern_hash == text_hash and self._verify_match(text, pattern, i + 1):
#                 matches.append(i + 1)

#         return matches

#     def _calculate_hash(self, string, length):
#         """Calculate polynomial rolling hash for given string"""
#         hash_value = 0
#         for i in range(length):
#             hash_value = (hash_value * self.base + ord(string[i])) % self.prime
#         return hash_value

#     def _verify_match(self, text, pattern, start_index):
#         """Verify actual string match to handle hash collisions"""
#         for i in range(len(pattern)):
#             if text[start_index + i] != pattern[i]:
#                 return False
#         return True


# # Example usage and demonstration
# def demonstrate_karp_rabin():
#     kr = KarpRabin()

#     # Test cases
#     test_cases = [
#         ("ABABDABACDABABCABCABCABCABC", "ABABCAB"),
#         ("GEEKS FOR GEEKS", "GEEK"),
#         ("AABAACAADAABAABA", "AABA"),
#         ("Hello World", "World"),
#         ("abcdefghijk", "def")
#     ]

#     for text, pattern in test_cases:
#         matches = kr.search(text, pattern)
#         print(f"Text: '{text}'")
#         print(f"Pattern: '{pattern}'")
#         print(f"Matches found at indices: {matches}")
#         print("-" * 50)


# Optimized version with better hash function
class OptimizedKarpRabin:
    def __init__(self, base=256, prime=1000000007):
        """
        Optimized version with larger prime to reduce collisions
        """
        self.base = base
        self.prime = prime

    def search_single(self, text, pattern):
        """
        Find first occurrence of pattern in text
        Returns index of first match or -1 if not found
        """
        n, m = len(text), len(pattern)
        # if pattern is longer than text, no match is possible
        if m > n:
            return -1

        # Calculate hashes
        pattern_hash = 0
        text_hash = 0
        base_power = 1

        # Calculate initial hashes and base power
        for i in range(m):
            pattern_hash = (pattern_hash * self.base + ord(pattern[i])) % self.prime
            text_hash = (text_hash * self.base + ord(text[i])) % self.prime
            # We need exactly m-1 multiplications to get base^(m-1)
            # Pattern length 3 → need base² → 2 multiplications
            # Pattern length 4 → need base³ → 3 multiplications
            if i < m - 1:
                base_power = (base_power * self.base) % self.prime
                # this base_power is the power for leftmost char in the selected text window

        # Check first window
        if pattern_hash == text_hash and text[:m] == pattern:
            return 0

        # Rolling hash
        for i in range(1, n - m + 1):
            # Remove first character of previous window
            # Multiply leftmost char with the base power calculated in for loop above
            text_hash = (text_hash - ord(text[i - 1]) * base_power) % self.prime
            # Add last character of current window
            text_hash = (text_hash * self.base + ord(text[i + m - 1])) % self.prime

            # Handle negative values
            text_hash = (text_hash + self.prime) % self.prime

            # Check match
            if pattern_hash == text_hash and text[i:i + m] == pattern:
                return i

        return -1


if __name__ == "__main__":
    # Demonstrate basic implementation
    # print("=== Basic Karp-Rabin Implementation ===")
    # demonstrate_karp_rabin()

    # Demonstrate optimized version
    print("\n=== Optimized Implementation ===")
    kr_opt = OptimizedKarpRabin()

    text = "The quick brown fox jumps over the lazy dog"
    patterns = ["The", "fox", "lazy", "cat"]

    for pattern in patterns:
        index = kr_opt.search_single(text, pattern)
        if index != -1:
            print(f"Pattern '{pattern}' found at index {index}")
        else:
            print(f"Pattern '{pattern}' not found")
