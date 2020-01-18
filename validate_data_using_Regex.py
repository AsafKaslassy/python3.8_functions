import re
import csv
import time
import logging


# Logger
logger = logging.getLogger('python3_8_log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('python3_8_log.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

CRED = '\033[91m'
CEND = '\033[0m'


def students_simple_data(csv_path):
  """
  simple application that reads the data from the CSV file and prints it to the screen.
  the code includes the use of regular expression for validating the data.
  invalid data won't be printed out to the screen.
  """

  # items,  e_mail, ID_list, phone_num, name, grade, subject = []
  items = []
  e_mail_list = []     # 0
  ID_list = []         # 1
  phone_num_list = []  # 2
  name_list = []       # 3
  grade_list = []      # 4
  subject_list = []    # 5

  with open(csv_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
      items.append(row)
    for item in items:
      e_mail_list.append(item[0])
      ID_list.append(item[1])
      phone_num_list.append(item[2])
      name_list.append(item[3])
      grade_list.append(item[4])
      subject_list.append(item[5])

  logger.info("started parsing csv: {}".format(csv_path))
  logger.info("validating e-mails, IDs, and phone numbers")
  time.sleep(2)

  print("\n#______e-mail_______")
  e_mail_pattern = "^[^@]+\@[\w]+\.[^@]{2,5}$"
  count = 0
  for e_mail in e_mail_list:
    result = re.search(e_mail_pattern, e_mail)
    if result:
      print("e-mail: {} -> Valid".format(result[0]))
      # logger.info(result)
    else:
      print(f"{CRED}e-mail: %s ----> not Valid{CEND}" % e_mail)
      count += 1
  print("\tOut of {} e-mails {} are in-valid".format(len(e_mail_list), count))
  time.sleep(1)

  print("\n\t#______ID_______")
  id_pattern_nine_digits = r'^[0-9]{9}$'
  count = 0
  for user_id in ID_list:
    result = re.search(id_pattern_nine_digits, user_id)
    if result:
      print("\tID: {} -> Valid".format(result[0]))
    else:
      print(f"\t{CRED}ID: %s ----> not Valid{CEND}"%user_id)
      count += 1
  print("\t\tOut of {} IDs {} are in-valid".format(len(ID_list), count))
  time.sleep(1)

  print("\n\t\t#______phone_______")
  phone_pattern_ten_digits = r'^(\d{3}[-][0-9]{7}|\d{10})$'
  count = 0
  for phone_number in phone_num_list:
    result = re.search(phone_pattern_ten_digits, phone_number)
    if result:
      print("\t\tphone: {} -> Valid".format(result[0]))
    else:
      # print("\t\tphone: {} ----> not Valid".format(phone_number))
      print(f"\t\t{CRED}phone: %s ----> not Valid{CEND}" % phone_number)
      count += 1
  print("\t\t\tOut of {} phone numbers {} are in-valid".format(len(phone_num_list), count))

def main():
  csv_path = r"D:\git\python3.8_exercises\StudentAvarages.csv"
  students_simple_data(csv_path)


if __name__ == '__main__':
  main()
