"""
Develop a small application that converts a list of tuples
that describe students into a list of objects instantiated from Student.
You should use the 'map' built in function.
"""


listofTuples = [('foo', 'bar', 'baz', 'qux', 'quux', 'corge')]
print(type(listofTuples))
map(lambda ob:Student(ob[0],ob[1]),students1)
# result = map(addition, numbers)
# print(list(result))