import unittest
import math

def suma(nro1,nro2):
    return nro1 + nro2

def resta(nro1,nro2):
    return nro1 - nro2

def multiplicacion(nro1,nro2):
    return nro1 * nro2

def division(nro1,nro2):
    return nro1 / nro2

def tangente(nro1):
    return math.tan(math.radians(nro1))

def fact(nro1):
    return math.factorial(nro1)

def potencia(nro1,nro2):
    return math.pow(nro1,nro2)
def raiz(nro1,nro2):
    return math.pow(nro1,1/nro2)

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        esperado = 12
        actual = suma(7,5)
        self.assertEqual(actual,esperado)
    
    def test_resta(self):
        esperado = 5
        actual = resta(10,5)
        self.assertEqual(actual,esperado)

    def test_multiplicacion(self):
        esperado = 50
        actual = multiplicacion(10,5)
        self.assertEqual(actual,esperado)
    
    def test_division(self):
        esperado = 2
        actual = division(20,10)
        self.assertEqual(actual,esperado)
    
    def test_tangente(self):
        esperado = 0.9999999999999999
        actual = tangente(45)
        self.assertEqual(actual,esperado)
    
    def test_factorial(self):
        esperado = 24
        actual = fact(4)
        self.assertEqual(actual,esperado)
    
    def test_potencia(self):
        esperado = 9
        actual = potencia(3,2)
        self.assertEqual(actual,esperado)
    
    def test_raiz(self):
        esperado = 5
        actual = raiz(125,3)
        self.assertEqual(actual,esperado)

    def tearDown(self):
        #Aqui va lo contrario cuando el test ha terminado
        pass
#LLamar al modulo principal para ejecutar las pruebas unitarias

if __name__== '__main__':
    unittest.main()

#Agregar tangente , factorial , potencia, raiz nsima