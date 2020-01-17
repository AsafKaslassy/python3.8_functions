#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "asaf.kaslassy@gmail.com"

import os
import re
import io
import sys
import math
import time
import glob
import utils
import pprint
import socket
import shutil
import logging
import turtle
import random
import logging
import pyperclip
# import pandas as pd
import urllib.request
# import pymysql.cursors
import xml.dom.minidom
from fractions import Fraction
# from utils import MathUtilsException

# GLOBALS
numbers = [12, 3, 6, -5, -12, -8, 13, 62]
sequence1 = [1, 2, 3, 4, 5, 6]
sequence2 = [3, 4, 5, 6]

source = r"C:\Users\Assaf\PycharmProjects\untitled\output\circles"
destination= r"C:\Users\Assaf\PycharmProjects\untitled\output\circles\images"

# david_average
david_marks = {
  "math": 90,
  "physics": 92,
  "chemistry": 80,
  "history": 70
}
# CRED = '\033[91m'
# CEND = '\033[1m'

factorial_exception_message = """FactorialException\n
                            \n a number for which it is not possible
                            \n to calculate factorial
                            \n(number smaller than 0)
                            """

Triangle_exception_message = """
\tTriangle_exception:
\tThe Triangle Inequality Theorem states
\tthat the sum of any 2 sides of a triangle
\tmust be greater than the measure of the third side.
                            """

logger = logging.getLogger('python3_8_log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('python3_8_log.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO )
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)



def paste_func_template(func_name):
  lower = func_name.lower()
  lower.replace(' ', '_')
  no_spaces = '_'.join(lower.split())
  final_func_name = no_spaces + '()'
  final_func = "\n\n" + "def " + final_func_name + ':\n  """\n  ' + final_func_name + '\n  """\n  \n  pass\n'
  pyperclip.copy(final_func)
  pyperclip.paste()
  print(final_func)


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


def simple_average():
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
  # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  list = [n * n for n in numbers]

  print(list)


def calc_factorial(number):
  if number == 0:
    return 1

  else:
    return number * calc_factorial(number - 1)

  # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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


def map_of_factorial(n):
  if n == 0:
    return 1
  else:
    return n * map_of_factorial(n - 1)


"""
factorials = map(Map_of_factorial,[1,2,3,4,5,6])
for number in factorials:
   print(number)
firstnames = ["moshe","haim","daniela"]
familynames = ["israeli","michael","darky"]
names = zip(firstnames,familynames)
for ob in names:
   print(ob[0]+" "+ob[1])
numbers=[12,3,6,-5,-12,-8,13,62]
def check(n) :
   if n>0:
       return n
   else:
       return "michael"
vec = filter(check,n )
for number in vec:
   print(number)
numbers = [12,3,6,-5,-12,-8,13,62]
vec = filter(check,numbers )
for number in numbers:
 if number>0:
   print (number)
 else:
   print("negative")
"""


def Filtering_Positive_Numbers():
  def check(n):
    if n > 0:
      return n
    else:
      return False

  vec = filter(check, numbers)

  for number in vec:
    print(number)
    pass



def use_my_utils(a, b):
  differenceof = utils.differenceof(a, b)
  sumof = utils.sumof(a, b)
  multiplyof = utils.multiplyof(a, b)
  divide = utils.divide(a, b)
  print(differenceof)
  print(sumof)
  print(multiplyof)
  print(divide)


def directories():
  """
  Develop a simple application that calculates
  the number of files and the number of sub-folders
  in the current folder... and prints these numbers to the screen
  """
  dirname = r'D:\pythonProjects'
  names = os.listdir(r'D:\pythonProjects')
  for name in names:
    if name.endswith(".py"):
      print(name, "file is located here:\n --->", os.path.join(dirname, name))

  print(glob.glob(dirname + '/*.py'))
  print("number of *.py (python) files :", len(glob.glob(dirname + '/*.py')))


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


def simple_dict_object_assignment(math, physics, chemistry, history):
  """
  Develop a simple script that includes the definition
  of the average function. The average function has
  four parameters: math, physics, chemistry, and history.
  The average function should receive the marks in these
  four subjects and return their average.
  You should include the required code for calculating David's average.
  David's marks (90 in math, 92 in physics, 80 in chemistry and 70 in history)
  should be passed over packed in a dict object.
  """
  subjects = (math, physics, chemistry, history)
  calced_average = sum(subjects) / len(subjects)
  print("David's Avarage of his grades:{0} is : {1}".format(subjects, calced_average))


def average(david, avi, ronen, galit):
  """
  The average function should receive the marks of all students
  packed in a dict object and then calculate their average and return it.
  Call the func like this :
  result = average(david=82, avi=90, ronen=78, galit=92)
  """
  students = (david, avi, ronen, galit)
  calculated_average = sum(students) / len(students)
  return calculated_average


def lambda_expression_simple_list_filtering():
  """
  Develop a simple program that creates a list of strings.
  Use the filter function for getting a new list of strings
  that includes those strings from the original
  list that their length is smaller than 10.
  Your solution should use a lambda expression.
  """
  list_of_strings = ["asaf", "sdsdsddsds", "gsgs", "dyfhgdtfghgdfhgfhdf"]
  filtered_strings = filter(lambda txt: filter_string_length(txt), list_of_strings)

  def filter_string_length(text):
    if len(text) < 10:
      return True
    else:
      return False

  for string in filtered_strings:
    print(string)


def intersect_function_list_comprehension_expression(sequence1, sequence2):
  """
  Define a function that is capable of calculating the intersection between two sequences.
  Your function should use the list comprehension expression.
  You should check your function by calling it and passing over two strings.
  """

  intersection_sequence = []

  for num in sequence1:
    if num in sequence2:
      intersection_sequence.append(num)
  return intersection_sequence


def recursive_factorial():
  """
  Define a recursive function that is capable of calculating the factorial of the passed argument.
  """

  pass


# __________collections:______________#
def the_set_operators():
  """
  Given the following two sets:
  one = {'a','b','c','d','e','f','g','h'}
  two = {'a','d','g'}
  Calculate the value of each one of the following expressions:
  """
  one = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
  two = {'a', 'd', 'g'}
  if 'a' in one:
    print("'a' in one")
  print(one - two)
  print(one | two)
  print(one & two)
  print(one ^ two)
  print(set('bcd') < one)
  print(set('abcde') > one)

class Student:
  pass

def comprehension_set_of_students():
  """
  You should develop a set that includes tuples as its elements.
  Each tuple holds the values that describe a specific student.
  You should create a comprehension set of Student objects
  based on the set of tuples. You should define the Student class accordingly.
  In addition, your code should iterate the set of Student objects
  and print the description of each one of them to the screen.
  """


def lotto_numbers():
  """
  Develop a simple application that
  generates 6 randomly selected numbers
  in the range 1..42. The numbers must
  be unique (they cannot repeat themselves).
  Your solution should use the Set collection.
  """
  numbers_list = []
  for num in range(1, 42 + 1):
    numbers_list.append(num)
  numbers_set = set(numbers_list)
  # print (numbers_set)
  print("The *set* of 6 Lotto winning numbers are : ")
  print(set(random.sample(numbers_set, 6)))


# __________XML:______________#


def bank_israel_currency_exchange_rates():
  """
  You should develop a simple application that prints out
  the current exchange rates of all currencies Bank Israel
  can provide us with their exchange rates. You can find
  all currencies' exchange rates at
  https://www.boi.org.il/currency.xml
  """

  document = xml.dom.minidom.parse("currency.xml")
  mapping = {}

  codes1 = document.getElementsByTagName("CURRENCYCODE")
  rates1 = document.getElementsByTagName("RATE")

  codes2 = map(lambda ob: ob.firstChild.data, codes1)
  rates2 = map(lambda ob: ob.firstChild.data, rates1)

  tuples = zip(codes2, rates2)

  for tpl in tuples:
    print(tpl)


def currencies_tcp_ip_client_server(currency_code):
  """
  You should develop a TCP/IP server that
  receives a currency code (e.g. USD, EURO etc..)
  and returns its exchange rate.
  In addition, you should develop a TCP/IP client
  application that receives from the user a currency
  code and prints out its exchange rate.
  The TCP/IP client application should interact with the server
  """
  currency_code = None
  rate = None

  return rate


# __________Exceptions:______________#


class FactorialException(Exception):
  pass


class StudentsPlatformException(Exception):
  pass


def the_factorial_assignment(num):
  """
  Define the FactorialException class.It should extend Exception.
  Define the factorial function. Whenever the factorial function receives a number for which
  it is not possible to calculate factorial (number smaller than 0)
  an exception should be thrown. It should be of the FactorialException type.
  Check your definition for the factorial function by calling it passing over a negative number.
  """

  if num < 0:
    time.sleep(0.1)
    raise FactorialException
  return 10 * num


# try:
#  num = 18-12
#  print(the_factorial_assignment(num))
# except FactorialException:
#   print(factorial_exception_message)
# print('continue...')


def the_mathutils_module_assignment(a, b):
  """
  The new module should include the definition for the MathUtilsException class.
  MathUtilsException should extend Exception.When trying to call the divide
  function passing over 0 as the second argument a MathUtilsException should be raised.
  """
  # if b == 0:
  #   print("0 detected")
  #   time.sleep(1)
  #   raise ZeroDivisionError
  # divide = utils.divide(a, b)
  # return divide


"""
# try:
#   a,b = 4,0
#   print(a,"/",b,"=",round(the_mathutils_module_assignment(a,b),ndigits=3))
# except ZeroDivisionError:
#   print("You tried dividing by zero \n "
#         "Zero division error:")
# print('continue...')
"""




# __________Files:______________#

def road_prayer():
  """
  creates a new file with road prayer (in Hebrew)
  saved into it. The road prayer should be in Hebrew
  and it should be in UTF8.
  """
  road_prayer_text_in_hebrew = """
           יְהִי רָצוֹן מִלְפָנֶיךָ יְיָ אֱלֹהֵינוּ וֵאלֹהֵי אֲבוֹתֵינוּ,
          שֶׁתּוֹלִיכֵנוּ לְשָׁלוֹם וְתַצְעִידֵנוּ לְשָׁלוֹם וְתַדְרִיכֵנוּ לְשָׁלוֹם (וְתִסְמְכֵנוּ לְשָׁלוֹם),
          וְתַגִּיעֵנוּ לִמְחוֹז חֶפְצֵנוּ לְחַיִּים וּלְשִׂמְחָה וּלְשָׁלוֹם.
"""
  print(road_prayer_text_in_hebrew)
  filename = "road_prayer_in_hebrew"
  with open(filename + '.txt', 'w', encoding='utf8') as filepath:
    filepath.write(road_prayer_text_in_hebrew)


def the_id_numbers_assignment():
  """
  reads the ID numberas from the file and prints them to the screen.
  Your short program should use the Set collection in order to
  avoid printing the same ID number more than once.
  """
  # _____random_ID_generator_______#
  Final_ID_List = set()
  number_of_IDs = 0

  while number_of_IDs < 10:
    random_ID = random.randint(301000000, 302000000)
    # random_ID = random.randint(10,11)
    number_of_IDs += 1
    Final_ID_List.add(random_ID)

  # Final_ID_List = [301467098,123,343,123,435,235,145,123,232,
  #                    123,123,343,123,435,235,145,123,232,]
  filename = "ID_numbers"

  # write to file:
  with open(filename + '.csv', 'w') as filepath:
    for num in Final_ID_List:
      filepath.write(str(num) + '\n')

  # read from file:
  readfile = open(filename + '.csv', 'r')
  ID_numbers_set = set()
  for ID in readfile:
    ID_numbers_set.add(ID)
  id_numbers_no_dup = list(ID_numbers_set)
  final_id_numbers = []
  for item in id_numbers_no_dup:
    final_id_numbers.append(item[0:-1])
  print("\n\tOriginal ID list:\t\t", Final_ID_List)
  print(len(Final_ID_List))
  print("\nID list with no duplicates:", final_id_numbers)
  print(len(final_id_numbers))


class Student:
  def __init__(self, idVal, nameVal, marksVal):
    self.id = idVal
    self.name = nameVal
    self.marks = marksVal


class Mark:
  def __init__(self, subject, mark):
    self.subject = subject
    self.mark = mark


def students_average_calculation():
  """
  Given a CSV file (each line includes strings separated using commas) that lists students marks...
  each row (id, name, mark, course) describes a specific student mark in a specific course,
  you should develop a simple application that creates a dict object for representing all students and their average.
  The dict keys should be the students IDs. The dict values should be objects instantiated from the Student class.
  Each Student object should have the marks attribute that holds the reference for a list of Mark objects.
  You should define the Student and the Mark classes separately. Once the entire data was read and processed
  the application should calculate the students' average (the average of all students' averages)
  """
  students = dict()

  with open(r"D:\pythonProjects\StudentAvarages.csv", mode='r') as file:
    lines = file.readlines
    for line in lines:
      text = line.split(",")
      if text[0] in students:
        students[text[0]].marks.append(Mark(text[3], text[2]))

  def students_data(self):
    """
    getStudent(id), getStudents(), saveStudent(ob). You should define the Student class.
    The data of each and every student should be saved in a separated file.
    The name of each file should be the id number of the student its data is saved within the file.
    Make sure, all students files are saved within a specific folder. In addition, you should define a new exception class.
    Its name should be StudentsPlatformException. Write simple code for checking the module you developed
    """
    pass

  def getStudent(self, id):
    pass

  def getStudents(self):
    pass


def students_simple_data():
  """
  Create a CSV file that holds data about 10 of your friends.
  Develop a simple application that reads the data from the CSV file and prints it to the screen.
  The data should include (at the minimum) the student's ID and their average.
  Your code should include the use of regular expression for validating the ID and the average.
  Rows with invalid data won't be printed out to the screen.
  """

  user_input = 'asde4a12@gmail.com'

  phone_pattern_ten_digits = r'^[0-9]{3}[-][0-9]{7}$'
  id_pattern_nine_digits = r'^[0-9]{9}$'
  e_mail_pattern = "\A[^@]+@[^@]+\.[^@]{2,4}"

  result = re.search(e_mail_pattern, user_input)
  if result:
    print("match")
    print(result)
  else:
    print("no match")






  """
  readfile = open('StudentAvarages' + '.csv')
  for value in readfile:
    splitted = value.split()
    # print(splitted)
"""


# csv_path = r"C:\Users\Assaf\PycharmProjects\untitled\StudentAvarages.csv"
# df_id = pd.read_csv(csv_path,usecols=['id'])
# df_avg = pd.read_csv(csv_path,usecols=


def simple_files_copying(source,destination):
  """
  simple application that goes over all files
  in the current directory and copies all image files
  extension is 'jpg' or 'gif' or 'png') to a new subfolder,
  that its name is 'images'.
  """

  valid_extensions = [".jpg", ".jpeg", ".gif", ".png"]
  logger.info('valid_extensions = %s' % valid_extensions)
  logger.info('Source = %s' % source)
  logger.info('destination = %s' % destination)
  fileNames = os.listdir(source)
  for filename in fileNames:
    logger.info('\t %s' % filename)

  if not os.path.exists(destination):
    try:
      os.makedirs(destination+'\\images')
    except:
      raise OSError


  logger.info("Started copying")

  for file in fileNames:
    source_full_file_path = os.path.join(source, file)
    extension = os.path.splitext(file)[1]
    if extension.lower() in valid_extensions:
      logger.info("copying {}\{} to ---> {}\{}".format(source, file, destination, file))
      shutil.copy(source_full_file_path, destination)

    else:
      continue
  os.startfile(destination)
  logger.info('opening folder : %s' %destination)
  logger.info('finished successfully')



def multiplication_numbers():
  """
  Develop a simple application that receives numbers
  through the command line and prints out their multiplication with each other.
  You should use sys.argv.
  """

  mult = 1
  for n in sys.argv:
    try:
      mult = mult * int(n)
    except:
      None
  logger.info("the Mult of {} is :".format(sys.argv[1:]))
  logger.info(mult)


def comparing_files():
  """
  Develop a simple application that receives through the command line the
  names of two files that hold texts in english. The application should logger.info
  True if the content is exactly the same,
  and False (otherwise). The optional "--ignorecase" argument will
  turn the comparison into a none case-sensitive one.
  """
  first_file = sys.argv[1]
  second_file = sys.argv[2]
  logger.info("comparing:\n'{0}' \n Vs. \n'{1}'\n".format(first_file, second_file))
  first_file_path = open(first_file, 'r')
  first_file_list = []
  for word1 in first_file_path:
    first_file_list.append(word1)
  logger.info(first_file_list)

  second_file_path = open(second_file, 'r')
  second_file_list = []
  for word2 in second_file_path:
    second_file_list.append(word2)
  logger.info(second_file_list)

  if first_file_list == second_file_list:
    logger.info("\n\tTrue ! , file are the same")
  else:
    logger.info(" \nFalse ! , files are not the same")


# ______databases_MySQL_____________#


# def mySQL():
#   # connect with the database
#   connection = pymysql.connect(host='localhost',
#                                user='israel',
#                                password='usa',
#                                db='israel',
#                                charset='utf8',
#                                port=3306,
#                                cursorclass=pymysql.cursors.DictCursor)
#   try:
#     with connection.cursor() as cursor:
#       sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s)"
#       cursor.execute(sql, ('haimm', '12345'))
#     # we must commit in order to have the changes saved
#     connection.commit()
#
#   finally:
#     connection.close()


# __________reqularExpression_________#


def regularExpressionDemo():
  pattern = re.compile("\d+g+")
  result = pattern.match("1233gggfasf43gggggg2", 3, 5)
  if result:
    logger.info("match")
  else:
    logger.info("no match")


class TriangleException(Exception):
  pass


class Triangle:
  """
  Define the Triangle class. The __init__ method should allow us to specify the lengths of the three sizes.
  If the three lengths cannot form a triangle a TriangleException should be raised.
  Write a short program for testing the Triangle class you defined
  """

  def __init__(self,A_length,B_length,C_length):
    self.A_length = A_length
    self.B_length = B_length
    self.C_length = C_length


def the_triangle_assignment_test(A_length,B_length,C_length):

    The_Triangle_Inequality_Throrem = A_length + B_length > C_length and \
                                      C_length + B_length > A_length and \
                                      A_length + C_length > B_length
    if not The_Triangle_Inequality_Throrem:
      raise TriangleException

    #   logger.info(CRED,Triangle_exception_message,CEND)
    #   logger.info (" A_length = {}\n B_length  = {}\n C_length = {}\n".format(A_length,B_length,C_length))
    #   logger.info ("""
    #           A + B > C
    #           C + B > A
    #           A + C > B
    #           """)
    #   os.startfile(r"C:\Users\Assaf\PycharmProjects\untitled\triangle_inequality_theorem.JPG")
    #
    #   time.sleep(1)
    #   raise TriangleException
    # else:
    #   logger.info (" A_length = {}\n B_length  = {}\n C_length = {}\n".format(A_length,B_length,C_length))
    #   logger.info (" The_Triangle_Inequality_Throrem is satisfied for all 3 conditions of the sides ")
    #
    #   #Draw Triangle using Turtle python lib
    #   draw = turtle.Turtle()
    #   draw.write("Triangle", True, align="right", font='david')
    #   draw.pensize(10)
    #   draw.screen.bgcolor("orange")
    #   draw.forward(100)
    #   draw.left(120)
    #   draw.forward(100)
    #   draw.fillcolor("violet")
    #   draw.left(120)
    #   draw.forward(100)
    #   turtle.done()


class BankException(Exception):
  pass


class BankAccount(object):
  """
  the following methods: deposit(self,sum) and withdraw(self,sum).
  Each object instantiated from BankAccount should have the balance attribute.
  my_sum
  """
  def __init__(self, my_sum, starting_balance):
    self.my_sum = my_sum
    self.starting_balance = starting_balance

  def deposit(self, my_sum):
    # deposit = starting_balance + my_sum
    pass

  def withdraw(self, my_sum):
    # withdraw = starting_balance - my_sum
    pass


def bank_account_exception_assignment(starting_balance, deposit_sum, withdraw_sum):
  """
  Define the BankAccount class. It should include the following methods: deposit(self,sum) and withdraw(self,sum).
  Each object instantiated from BankAccount should have the balance attribute.
  When trying to withdraw a sum bigger than the balance a BankException should be raised
  and the balance should remain the same. BankException should extend Exception.
  You should create a simple program that creates a new account with a balance of $100,
  deposits $90 and then withdraws $200. The simple program should print out the balance
  (after all operations took place).
  """

  # starting_balance = 100
  if withdraw_sum == "":
    withdraw_sum = 0
  if withdraw_sum == 0:
    logger.info("no withdraw")

  # deposit = starting_balance + deposit_sum
  # withdraw = starting_balance - withdraw_sum

  logger.info("deposit_sum =", deposit_sum)
  logger.info("withdraw_sum =", withdraw_sum)


  current_balance = starting_balance + deposit_sum - withdraw_sum

  if current_balance > starting_balance:
    logger.info("the current balance after all operations took place is: ",  current_balance)

  while current_balance < starting_balance:
    try:
      logger.info( "Illegal operation: \nTrying to withdraw a sum bigger than the balance")
      logger.info("\tThe current balance stays the same: ", starting_balance)
      break
    except BankException:
      raise BankException



















def main():
  """
  uncomment the function you want to run
  """

  # result = average(david=82, avi=90, ronen=78, galit=92) ;print("Avarage:",result) #TODO:done
  # print(intersect_function_list_comprehension_expression(sequence1, sequence2))     #TODO:done
  # lambda_expression_simple_list_filtering()   #TODO:done
  # fractions()                                 #TODO:done
  # print_words_into_file()                     #TODO:done
  # read_lines_from_file()                      #TODO:done
  # simple_average()                            #TODO:done
  # trenary_operator()                          #TODO:done
  # simple_while_loop()                         #TODO:done
  # tuple_swap()                                #TODO:done
  # list_of_tuples()                            #TODO:done
  # dic_of_tuples()                             #TODO:done
  # simple_comprehensive_list()                 #TODO:done
  # calc_factorial()                            #TODO:done
  # total_income()                              #TODO:done
  # calc_list_of_tuples()                       #TODO:done
  # calc_sum_of_tuples()                        #TODO:done
  # map_of_factorial()                          #TODO:done
  # Filtering_Positive_Numbers()                #TODO:done
  # comprehension_list_of_averages()            #TODO:done
  # simple_dict_object_assignment(**david_marks)#TODO:done
  # use_my_utils(10, 5)                         #TODO:done
  # directories()                               #TODO:done
  # average(**student_marks)                    #TODO:done
  # recursive_factorial()                       #TODO:done
  # the_set_operators()                         #TODO:done
  # lotto_numbers()                             #TODO:done
  # road_prayer()                               #TODO:done
  # the_id_numbers_assignment()                 #TODO:done
  # simple_files_copying()                      #TODO:done
  # multiplication_numbers()                    #TODO:done
  # comparing_files()                             #TODO:done
  # the_mathutils_module_assignment(a,b)        #TODO:done
  # bank_israel_currency_exchange_rates()       #TODO:done
  # students_data()
  # students_simple_data()                      #TODO:-almost done
  # comprehension_set_of_students()
  # currencies_tcp_ip_client_server()
  # the_factorial_assignment(num)
  # mySQL()
  # students_average_calculation()
  # regularExpressionDemo()
  # Triangle.the_triangle_assignment()
  # the_triangle_assignment_test(A_length=12, B_length=13, C_length=14) #TODO: convert this func to work in class (?)
  # bank_account_exception_assignment(starting_balance=100, deposit_sum=50, withdraw_sum=0)
  # simple_files_copying(source = source , destination= destination)
  # commit_test





  # TODO:
  '''
    # students_data()
    comprehension_set_of_students()
    currencies_tcp_ip_client_server()
    the_factorial_assignment(num)
    mySQL()
    students_average_calculation()
    # Triangle.the_triangle_assignment()
  '''

  # _________________________________________________
  paste_func_template(func_name="The Triangle Assignment")


if __name__ == '__main__':
  main()