class pasta:
    def __init__(self, whitepasta, italian):
        self.whitepasta =  whitepasta
        self.italian = italian
    
    def tasty(self):
        print("pasta ate")

       
    def cheese(self):
        print("yummy chesse")   

cooked_pasta = pasta("delious", "costly")
print(cooked_pasta.whitepasta)
print(cooked_pasta.italian)

"""
class American:
 def __init__(self, name, state) :
        self.name = name
        self.state = state

        def print_info(self):
          print(f"Name: {self,name}), state: {self.state}")

class NewYorker(American):
      def __init__(self, name, borough):
        super().__init__(name, "New york")

def print_info(self):
    super().print_info()
    print(f"borough: {self.borough}")

american = American("robbert", "california")
american.print_info()
new_yorker = NewYorker("michal", "florida")
"""
class Rectangle:
 def __init__(self, length, width):
  self.length = length
  self.width = width

def area(self):
  return self.length * self.width

def perimeter(self):
  return 2 * (self.length + self.width)

rect = Rectangle(4, 5)

print("Perimeter:", rect.perimeter())
