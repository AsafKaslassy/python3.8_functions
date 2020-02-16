"""
Define the class Course. It should describe an academic course taken in the university.
Your class should include the definition of the following instance variables:
name:String
id:long
startDate:DateTime
endDate:DateTime
teacher:Person
classroom:Room
Your Course class should include the definition of the PrintDetails() methods.
Calling that method on a specific Course object we should get its details printed out to the screen.
All instance variables should be defined with the private access modifier.
Each one of them should be defined together with a property that allows getting and setting its value.
The properties you define should include validation tests.
In addition, you should define the Room and the Person classes. Each one of them should include two instance variables,
 and two properties at the minimum.
You should instantiate the Course class you defined in order to get an object that represents
 the course in which you currently participate. Y
 ou should call the printDetails method on that object in order to get its details printed to the screen.
"""


class Course:
    def __init__(self,name,ID,startDate,endDate,teacher,classroom):
        self.__name = "no name"
        self.__ID = -1
        self.__startDate = -1
        self.__endDate = -1
        self.__teacher = "no teacher"
        self.__classroom = "no classroom"
        self.name = name
        self.ID = ID
        self.startDate = startDate
        self.endDate = endDate
        self.teacher = teacher
        self.classroom = classroom

    @property
    def name(self):
        return self.__name
    @property
    def ID(self):
        return self.__ID
    @property
    def startDate(self):
        return self.__startDate
    @property
    def endDate(self):
        return self.__endDate
    @property
    def teacher(self):
        return self.__teacher
    @property
    def classroom(self):
        return self.__classroom

    ##setters
    @name.setter
    def name(self, txt):
        if txt!=None:
            self.__name = txt
    @ID.setter
    def ID(self, num):
        self.__ID = num
    @startDate.setter
    def startDate(self,num):
        self.__startDate = num
    @endDate.setter
    def endDate(self,num):
        self.__endDate = num
    @teacher.setter
    def teacher(self,num):
        self.__teacher = num
    @classroom.setter
    def classroom(self,num):
        self.__classroom = num

    def __str__(self):
        return str(self.name)+","+str(self.ID)+","+str(self.startDate)+","+str(self.endDate)+","+str(self.teacher)+","+str(self.classroom)


    def PrintDetails(self):
        print("name,ID,startDate,endDate,teacher,classroom")
        return str(self.name)+","+str(self.ID)+","+str(self.startDate)+","+str(self.endDate)+","+str(self.teacher)+","+str(self.classroom)


class Person:
    def __init__(self, first, last, idVal):
        self.__firstName = "No First Name"
        self.__lastName = "No Last Name"
        self.__idVal = -1
        self.FirstName = first
        self.LastName = last
        self.Id = idVal
    @property
    def FirstName(self):
        return self.__firstName
    @property
    def LastName(self):
        return self.__lastName
    @property
    def Id(self):
        return self.__id

    ##setters
    @FirstName.setter
    def FirstName(self, txt):
        if txt!=None:
            self.__firstName = txt
    @LastName.setter
    def LastName(self, txt):
        if txt!=None:
            self.__lastName = txt
    @Id.setter
    def Id(self,num):
        self.__idVal = num


class Room:
    def __init__(self, RoomName, floor):
        self.__RoomName = "No Room Name"
        self.__floor = "No floor"
        self.RoomName = RoomName
        self.floor = floor
    @property
    def RoomName(self):
        return self.__RoomName
    @property
    def floor(self):
        return self.__floor

    ##setters
    @RoomName.setter
    def RoomName(self, txt):
        if txt!=None:
            self.__RoomName = txt
    @floor.setter
    def floor(self,num):
        self.__floor = num


ob = Course(name="Physics",ID="553503",startDate="21032020",endDate="21052020",teacher="Dr Amnon",classroom="503-3")

print(ob.name)