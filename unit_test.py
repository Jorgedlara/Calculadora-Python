import unittest

#Pruebas unitarias a la función "eval" usada para obtener el resultado en la calculadora

class test_calculadora(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(eval("5+5"), 10)

    def test_res(self):
        self.assertEqual(eval("25-20"), 5)

    def test_mult(self):
        self.assertEqual(eval("10*10"), 100)
    
    def test_div(self):
        self.assertEqual(eval("50/10"), 5)

    def test_jerarquia(self):
        self.assertEqual(eval("25*5-25"), 100)

    def test_sumres(self):
        self.assertEqual(eval("25-20+50"), 55)

if __name__ == "__main__":
    unittest.main()