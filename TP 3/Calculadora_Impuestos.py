#Ejercicio 2

class Impuestos(object):
    _instance = None

    def __init__(self):
        print('Inicializa el objeto')

    def __new__(cls):
        if cls._instance is None:
            print('Creando el objeto')
            cls._instance = super(Impuestos, cls).__new__(cls)
        return cls._instance

    def calcular(self, base):
        iva = base * 0.21
        iibb = base * 0.05
        contrib = base * 0.012
        total = iva + iibb + contrib
        print(f"  IVA (21%):                ${iva:.2f}")
        print(f"  IIBB (5%):                ${iibb:.2f}")
        print(f"  Contrib. municipales (1.2%): ${contrib:.2f}")
        print(f"  Total impuestos:          ${total:.2f}")
        return total



i1 = Impuestos()
print(i1)
i1.calcular(1000)

i2 = Impuestos()
print(i2)
i2.calcular(5000)

print("¿Misma instancia?", i1 is i2)