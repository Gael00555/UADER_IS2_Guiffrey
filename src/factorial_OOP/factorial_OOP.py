
import sys  


class Factorial:
    
    def __init__(self):
        pass  

    
    def calcular(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1  
        else:
            fact = 1  
            while num > 1:
                fact *= num  
                num -= 1     
            return fact

    def run(self, min, max):
        
        for n in range(min, max + 1):
            print("Factorial ", n, "! es ", self.calcular(n))

f = Factorial()

if len(sys.argv) < 2:
    rango = input("Ingrese un número o rango (ej: 5 o 4-8 o -10 o 5-): ")
else:
    rango = sys.argv[1]  


if '-' in rango:
    partes = rango.split('-')  

    if partes[0] == '':
    
        desde = 1
        hasta = int(partes[1])
    elif partes[1] == '':
        
        desde = int(partes[0])  
        hasta = 60
    else:
        # rango completo
        desde = int(partes[0])  
        hasta = int(partes[1]) 
else:
    # Si no hay guion, es un número solo
    desde = hasta = int(rango)  # Convertimos a entero


f.run(desde, hasta)
