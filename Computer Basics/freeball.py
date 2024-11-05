import numpy as np

print("This is a program to know the difference positions between consecutive time steps")
h = int(input("enter height: ")) #Para que metas el valor de la altura 
g = 9.8  #La gravedad
t= np.linspace(start=1, stop=100, num=100) #Para cambiar el tiempo


# Calculamos la diferencia de posicion entre cada paso de tiempo
y = h - (0.5 * g * t**2) #La ecuacion
print("Los resultados:")
print(y)