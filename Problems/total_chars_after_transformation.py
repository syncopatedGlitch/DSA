'''
You are given a string s and an integer t, representing
the number of transformations to perform. In one
transformation, every character in s is replaced according
to the following rules:

If the character is 'z', replace it with the string "ab".
Otherwise, replace it with the next character in the
alphabet. For example, 'a' is replaced with 'b', 'b' is
replaced with 'c', and so on.
Return the length of the resulting string after exactly
t transformations.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: s = "abcyy", t = 2
Output: 7

Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'b' becomes 'c'
'c' becomes 'd'
'y' becomes 'z'
'y' becomes 'z'
String after the first transformation: "bcdzz"
Second Transformation (t = 2):
'b' becomes 'c'
'c' becomes 'd'
'd' becomes 'e'
'z' becomes "ab"
'z' becomes "ab"
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab",
which has 7 characters.

Example 2:

Input: s = "azbk", t = 1
Output: 5

Explanation:
First Transformation (t = 1):
'a' becomes 'b'
'z' becomes "ab"
'b' becomes 'c'
'k' becomes 'l'
String after the first transformation: "babcl"
Final Length of the string: The string is "babcl",
which has 5 characters.
'''


def length_after_transformations(s: str, t: int) -> int:
    '''
    We define f(i,c) as the number of occurrences of the character
    c in the string after i transformations. For sake of clarity
    and ease of notation, we let c = [0,26), which corresponds to
    the 26 characters from a to z in sequence.

    Initially, each f(0,c) represents the number of occurrences of
    c in the given string s. As we iterate from f(i-1,⋯) to f(i,⋯):

    If c=0, corresponding to a, it can be converted from z, therefore:
    f(i,0)=f(i-1,25)
    If c=1, corresponding to b, it can be converted from z or a,
    therefore: f(i,1)=f(i-1,25)+f(i-1,0)
    If c≥2, it can come from the last character conversion, therefore:
    f(i,c)=f(i-1,c-1)
    So we obtain the recursive formula, which can be calculated from
    f(1,⋯) all the way to f(t,⋯). The sum of all f(t,c) is
    the final answer.

    Optimize
    Notice that in this recurrence formula, the calculation of
    f(i,⋯) only depends on the value of f(i-1,⋯), therefore we
    can use two one-dimensional arrays instead of the entire
    two-dimensional array f for recursion, as can be seen in
    the arrays cnt and nxt in the following code.
    '''
    MOD = 10**9 + 7
    initial_z_contrib = [0] * (t + 1)
    initial_z_count_at_step_0 = 0

    for char in s:
        if char == 'z':
            initial_z_count_at_step_0 += 1
        else:
            steps_to_z = ord("z") - ord(char)
            if steps_to_z <= t:
                initial_z_contrib[steps_to_z] += 1

    z_counts = [0] * (t + 1)
    z_counts[0] = initial_z_count_at_step_0

    for i in range(1, t + 1):
        from_s = initial_z_contrib[i]
        # 'z's from the 'a' part of an "ab" split (26 steps ago)
        from_prev_z_a = z_counts[i - 26] if i >= 26 else 0
        # 'z's from the 'b' part of an "ab" split (25 steps ago)
        from_prev_z_b = z_counts[i - 25] if i >= 25 else 0

        z_counts[i] = (from_s + from_prev_z_a + from_prev_z_b) % MOD

    string_length = len(s)
    for i in range(t):
        string_length = (string_length + z_counts[i]) % MOD
    return int(string_length)


def tests():
    s = 'v'
    t = 7
    res = length_after_transformations(s, t)
    print(f"result is {res}")
    assert res == 2


tests()
