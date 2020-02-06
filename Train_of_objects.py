"""
Define the class Locomotive and the class Cabin.
These two classes should allow the developers to
construct a graph of objects that represent a train.
Use these two classes for getting a graph of objects
that represent a train with 5 cabins.
"""


class Locomotive:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class Cabin:
  def __init__(self):
    self.head_value = None

  def print_details(self):
    print_value = self.head_value
    while print_value is not None:
      print(print_value.data)
      print_value = print_value.next

  def first_cabin(self, new_data):
    new_node = Locomotive(new_data)
    new_node.next = self.head_value
    self.head_value = new_node


cabin_list = Cabin()
cabin_list.head_value = Locomotive("Cabin #1")
cabin2 = Locomotive("Cabin #2")
cabin3 = Locomotive("Cabin #3")
cabin4 = Locomotive("Cabin #4")
cabin5 = Locomotive("Cabin #5")

cabin_list.head_value.next = cabin2
cabin2.next = cabin3
cabin3.next = cabin4
cabin4.next = cabin5

cabin_list.first_cabin("Locomotive")

cabin_list.print_details()
