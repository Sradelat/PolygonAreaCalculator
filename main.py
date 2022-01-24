# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(7)
rect.set_width(4)
print(rect.get_amount_inside(sq))  # rect 8, 16 sq 4

# rect = shape_calculator.Rectangle(5, 10)
# print(rect.get_area())
# rect.set_width(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_diagonal())  # ((width ** 2 + height ** 2) ** .5)
# # print(rect.get_picture())
#
# sq = shape_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print("Rect: " + str(rect.get_diagonal()))
# print("Sq: " + str(sq.get_diagonal()))



# Run unit tests automatically
# main(module='test_module', exit=False)