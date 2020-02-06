"""
Define the class Student.
Create a list of 6 Student objects that represent the students in your class.
Use the max function for finding the student with the highest average.
"""


class Student:
  def __init__(self, sid, fname, lname, avg):
    self.sid = sid
    self.fname = fname
    self.lname = lname
    self.avg = avg

  def __str__(self):
    return " \nfirst name: "+self.fname + "  \nlast name:  "+ self.lname + " \nAvarage: "+str(self.avg)


students = [
  Student(124, "mosh", "levy", 80),
  Student(12284, "mo", "lklasvy", 97),
  Student(122384, "mos21h", "sad", 95),
  Student(112284, "mo1s2h", "gea", 91),
  Student(112284, "asaf", "kaslassy", 100),
  Student(122284, "mos32h", "fasd", 92)
]

beststudent = lambda dat: max(dat, key=lambda ob: ob.avg)
print(beststudent(students))


