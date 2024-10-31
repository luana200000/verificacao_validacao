import unittest

# Função para calcular a média de três notas
def calcular_media(*notas):
    media = sum(notas) / len(notas)
    return media

class TestCalcularMedia(unittest.TestCase):
    
    def test_media_basica(self):
        self.assertEqual(calcular_media(8.0, 7.0, 9.0), 8.0)
    
    def test_todas_notas_zero(self):
        self.assertEqual(calcular_media(0.0, 0.0, 0.0), 0.0)
    
    def test_notas_maximas(self):
        self.assertEqual(calcular_media(10.0, 10.0, 10.0), 10.0)
    
    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(8.5, 7.2, 9.8), 8.5, places=1)

if __name__ == '__main__':
    unittest.main()

