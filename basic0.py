#List List Comprehensions
L1 = ['Hello', 'World', 18, 'Apple', None]
to make L1 like ['hello', 'world', 'apple']
l2 = [i.lower() for i in L1 if isinstance(i, str) and i != None]

#Map and reduce 
class map(object):
    """
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """

eg: l = list(map(str, [1,2,3,4,5,6,7,8,9,0]))
>>> ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def reduce(function, sequence, initial=None): # real signature unknown; restored from __doc__
    """
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    """
    pass
  
eg: 1. reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    2.def prod(L):
        def mulipy(a, b):
            return a *b
    return reduce(mulipy, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
>>> 3 * 5 * 7 * 9 = 945

    3.CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


#Filter
class filter(object):
    """
    filter(function or None, iterable) --> filter object
    
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
eg: def is_odd(n):
        return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
