'''
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome!
To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy,
and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers,
because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second,
9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make,
given the parameters of:
1. your referral bonus, and
2. the price of a beer can
'''

def beeramid(bonus, price):
    num_cans = int(bonus // price)
    if num_cans < 1:
        return 0
    if num_cans == 1:
        return 1

    num_cans -= 1
    levels = 1
    middle = 2
    side = 1

    while True:
        num_cans -= middle
        num_cans -= side * 2
        if num_cans >= 0:
            levels += 1
        else:
            break
        middle += side * 2 + 1
        side += 1

    return levels

assert beeramid(1500, 2) == 12
assert beeramid(5000, 3) == 16