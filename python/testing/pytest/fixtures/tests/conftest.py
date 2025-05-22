import pytest
import src.shapes as shapes

# Fixtures
# objetos globales instanciados para testeo

# conftest.py: es llamado el archivo que 
# contenga todos los fixtures para esta suite de testeos
# YA NO ES NECESARIO IMPORTARLO

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10,20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)
