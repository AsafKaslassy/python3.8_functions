"""
Define the class Locomotive and the class Cabin.
These two classes should allow the developers to
construct a graph of objects that represent a train.
Use these two classes for getting a graph of objects
that represent a train with 5 cabins.
"""


class Engine:
  def __init__(self, numberVal, brandVal):
    self.hp = numberVal
    self.brand = brandVal


class Locomotive:
  def __init__(self, idVal, engVal, nextVal):
    self.__id = None
    self.__next = None

    self.id = idVal
    self.next = nextVal
    self.engine = engVal

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):
    if value > 0:
      self.__id = value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, value):
    self.__next = value

  @property
  def engine(self):
    return self.__engine

  @engine.setter
  def engine(self, value):
    # if value.hp > 1000:
    self.__engine = value

  # def __str__(self) -> str:
  #   return "im a cabin, my id is "
  #
  # def __repr__(self) -> str:
  #   return self.__str__()


class Cabin:
  def __init__(self, idVal, nextVal):
    self.__id = None
    self.__next = None

    self.id = idVal
    self.next = nextVal

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):
    if value > 0:
      self.__id = value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, value):
    self.__next = value


locomotive = [
  Locomotive(124, Engine(2200, "toyota"),
             Cabin(424,
                   Cabin(323,
                         Cabin(3245,
                               Cabin(314,
                                     Cabin(424, None))))))
              ]
print("gaga")






