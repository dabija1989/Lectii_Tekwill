"""
Creați un serviciu pentru forme (Shape service).
Metodele din serviciul pentru forme (Shape service) ar trebui să fie toate staticmethods.
Serviciul pentru forme (Shape service) ar trebui să aibă următoarele proprietăți ca proprietăți ale clasei:
DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - Puteți alege orice valori implicite de tip șir (string).
Serviciul pentru forme (Shape service) ar trebui să aibă următoarele metode:
• create_default_circle(radius) - creează și returnează un obiect de tip Cerc (Circle) cu proprietăți pentru culori
   preluate din valorile implicite.
• create_default_rectangle(width, length) - creează și returnează un obiect de tip Dreptunghi (Rectangle) cu proprietăți
   pentru culori preluate din valorile implicite.
• create_default_square(side_length) - creează și returnează un obiect de tip Pătrat (Square) cu proprietăți pentru
   culori preluate din valorile implicite.
• color_shapes(list_of_shapes, inner_color, border_color) - setează culorile tuturor formelor din lista de forme la
   culorile specificate ca argumente.

"""
# Solutie

from home_work_21.ex_1_1 import Circle, Rectangle, Square, Shape


class ShapeService:
    DEFAULT_INNER_COLOR = "default_inner"
    DEFAULT_BORDER_COLOR = "default_border"

    @staticmethod
    def create_default_circle(radius: float) -> Circle:
        return Circle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, radius)

    @staticmethod
    def create_default_rectangle(width: float, length: float) -> Rectangle:
        return Rectangle(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, width, length)

    @staticmethod
    def create_default_square(side_length: float) -> Square:
        return Square(ShapeService.DEFAULT_INNER_COLOR, ShapeService.DEFAULT_BORDER_COLOR, side_length)

    @staticmethod
    def color_shapes(list_of_shapes: list[Shape], inner_color: str, border_color: str) -> None:
        for shape in list_of_shapes:
            if isinstance(shape, Shape):
                shape.set_inner_color(inner_color)
                shape.set_border_color(border_color)


# Verificare
# Presupunem ca avem o Circle class definita cu atributele private _inner_color and _border_color

# Pasul 1: Instantierea obiectelor
circle = ShapeService.create_default_circle(5.0)
rectangle = ShapeService.create_default_rectangle(3.0, 4.0)
square = ShapeService.create_default_square(6.0)

# Pasul 2: Crearea instantelor
shapes_list = [circle, rectangle, square]

# Pasul 3: Chemarea metodei color_shapes
ShapeService.color_shapes(shapes_list, "red", "blue")

# Pasul 4: Verificarea rezultatelor
for shape in shapes_list:
    print(f"Shape: {shape.__class__.__name__}")
    print(f"Inner Color: {shape._inner_color}")
    print(f"Border Color: {shape._border_color}")
    print("------------------")
