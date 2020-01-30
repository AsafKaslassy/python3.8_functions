class Car:
  def __init__(self, model, Car_id, brand, year):
    self.__model = "no model"
    self.__Car_id = "no carID"
    self.__brand = "no brand"
    self.__year = "no year"

    self.model = model
    self.Car_id = Car_id
    self.brand = brand
    self.year = year

  def __repr__(self):
    return "\nmy car is " + " \n model: " + \
           str(self.model) + "\n Car_id: " + \
           str(self.Car_id) + " \n brand: " + \
           str(self.brand) + "\n year: " + \
           str(self.year)

  # def __repr__(self) -> str:
  #   return self.__str__()

  @property
  def model(self):
    return self.__model

  @model.setter
  def model(self, value):
    self.__model = value

  @property
  def Car_id(self):
    return self.__Car_id

  @Car_id.setter
  def Car_id(self, value):
    self.__Car_id = value

  @property
  def brand(self):
    return self.__brand

  @brand.setter
  def brand(self, value):
    self.__brand = value

  @property
  def year(self):
    return self.__year

  @year.setter
  def year(self, value):
    self.__year = value


cars = [
  Car(model="Corolla", Car_id=" 1234567", brand=" Toyota", year=" 2015"),
  Car(model="yaris", Car_id=" 1233267", brand=" Toyota", year=" 2018")
]
print(cars)
