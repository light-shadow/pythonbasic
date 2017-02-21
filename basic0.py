#List List Comprehensions
L1 = ['Hello', 'World', 18, 'Apple', None]
to make L1 like ['hello', 'world', 'apple']
l2 = [i.lower() for i in L1 if isinstance(i, str) and i != None]
