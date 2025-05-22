import requests
import unittest
from unittest.mock import patch, Mock

def get_user_data(user_id):
    response = requests.get(f"https://API.example.com/users/{user_id}")
    return response.json()

# ================ MOCKS ================================
# no se busca probar que la conexión a la API sea exitosa
# se busca probar que pasa ANTES de llamar al API/BD
# y DESPUES de llamarla.
# =======================================================

# Clase que usa Casos de uso para los tests
class TestUserData(unittest.TestCase):

    # patch: Crea un MOCK cada que se llame al metodo 'requests.get' 
    # y así no hacer un LLAMADO REAL a l API o a la DB
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        # instanciamos un mock que simule el objeto "response"
        mock_response = Mock()

        # diccionario con datos del usuario con ID: "user_id"
        response_dict = {'name': 'Alem', 'email': 'glu@gmail.com'}
        
        # Simulamos que la respuesta que nos dio la API después de la llamada
        # son los valores colocados en el diccionario "response_dict"
        mock_response.json.return_value = response_dict

        # el mock que creemos tendrá el retorno 
        # del mock que simula el retorno de la API
        mock_get.return_value = mock_response

        # creación de un usuario fake con la id=1
        # usando una llamada NO REAL 'request.get' gracis al patch
        user_data = get_user_data(3)

        # demostración de que el mock hace UNA UNICA llamada correcta
        mock_get.assert_called_with("https://API.example.com/users/1")
        self.assertEqual(user_data, response_dict)

if __name__ == '__main__':
    unittest.main()



