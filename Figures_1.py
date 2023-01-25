from Rest_pol import Restangle, Square, Circle

r1 = Restangle(3, 4)
r2 = Restangle(12, 5)

sq1 = Square(4)
sq2 = Square(12.5)

c1 = Circle(3)
c2 = Circle(4)
figures = [r1, r2, sq1, sq2, c1, c2]
for figure in figures:
    if isinstance(figure, Restangle):
        print(figure.get_area())
    if isinstance(figure, Square):
        print(figure.get_area_square())
    if isinstance(figure, Circle):
        print(figure.get_circle_area())
