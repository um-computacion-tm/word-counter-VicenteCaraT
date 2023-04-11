import unittest


from Contador_palabras import count_words

class TestCountWords (unittest.TestCase):
    
    def test_1(self):
        resultado = count_words('hola mundo')
        self.assertEqual (resultado, {'hola':1, 'mundo':1})
    
    def test_2(self):
        resultado = count_words('hola hola mundo palabras MUNDO PALABRAS perro gato')
        self.assertEqual (resultado, {'hola':2, 'mundo':2, 'palabras':1, 'palabras':2, 'perro':1, 'gato':1})



if __name__ == '__main__':
    unittest.main()