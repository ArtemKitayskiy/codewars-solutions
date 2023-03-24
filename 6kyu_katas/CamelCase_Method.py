'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
All words must have their first letter capitalized without spaces.
'''

def camel_case(string):
    return ''.join(map(lambda x: x[0].upper() + x[1:], string.split()))

assert camel_case("hello case") == 'HelloCase'
assert camel_case("camel case word") == 'CamelCaseWord'