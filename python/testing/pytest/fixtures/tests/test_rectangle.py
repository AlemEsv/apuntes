import pytest


def test_area(my_rectangle):
    # llamada a un rectangulo
    # rectangle = shapes.Rectangle(10,20)

    assert my_rectangle.area() == 200

def test_perimeter(my_rectangle):
    # llamada a un rectangulo, redundante
    # Es mejor hacer un fixture
    # rectangle = shapes.Rectangle(10,20)

    assert my_rectangle.perimeter() == 60

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle