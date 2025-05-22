class calculadora:

    def divide(n1, n2):
        if n2 == 0:
            raise ValueError
        return n1 / n2
    
import math

# clase padre
class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

# clases hijo circulo y rectangulo

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

# define funcion == si es que se busca 
# hacer una equivalencia entre esta clase y "otra"
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length,side_length)