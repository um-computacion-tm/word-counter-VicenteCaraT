import unittest 


def count_words(words):
    for i in words:


class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})
    def test_st1(self):
        result = count_words ('hola como estas')
        self.assertEqual(result, {'hola' 'como' 'estas': 3})
    def test_st2(self):
        result = count_words ('que pasa internautas de la galaxia')
        self. assertEqual (result, {'que' 'pasa' 'internautas' 'de' 'la' 'galaxia':6})




if __name__ == '__main__':
    unittest.main()