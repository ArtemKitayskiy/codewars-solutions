'''
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
'''

def first_non_repeating_letter(string):
    lst = list(string.lower())
    for i,v in enumerate(lst):
        if lst.count(v) == 1:
            return string[i]
    return ''

assert first_non_repeating_letter('a') == 'a'
assert first_non_repeating_letter('stress') == 't'
assert first_non_repeating_letter('moonmen') == 'e'


