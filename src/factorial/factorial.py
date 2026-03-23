
import sys


def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    
    elif num == 0: 
        return 1
    else: 
        fact = 1  
        
        while(num > 1): 
            fact *= num  
            num -= 1     
        return fact      

# Si no se pasó ningún argumento, se le pide al usuario que ingrese uno
if len(sys.argv) < 2:
    rango = input("Ingrese un número o rango (ej: 5 o 4-8 o -10 o 5-): ")
else:
    rango = sys.argv[1]  # Tomamos el argumento de la línea de comandos

# Analizamos el argumento para determinar el rango
if '-' in rango:
    partes = rango.split('-')  # Separamos por el guion
    
    if partes[0] == '':
        # no tiene límite inferior, se calcula desde 1
        desde = 1
        hasta = int(partes[1])  
    elif partes[1] == '':
        # no tiene límite superior, se calcula hasta 60
        desde = int(partes[0])
        hasta = 60
    else:
        # rango completo
        desde = int(partes[0])  
        hasta = int(partes[1]) 
else:

    desde = hasta = int(rango)  


for n in range(desde, hasta + 1):
    print("Factorial ", n, "! es ", factorial(n))
