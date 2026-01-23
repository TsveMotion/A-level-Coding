import math as m

class Triangle(): #Creating a class called triangle
  def __init__(self, side1, side2, side3, ): #Defines the construtctor for 3 sides of a triangle
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def getType(self): #Identifyer using the sides to id the type of triangle.
    if self.side1 == self.side2 == self.side3:
      return("Equilateral")
    elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
      return("Isosceles")
    else:
      return("Scalene")

  #Returns data when called for according side.
  def get_side1(self):
    return(self.side1)
  def get_side2(self):
    return(self.side2)
  def get_side3(self):
    return(self.side3)

  #Edits data when called for according side.
  def set_side1(self, new_side1):
    self.side1 = new_side1
  def set_side2(self, new_side2):
    self.side2 = new_side2
  def set_side3(self, new_side3):
    self.side3 = new_side3

#User Input for 3 side lengths of a triangle.
side1 = int(input("What is your length of side1: "))
side2 = int(input("What is your length of side2: "))
side3 = int(input("What is your length of side3: "))

#Creates the instance using the users data.
t1 = Triangle(side1, side2, side3)

#Prints the triangle type
print("Triangle Type: ", t1.getType())


