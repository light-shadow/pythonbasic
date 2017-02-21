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
  
eg: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    def prod(L):
        def mulipy(a, b):
            return a *b
    return reduce(mulipy, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
>>> 3 * 5 * 7 * 9 = 945
