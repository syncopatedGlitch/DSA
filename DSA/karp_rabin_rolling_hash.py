"""Karp-Rabin Rolling Hash Implementation

This module implements the Karp-Rabin rolling hash algorithm,
a fundamental technique used in string matching and pattern
searching. The rolling hash allows efficient
computation of hash values for sliding windows of text.

Rolling Hash Concept:
The rolling hash enables O(1) computation of hash values
for consecutive substrings by using the previous hash value
instead of recalculating from scratch. This is achieved through
polynomial hashing with a mathematical relationship between
consecutive windows.

Mathematical Foundation:
For a string S[i...j], the hash is computed as:
hash(S[i...j]) = (
    S[i] * base^(j-i) + S[i+1] * base^(j-i-1) + ... + S[j] * base^0
) % prime

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
    def __init__(self, base=256, prime=1000000007):
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
        # Let's trace the code with a concrete example:
        # * text = "abedabc" (n=7)
        # * pattern = "abc" (m=3)
        # initialize text, pattern and their lengths
        n, m = len(text), len(pattern)

        if m > n:
            return -1

        # calculate initial hash
        pattern_hash = 0
        text_hash = 0
        base_power = 1  # This will hold base^(m-1)
        # This loop calculates the hash for the pattern ("abc") and
        # the first window of the text ("abe").
        for i in range(m):
            pattern_hash = (
                pattern_hash * self.base + ord(pattern[i])
            ) % self.prime
            text_hash = (text_hash * self.base + ord(text[i])) % self.prime
            # We need exactly m-1 multiplications to get base^(m-1)
            # Pattern length 3 → need base² → 2 multiplications
            # Pattern length 4 → need base³ → 3 multiplications
            # We also pre-calculate base^(m-1), which is base² here.
            # This is the power of the most significant character,
            # needed for removal.
            if i < m - 1:
                # The entire rolling hash algorithm relies on a principle
                # of modular arithmetic:
                # (a * b) % p is the same as ((a % p) * (b % p)) % p
                # This means we can apply the modulo at each intermediate
                # step without changing the final result of the entire
                # calculation. Since the main hash calculations for
                # pattern_hash and text_hash are also done modulo prime,
                # it's essential that the base_power we use to subtract
                # the leading character is also calculated within
                # the same modulo system.
                # In short, we are performing all our arithmetic in a
                # finite mathematical field defined by mod prime.
                # Doing the % self.prime in the base_power calculation
                # ensures it stays within that field, preventing
                # overflow and keeping the "rolling" math correct.
                base_power = (base_power * self.base) % self.prime

        # Check first window
        if pattern_hash == text_hash and text[:m] == pattern:
            return 0

        # If initial hash doesnt match, perform rolling Hash on sliding window
        # Let's take a simple example:
        # * String: cat
        # * Base: 256 (chosen in your code because it covers the standard
        # ASCII character set)
        # * Prime: 1000000007 (a large prime number to prevent the hash value
        # from getting too big and to reduce the chance of collisions)

        # The hash for "cat" is calculated like this, similar to how we
        # understand numbers in base-10 (e.g., 123 = 1*10² + 2*10¹ + 3*10⁰):

        # hash("cat") = (
        # ord('c') * base² + ord('a') * base¹ + ord('t') * base⁰
        # ) % prime

        # * ord('c') = 99
        # * ord('a') = 97
        # * ord('t') = 116
        # * base = 256

        # hash("cat") = ( 99 * 256² + 97 * 256¹ + 116 * 256⁰ ) % 1000000007
        # hash("cat") = ( 99 * 65536 + 97 * 256 + 116 * 1 ) % 1000000007
        # hash("cat") = ( 6488064 + 24832 + 116 ) % 1000000007
        # hash("cat") = 6513012 % 1000000007 = 6513012

        # 4. The "Rolling" Mechanism: The O(1) Update

        # Now, let's see how to "roll" the hash. Imagine our text is abcat
        # and our pattern is cat (length 3).

        # 1. We first have the window abc. We calculate its hash: hash("abc").
        # 2. Now we want the hash for the next window, bca. Instead of
        # recalculating from scratch, we do this:

        # a.  Remove the leftmost character ('a'): The value of 'a' in
        #     hash("abc") was ord('a') * base². We need to subtract this.
        # b.  Shift the window to the left: Multiply the remaining hash
        #     by the base. This effectively promotes b to the base² position
        #     and c to the base¹ position.
        # c.  Add the new rightmost character ('t'): Add the value of the
        #     new character, ord('t').

        # The formula looks like this:
        # hash("bcat") = (
        #   (hash("abc") - ord('a') * base²) * base + ord('t')
        # ) % prime

        # This single operation of remove, shift, and add is incredibly fast,
        # taking the same amount of time regardless of how long the pattern is.
        # This is the O(1) update.
        # i will go from 1 to (7 - 3), so i = 1, 2, 3, 4
        for i in range(1, n - m + 1):
            # Remove first character of previous window
            text_hash = (
                text_hash - (ord(text[i - 1]) * base_power)
            ) % self.prime
            # Add last character of current window
            text_hash = (
                (text_hash * self.base) + ord(text[i + m - 1])
            ) % self.prime
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
        print(f"Searching string {pattern} ({len(pattern)})",
              f"in text: {text} ({len(text)})")
        index = kr_opt.search_string(text, pattern)
        if index != -1:
            print(f"Pattern '{pattern}' found at index {index}")
        else:
            print(f"Pattern '{pattern}' not found")
