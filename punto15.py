import math

def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if a == 0:
        print ("NO puede ser 0") 
    
    elif discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("Las raíces son:", raiz1, " y ", raiz2)

    elif discriminante == 0:
        raiz = -b / (2*a)
        print("La raíz doble es:", raiz)
    else:
        print("No hay raíces reales")

# Ejemplo de uso
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

ecuacion_cuadratica(a, b, c)