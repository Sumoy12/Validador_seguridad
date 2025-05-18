import unittest
from validador_seguridad_app import validar_texto

class TestValidador(unittest.TestCase):
    def test_validacion(self):
        lista = ['contraseña', 'clave', 'admin']
        self.assertEqual(validar_texto("La contraseña fue cambiada", lista), ['contraseña'])
        self.assertEqual(validar_texto("Texto sin riesgo", lista), [])
        self.assertIn('admin', validar_texto("Usuario admin ingresó", lista))

if __name__ == '__main__':
    unittest.main()
