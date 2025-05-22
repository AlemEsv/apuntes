import pytest
import src.my_function as shapes

# probar con parametros generales
@pytest.mark.parametrize("side_length, expected_area", 
                         [(5,25),
                          (4,16),
                          (9,81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area