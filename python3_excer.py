import os
import sys
import math
from fractions import Fraction
import utils


def fractions():
  """Fractions exercise
  Create a list that holds Fraction objects that represent ½, ¾, ⅝ and ⅞.
  Create a copy for that list by calling the copy() function. Change the
  first fraction in the new list and print the first list to the screen.
  You should expect to see the original list.
  """
  fraction_list = [1 / 2, 3 / 4, 5 / 8, 7, 8]
  print("first list (original list)        ", fraction_list)
  list_copy = fraction_list.copy()
  list_copy[0] = 1 / 10
  print("copied list (changed 1st fraction)", list_copy)


def average():
  """You should develop a short program that creates a list
  that includes the following numbers:  12, 15 and 18.
  Your code should calculate the average of all numbers
  the list includes, and print it to the screen."""
  my_list = []
  for i in range(12, 19, 3):
    my_list.append(i)
  print("    my list  ", my_list)
  average_of_list = sum(my_list) / len(my_list)
  print("the average of the list is %d" % int(average_of_list))


def trenary_operator():
  """
  "hello" if b>a else "salam"
  'haifa' if b>a and b>0 else 'ramat-gan'
  109 if a>b else 'rehovot'
  'tel-aviv' if 'a' in ['a','b','c','d'] else 'rehovot'
  'tel-aviv' if 'a' in 'abcd' else 'rehovot'
  'blue' if 'b' not in "mosh" else 'red'
  'winter' if a>2 and a%2==1 else "summer"
  123 if 'y' not in 'yahoo' else 'x'"""


def print_words_into_file():
  users_text = input("enter your text you'd like to input: ")
  filepath = input("enter file name : ")
  filename = open(filepath + '.txt', 'w')
  filename.write(users_text)


def read_lines_from_file():
  filepath = input("enter file name : ")
  filename = open(filepath + '.txt', 'r')
  # print (filename)
  for word in filename:
    print(word)


def simple_while_loop():
  """
  Develop a simple program that calculates the multiplication
  of all numbers in between 1 and 10 (included).
  Your solution should use the while loop
  """

  n = 1
  sum = 0
  while n <= 10:
    sum += n
    n += 1
  print(sum)


def tuple_swap():
  """
  Develop a simple script that assigns two variables
   with two values and later swaps the two with each other.
    You should use the tuple unpacking statement.
  """
  a = 3
  b = 4
  print(a, b)
  a, b = b, a
  print(a, b)


def list_of_tuples():
  books = [

    (123123, "core php", 122, 39.9),
    (234432, "core java", 242, 49.9),
    (893123, "mongo in 8 days!", 128, 19.9),
    (923123, "scala now", 522, 34.9)
  ]

  for id, name, pages, price in books:
    print('id:', id, 'name:', name, 'page:', pages, 'price:', price)


def dic_of_tuples():
  books = {

    123123: (123123, "core php", 122, 39.9),

    234432: (234432, "core java", 242, 49.9),

    893123: (893123, "mongo in 8 days!", 128, 19.9),

    923123: (923123, "scala now", 522, 34.9)

  }
  for isbn in books:
    (id, name, pages, price) = books[isbn]

    print(id, name, pages, price)


def simple_comprehensive_list():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  list = [n * n for n in numbers]

  print(list)


def calc_factorial(number):
  if number == 0:
    return 1

  else:
    return number * calc_factorial(number - 1)

  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  list = [factorial(n) for n in numbers]

  print(list)


def create_custom_text_file():
  users_text = "10000.5 \n20000 \n410000.2 \n3000"
  filepath = 'incomes'
  filename = open(filepath + '.txt', 'w')
  filename.write(users_text)


def total_income():
  """
  The incomes.txt file includes the following lines:
  10000.5
  20000
  410000.2
  3000
  The following code should go over the numbers incomes.txt includes,
  calculate their sum and print it to the screen.
  """
  create_custom_text_file()

  sum = 0
  for string in open('incomes.txt'):
    sum += float(string)

  print(sum)


def calc_list_of_tuples():
  """
  The following list includes tuples.
  Each one of the tuples includes a number and its base.
  [(10001,2),(23432,5),(245334,8),(234234,7)]
  The following program should calculate the
  sum of all numbers and print it to the screen.
 You should complete the missing code.
  :return:
  """
  sum = 0
  numbers = [(10001, 2), (23432, 5), (245334, 8), (234234, 7)]
  for (number, base) in numbers:
    sum += int(str(number), base)
    print(number, base)
  print("sum: = ", sum)


def calc_sum_of_tuples():
  sum = 0
  for number in range(1, 100):
    sum += number

  print(sum)


def Map_of_factorial(n):
  if n == 0:
    return 1
  else:
    return n * Map_of_factorial(n - 1)


"""
# factorials = map(Map_of_factorial,[1,2,3,4,5,6])
# for number in factorials:
#    print(number)


# firstnames = ["moshe","haim","daniela"]
#
# familynames = ["israeli","michael","darky"]
#
# names = zip(firstnames,familynames)
#
# for ob in names:
#
#    print(ob[0]+" "+ob[1])


# numbers=[12,3,6,-5,-12,-8,13,62]
#
# def check(n) :
#
#    if n>0:
#
#        return n
#    else:
#        return "michael"
# vec = filter(check,n )
# for number in vec:
#    print(number)
#

# numbers = [12,3,6,-5,-12,-8,13,62]
# vec = filter(check,numbers )
# for number in numbers:
#  if number>0:
#    print (number)
#  else:
#    print("negative")

"""


# def Filtering_Positive_Numbers():
#   pass
#
#
# numbers = [12, 3, 6, -5, -12, -8, 13, 62]
#
#
# def check(n):
#   if n > 0:
#     return n
#   else:
#     return False
#
#
# vec = filter(check, numbers)
#
# for number in vec:
#   print(number)


def comprehension_list_of_averages():
  """
  You should develop a short program that creates a list of tuples.
  Each tuple should represent a specific student.
  Each tuple should hold the 'first name', 'last name', 'id' and 'average'
  (of the specific student that tuple represents).
  You should create a comprehension list of the averages of all students.
  """
  list_of_student_tuples = [
    ("Asaf", "Kaslassy", 301467098, 95),
    ("John", "Smith", 3000003, 90),
    ("Barbara", "Straised", 400004, 85),
    ("Jimmy", "Handrix", 500005, 80)
  ]
  grades_comprehension_list = [item[3] for item in list_of_student_tuples]
  for item in grades_comprehension_list:
    if item > 89:
      print(item)


# # mapDemo
# numbers1 = [1, 2, 3, 4, 5]


def f(price):
  in_dollars = price / 3.5
  return in_dollars


# numbers2 = map(f, numbers1)
#
# for num in numbers2:
#   print(num)

def average(math, physics, chemistry, history):
  """
  (Difficulty Level 2/5)
  Develop a simple script that includes the definition
  of the average function. The average function has
  four parameters: math, physics, chemistry, and history.
  The average function should receive the marks in these
  four subjects and return their average.
  You should include the required code for calculating David's average.
  David's marks (90 in math, 92 in physics, 80 in chemistry and 70 in history)
  should be passed over packed in a dict object.
  """
  # print("grades : ", math, physics, chemistry, history)
  david_marks = {
    "math": 90,
    "physics": 92,
    "chemistry": 80,
    "history": 70
  }

  # avarages_david = sum(david_marks.get())
  # print(avarages_david)


def use_my_utils(a, b):
  differenceof = utils.differenceof(a, b)
  sumof = utils.sumof(a, b)
  multiplyof = utils.multiplyof(a, b)
  print(differenceof)
  print(sumof)
  print(multiplyof)


def directories():
  """
  Develop a simple application that calculates
  the number of files and the number of sub-folders
  in the current folder... and prints these numbers to the screen

  """


# ____________________________________________________________________________________


def main():
  david_marks = {
    "math": 90,
    "physics": 92,
    "chemistry": 80,
    "history": 70
  }

  """
  uncomment the function you want to run
  """
  # fractions()
  # print_words_into_file()
  # read_lines_from_file()
  # average()
  # trenary_operator()
  # simple_while_loop()
  # tuple_swap()
  # list_of_tuples()
  # dic_of_tuples()
  # simple_comprehensive_list()
  # calc_factorial()
  # total_income()
  # calc_list_of_tuples()
  # calc_sum_of_tuples()
  # Map_of_factorial()
  # Filtering_Positive_Numbers
  # comprehension_list_of_averages()
  # average(**david_marks)
  use_my_utils(10, 5)


if __name__ == '__main__':
  main()
