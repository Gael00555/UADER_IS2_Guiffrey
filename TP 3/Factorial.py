# Ejericio 1
import math

class Factorial(object):
    _instance = None

    def __init__(self):
        print('Inicializa el objeto')

    def __new__(cls):
        if cls._instance is None:
            print('Creando el objeto')
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        return math.factorial(n)

f1 = Factorial()
print(f1, f1.calcular(5))

f2 = Factorial()
print(f2, f2.calcular(7))

print("¿Misma instancia?", f1 is f2)