import time
import pytest
# importa MODULOS no carpetas
from src.my_function import calculadora

# MARCADORES PARA TESTS

# test marcado como lento
# arrojará un aviso al correr el test
#@pytest.mark.slow
def test_very_slow():
    time.sleep(2) # en segundos
    result = calculadora.divide(10,5)
    assert result == 2

# skipeará el test
@pytest.mark.skip(reason="feature broken")
def test_divide():
    assert calculadora.divide(4,4) == 3 

# marca al test como erroneo
@pytest.mark.xfail(reason="not working")
def test_divide_zero():
    assert calculadora.divide(4,0) == 4
    