def f(age):
  def f1(num):
    if age < 80:
      return num + 10
    elif 80 <= age <= 100:
      return num + 5

  return f1


temp = f(85)(60)
print(temp)
