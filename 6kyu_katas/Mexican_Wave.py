'''
Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

Rules
 1.  The input string will always be lower case but maybe empty.
 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
'''

def wave(people):
    res = []
    people =list(people)
    for i,v in enumerate(people):
        if v != ' ':
            people[i] = v.upper()
            res.append(''.join(people))
            people[i] = v.lower()
    return res


result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
assert wave("codewars") == result
result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
assert wave("two words") == result