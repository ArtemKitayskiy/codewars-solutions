'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
'''

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: int(x / y)}

def zero(oper=''): return '0' if oper == '' else op[oper[1]](0, int(oper[0]))
def one(oper=''): return '1' if oper == '' else op[oper[1]](1, int(oper[0]))
def two(oper=''): return '2' if oper == '' else op[oper[1]](2, int(oper[0]))
def three(oper=''): return '3' if oper == '' else op[oper[1]](3, int(oper[0]))
def four(oper=''): return '4' if oper == '' else op[oper[1]](4, int(oper[0]))
def five(oper=''): return '5' if oper == '' else op[oper[1]](5, int(oper[0]))
def six(oper=''): return '6' if oper == '' else op[oper[1]](6, int(oper[0]))
def seven(oper=''): return '7' if oper == '' else op[oper[1]](7, int(oper[0]))
def eight(oper=''): return '8' if oper == '' else op[oper[1]](8, int(oper[0]))
def nine(oper=''): return '9' if oper == '' else op[oper[1]](9, int(oper[0]))

def plus(x): return x + '+'
def minus(x): return x + '-'
def times(x): return x + '*'
def divided_by(x): return x + '//'

assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3
