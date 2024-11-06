# Solicitar un número al usuario
numero = float(input("Introduce un número: "))

# Verificar si el número es positivo o negativo
if numero > 0:
    print(numero,"es un número positivo.")
elif numero < 0:
    print(numero,"es un número negativo.")
else:
    print("El número es cero.")
