# Exercitiul 1
"""
Creați clasele enumerate mai jos. Utilizați moștenirea.
Pentru toate proprietățile, utilizați sublinieri în interiorul clasei pentru a ascunde proprietățile
(exemplu self._inner_color) și declarați metode get și set (exemplu set_inner_color).
Creați o clasă care descrie o Formă (Shape)
Clasa Formă ar trebui să aibă următoarele proprietăți:
• culoarea interioară (inner color)
• culoarea marginii (border color)
Creați o altă clasă Cerc (Circle) care extinde clasa Formă (Shape).
Clasa cerc ar trebui să aibă următoarele proprietăți suplimentare:
• rază (radius)
Creați o altă clasă Dreptunghi (Rectangle) care, de asemenea, extinde clasa Formă (Shape)
Clasa dreptunghi ar trebui să aibă următoarele proprietăți suplimentare:
• lățime (width)
• lungime (length)
Creați o altă clasă Pătrat (Square) care extinde clasa Dreptunghi (Rectangle)
Clasa Pătrat ar trebui să se asigure că lățimea și lungimea sunt egale atunci când una dintre ele este setată.
 De exemplu, dacă setez square.set_length(4), square.get_width() ar trebui să fie și el 4.
"""


# Solution
# Crearea clasei Shape
class Shape:
    def __init__(self):
        self._inner_color = None
        self._border_color = None

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, color):
        self._inner_color = color

    def get_border_color(self):
        return self._border_color

    def set_border_color(self, color):
        self._border_color = color


# Crearea clasei Circle
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self._radius = None

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius


# Crearea clasei rectangle
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self._width = None
        self._length = None

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length


# Creare clasei Square
class Square(Rectangle):
    def set_width(self, width):
        super().set_width(width)
        self._length = width  # Keep length equal to width when width is set.

    def set_length(self, length):
        super().set_length(length)
        self._width = length  # Keep width equal to length when length is set.
