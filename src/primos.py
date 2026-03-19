#!/usr/bin/python3
# Programa para mostrar todos los números primos en un intervalo dado

# Definición del intervalo de búsqueda
lower = 1  # Límite inferior del intervalo
upper = 500  # Límite superior del intervalo

print("Prime numbers between", lower, "and", upper, "are:")

# Iteramos sobre todos los números en el intervalo
for num in range(lower, upper + 1):
   # Los números primos son mayores que 1
   if num > 1:
       # Verificamos si el número es divisible por algún número menor a él
       for i in range(2, num):
           if (num % i) == 0:
               break  # Si es divisible, no es primo
       else:
           print(num)  # Si no fue divisible por ninguno, es primo
