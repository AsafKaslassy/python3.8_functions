

# def numbers():
#   for num in range(10):
#     print("num=", num)
#     yield num
#
#
# for number in numbers():
#   print(number)
#
# print(type(numbers()))


def simpleGeneratorFun():
  yield "1"
  yield 2
  yield [3,3,4]
  yield (3,3,4)
  # return ("1")
  # return ("2")
  # return ("3")


# Driver code to check above generator function
for value in simpleGeneratorFun():
  print(value)
