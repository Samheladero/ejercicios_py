num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

# Verificar divisibilidad
if (num1 % num2 == 0):
    print(num1,"es divisible por",num2)
elif (num1 % num3 == 0):
    print(num1,"es divisible por",num3)
elif (num2 % num1 == 0):
    print(num2,"es divisible por",num1)
elif (num2 % num3 == 0):
    print(num2,"es divisible por",num3)
elif (num3 % num1 == 0):
    print(num3,"es divisible por",num1)
elif (num3 % num2 == 0):
    print(num3,"es divisible por",num2)
else:
    print("Ningún número es divisible por otro.")