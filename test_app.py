import unittest
from validador_seguridad_app import validar_texto

class TestValidador(unittest.TestCase):
    """Pruebas unitarias para la función validar_texto."""

    def test_validacion(self):
        """Verifica que se detecten correctamente las palabras de riesgo presentes en el texto."""
        lista = ['contraseña', 'clave', 'admin']
        self.assertEqual(validar_texto("La contraseña fue cambiada", lista), ['contraseña'])
        self.assertEqual(validar_texto("Texto sin riesgo", lista), [])
        self.assertIn('admin', validar_texto("Usuario admin ingresó", lista))

    def test_multiples_palabras(self):
        """Verifica que se detecten múltiples palabras de riesgo presentes en una sola entrada."""
        lista = ['clave', 'segura']
        resultado = validar_texto("La clave segura fue aceptada", lista)
        self.assertEqual(set(resultado), {'clave', 'segura'})

    def test_mayusculas_y_minusculas(self):
        """Valida que la detección sea insensible a mayúsculas/minúsculas."""
        lista = ['peligro', 'riesgo']
        resultado = validar_texto("Hay un PELIGRO inminente y alto RIESGO", lista)
        self.assertEqual(set(resultado), {'peligro', 'riesgo'})

    def test_palabras_parciales_no_detectadas(self):
        """Verifica que palabras de riesgo no se detecten dentro de otras palabras más largas (si se desea comportamiento exacto)."""
        lista = ['admin']
        resultado = validar_texto("El administrador general", lista)
        self.assertNotIn('admin', resultado)  # Este test depende de si quieres coincidencias exactas o parciales

if __name__ == '__main__':
    unittest.main()
