'''
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).
'''

def two_sum(numbers, target):
    for first in range(len(numbers)):
        for second in range(first+1, len(numbers)):
            if numbers[first] + numbers[second] == target:
                return [first, second]


assert sorted(two_sum([1,2,3], 4)) == [0,2]
assert sorted(two_sum([1234,5678,9012], 14690)) == [1,2]
assert sorted(two_sum([2,2,3], 4)) == [0,1]