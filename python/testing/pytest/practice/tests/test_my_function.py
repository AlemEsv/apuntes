import pytest
# importa MODULOS no carpetas
from src.my_function import calculadora

def test_add():
    # Arrange y Act
    result = calculadora.add(1,4)

    # Assert
    assert result == 5

# concatena strings
def test_add_strings():
    # Arrange y Act
    result = calculadora.add("Me gustan ", "las hamburguesas")

    # Assert
    assert result == "Me gustan las hamburguesas"

def test_divide():
    # Arrange y Act
    result = calculadora.divide(4,2)

    # Assert
    assert result == 2

def test_divide_by_zero():
    # Assert
    # pytest.raises captura excepciones, generalmente ValueErrors
    with pytest.raises(ValueError):
        # Arrange y Act
        result = calculadora.divide(3,0)