import matplotlib.pyplot as plt  
minimo=1
maximo=10000
def collatz(n):
    """Calcula la cantidad de iteraciones para que n converja a 1"""
    iteraciones = 0  
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1   
        iteraciones += 1    
    return iteraciones


numeros = []      #
iteraciones = [] 


for n in range(minimo,maximo+1):
    numeros.append(n)
    iteraciones.append(collatz(n))



plt.plot(iteraciones, numeros)


plt.xlabel("Número de iteraciones")  
plt.ylabel("Número n de inicio")     
plt.title("Conjetura de Collatz para números entre 1 y 10000")

plt.grid(True) 
plt.show()  # Mostramos el gráfico
