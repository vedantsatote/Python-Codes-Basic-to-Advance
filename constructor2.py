class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Creating instances of Rectangle
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

# Calculating area and perimeter
print(f"Area of rect1: {rect1.area()}")
print(f"Perimeter of rect1: {rect1.perimeter()}")

print(f"Area of rect2: {rect2.area()}")
print(f"Perimeter of rect2: {rect2.perimeter()}")
