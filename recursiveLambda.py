"""
You should develop a lambda expression that describes a recursive function
 we can use for calculating the multiplication of all numbers a list includes.
"""

numList = [1, 2, 4, 6, 8, 10]
# result = [numList[i] * numList[i + 1] for i in range(len(numList)-1)]
# print(result)


def mult(a=4, b=2):
  if a == 0:
    return 0
  elif a == 1:
    return b
  else:
    return b + mult(a - 1, b)


print(mult())
