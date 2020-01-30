"""
Develop a separated module the includes the definition for the Student class.
The variables each Student object should have are 'firstName', 'lastName', 'id' and 'average'.
Develop a simple separated module (that uses the student module)
that includes simple code for creating a list of objects. Each object represents a specific
student in class. Your code should calculate the students average and print it to the screen.
"""


class Student:
  def __init__(self, sid, fname, lname, avg):
    self.__sid = 1
    self.__fname = "no_fname"
    self.__lname = "no_lname"
    self.__avg = 1
    self.sid = sid
    self.fname = fname
    self.lname = lname
    self.avg = avg

  @property
  def sid(self):
    return self.__sid

  @sid.setter
  def sid(self, value):
    self.__sid = value

  @property
  def fname(self):
    return self.__fname

  @fname.setter
  def fname(self, value):
    self.__fname = value

  @property
  def lname(self):
    return self.__lname

  @lname.setter
  def lname(self, value):
    self.__lname = value

  @property
  def avg(self):
    return self.__avg

  @avg.setter
  def avg(self, value):
      if 100 >= value >= 0:
        self.__avg = value

  def __str__(self) -> str:
    return "im a student, my avg is " + str(self.avg) + " my last name:" + str(self.lname)

  def __repr__(self) -> str:
    return self.__str__()


students = [
  Student(124, "mosh", "levy", 80),
  Student(12284, "mos2h", "lkaslasvy", 97),
  Student(122384, "mos21h", "sad", 95),
  Student(112284, "mo1s2h", "gea", 91),
  Student(122284, "mos32h", "fasd", 92)
]


best_students = filter(lambda x: x.avg > 85, students)
for best in best_students:
  print(best)


