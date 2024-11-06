#solicitar 3 numero para calcular
Num1 = float(input("Digite el primer numero: "))
Num2 = float(input("Digite el segundo numero: "))
Num3 = float(input("Digite el tercer numero: "))

#encontrar el numero mayor y el menor
Mayor = max(Num1, Num2, Num3)
Menor = min(Num1, Num2, Num3)

print("El numero mayor es: ",Mayor)
print("El numero menor es: ",Menor)

#verificar si son iguales o diferentes 
if Num1 == Num2 == Num3:
    print("Los numeros son iguales.")
elif Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print("Hay numero iguales.")
    if Num1 == Num2:
        print("Los numeros iguales son: ",Num1, "y", Num2)
    elif Num2 == Num3:
        print("Los numero iguales son: ",Num2, "y", Num3)
    elif Num1 == Num3:
        print("Los numeros iguales son: ",Num1, "y", Num3)
else:
    print("No hay numero iguales.")
