import math as m

instances = []

class circle():
  def __init__(self, radius):
    self.radius = float(radius)

  def get_Diameter(self):
    return(self.radius*2)

  def get_area(self):
    return((self.radius**2)*m.pi)

  def get_radius(self):
    return(self.radius)

  def get_circumference(self):
    return(self.get_Diameter()*m.pi)

  def array_saver(self):
    dictionary = {
        "diameter" : self.get_Diameter(),
        "area" :self.get_area(),
        "radius" : self.get_radius(),
        "circumference" : self.get_circumference()
    }
    instances.append(dictionary)








user = float(input("Input a float for circle calculator... "))

c1 = circle(user)

c1.array_saver()

print(f"Your diameter is: ",c1.get_Diameter())
print(f"Your area is: ",c1.get_area())
print(f"Your radius is: ",c1.get_radius())
print(f"Your circumference is: ",c1.get_circumference())





print(instances)