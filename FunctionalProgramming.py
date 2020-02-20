"""
Develop a small program that goes over the ID numbers stored in a file,
and for each one of the numbers calculates the magical numbers.
If a magical number of a given ID number is lower than 5
then the ID number is a suspected one. Your program should
print out all of the suspected ID numbers, and it should do it effectively using the yield statement.
"""

# MAGICAL NUMBER = SUM OF NUMBERS, IF BIGGER THAN 9, SUM AGAIN.


def g1():
  with open("ids")as f:
    for line in f:
      yield line


def g2():
  for text in g1():
    try:
      num = int(text)
      yield num
    except:
      print("error in type")


# MAGICAL NUMBER = SUM OF NUMBERS, IF BIGGER THAN 9, SUM AGAIN.
def g3():
  for num in g2():
    magical_number = calc(num)
    if magical_number < 5:
      yield num


def calc(num):
    number_splited_to_digits = [int(d) for d in str(num)]
    # print(number_splited_to_digits)
    summed_num = 0
    for digit in number_splited_to_digits:
      summed_num += digit
    # print("summed_num = ", summed_num)
    return summed_num


ob = g3()
for number in ob:
  print(number)
