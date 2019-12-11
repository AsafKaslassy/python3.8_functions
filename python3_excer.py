import os
import sys
import math
from fractions import Fraction


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
  for id, name, pages, price in books:
    # (__, ____, _____, ____) = books[isbn]

    print(id, name, pages, price)


def simple_Comprehensive_List():
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
  numbers = [(10001,2),(23432,5),(245334,8),(234234,7)]
  for (number,base) in numbers:
    sum += int(str(number),base)
    print(number,base)
  print("sum: = ",sum)


def calc_sum_of_tuples():
  sum = 0
  for number in range(1,100):
    sum += number

  print(sum)




def Map_of_factorial(n):
  if n==0:
    return 1
  else:
    return n*Map_of_factorial(n-1)

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

numbers=[12,3,6,-5,-12,-8,13,62]
# vec = filter(check,numbers )
for number in numbers:
  if number>0:
    print (number)
  else:
    print("negative")



def c():
  pass


def d():
  pass


# ___________________________


def main():
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
  # simple_Comprehensive_List()
  # calc_factorial()
  # total_income()
  # calc_list_of_tuples()
  # calc_sum_of_tuples()
  # Map_of_factorial


  # TODO: understand dic_of_tuples()
  # TODO: understand   Map_of_factorial(1) vs Map_of_factorial


if __name__ == '__main__':
  main()
