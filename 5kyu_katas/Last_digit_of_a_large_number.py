'''
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b.
Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969.
The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6. Also, please take 0^0 to be 1.

You may assume that the input will always be valid.
'''

def last_digit(n1, n2):
    end = {0: [0, 0, 0, 0],
           1: [1, 1, 1, 1],
           2: [2, 4, 8, 6],
           3: [3, 9, 7, 1],
           4: [4, 6, 4, 6],
           5: [5, 5, 5, 5],
           6: [6, 6, 6, 6],
           7: [7, 9, 3, 1],
           8: [8, 4, 2, 6],
           9: [9, 1, 9, 1]}

    return 1 if n2 == 0 else end[n1 % 10][(n2 % 4)-1]

assert last_digit(4, 1) == 4
assert last_digit(4, 2) == 6
assert last_digit(9, 7) == 9
assert last_digit(10, 10 ** 10) == 0
assert last_digit(2 ** 200, 2 ** 300) == 6