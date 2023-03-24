'''
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
'''

def tower_builder(n_floors):
    res = []
    for i in range(n_floors):
        res.append(' ' * (n_floors - i - 1) + '*' * i + '*' + '*' * i + ' ' * (n_floors - i - 1))
    return res


assert tower_builder(1) == ['*', ]
assert tower_builder(2) == [' * ', '***']
assert tower_builder(3) == ['  *  ', ' *** ', '*****']