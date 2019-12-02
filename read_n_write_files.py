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
  fraction_list = [1/2 , 3/4, 5/8, 7,8]
  print ("first list (original list)        " , fraction_list)
  list_copy = fraction_list.copy()
  list_copy[0] = 1/10
  print ("copied list (changed 1st fraction)" , list_copy)


def average():
  """You should develop a short program that creates a list
  that includes the following numbers:  12, 15 and 18.
  Your code should calculate the average of all numbers
  the list includes, and print it to the screen."""
  my_list = []
  for i in range(12,19,3):
    my_list.append(i)
  print ("    my list  " ,my_list)
  average_of_list = sum(my_list) / len(my_list)
  print ("the average of the list is %d" %int(average_of_list))


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
  filename = open(filepath +'.txt','w')
  filename.write(users_text)
  # print (filename)
  # print (filepath)


def read_lines_from_file():
  filepath = input("enter file name : ")
  filename = open(filepath +'.txt','r')
  # print (filename)
  for word in filename:
    print (word)


def main():
  # fractions()
  # print_words_into_file
  # read_lines_from_file
  # average()
  trenary_operator


if __name__ == '__main__':
  main()
