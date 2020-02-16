"""
Define the class Person and create a list of 5 Person objects that represent your best friends.
Each object instantiated from Person should be with the following attributes:
firstName, lasrtName, id and age.
Your code should iterate these friends and prints their details to the screen.
"""

class Person:
    def __init__(self, first, last, Id, age):
        self.__first = "No First Name"
        self.__last = "No Last Name"
        self.__Id = -1
        self.__age = -1
        self.first = first
        self.last = last
        self.Id = Id
        self.age = age

    @property
    def first(self):
        return self.__first
    @property
    def last(self):
        return self.__last
    @property
    def Id(self):
        return self.__Id
    @property
    def age(self):
        return self.__age

    @first.setter
    def first(self, txt):
        if txt!=None:
            self.__first = txt
    @last.setter
    def last(self, txt):
        if txt!=None:
            self.__last = txt
    @Id.setter
    def Id(self,num):
        self.__Id = num
    @age.setter
    def age(self,num):
        self.__age = num

    def __str__(self):
        return str(self.first)+","+str(self.last)+","+str(self.Id)+","+str(self.age)


bestFriends =  [Person(first="assdaf", last="assaf",Id="30145678", age="12"),
                Person(first="assdaf", last="akas", Id="30146098", age="320"),
                Person(first="asawaf", last="vkas", Id="31467098", age="30"),
                Person(first="aswaf", last="kfeas", Id="30146708", age="34"),
                Person(first="asfaf", last="kwaas", Id="30147098", age="380")]

print ("first, last,   Id,  age")
for friend in bestFriends:
    print (friend.first,friend.last,friend.Id,friend.age)

