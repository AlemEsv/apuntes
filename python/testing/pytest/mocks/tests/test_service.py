# MOCKS: TESTING DE SERVICIOS

import pytest
import src.service as service
import unittest.mock as mock

# Instancia de un mock para 
# simular el método get_user definido en service
@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db():
    
    pass