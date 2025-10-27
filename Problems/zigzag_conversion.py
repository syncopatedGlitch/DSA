'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


def convert(s: str, num_rows: int) -> str:
    # no zig zag possible for 1 row
    if num_rows == 1:
        return s
    # for rows > 1
    roof = 0
    floor = num_rows - 1
    matrix = [[] for _ in range(num_rows)]
    row = 0
    direction = "down"
    for char in s:
        if row >= roof and row < floor:
            if direction == "down":
                matrix[row].append(char)
                row += 1
            if direction == "up":
                matrix[row].append(char)
                if row > roof:
                    row -= 1
                else:
                    direction = "down"
                    row += 1

        elif row == floor:
            matrix[row].append(char)
            row -= 1
            direction = "up"
    final = ""
    for row in matrix:
        for char in row:
            final += char
    return final


def tests():
    s = "PAYPALISHIRING"
    numRows = 3
    res = convert(s, numRows)
    assert res == "PAHNAPLSIIGYIR"
    s = "PAYPALISHIRING"
    numRows = 4
    res = convert(s, numRows)
    assert res == "PINALSIGYAHRPI"


tests()
