"""
Develop a small application that converts a list of tuples
that describe students into a list of objects instantiated from Student.
You should use the 'map' built in function.
"""
# sid, fname, lname, avg
listofTuples = [(123, "David", "kahana", 98), (456, "dani", "kahdana", 94), (235, "Daff", "kadhana", 91)]
print(type(listofTuples))


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
    self.__avg = value

  def __str__(self) -> str:
    return "im a student "+ self.fname + self.lname + str(self.avg)

  def __repr__(self) -> str:
    return self.__str__()


# def convert(ob):
#   return Student(ob[0], ob[1], ob[2], ob[3])
# Tuple Un-Packing ->  (*ob) == ob[0], ob[1], ob[2], ob[3]

result = map(lambda ob: Student(*ob), listofTuples)
print(list(result))
