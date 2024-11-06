""" #solicitar 3 numero para encontrar el medio  
Num1 = int(input("Digite el primer numero unico: "))
Num2 = int(input("Digite el segundo numero unico: "))
Num3 = int(input("Digite el tercer numero unico: "))

#verificar si hay numeros que no son unicos 
if Num1 == Num2 or Num1 == Num3 or Num2 == Num3:
    print("Error: Hay numero que no son unicos")
#mostrar el numero medio 
else:
    NumMenor = min(Num1, Num2, Num3)
    NumMayor = max(Num1, Num2, Num3)
    ValorMedio = (Num1 + Num2 + Num3) - NumMenor - NumMayor
    print("El numero medio es: ",ValorMedio) """

#solicitar 3 numeros para encontrar el numero medio 
a = float(input("Digite el primer numero unico: "))
b= float(input("Digite el segundo numero unico: "))
c = float(input("Digite el tercer numero unico: "))

#verificar si hay numeros que no son unicos 
if a == b or a == c or b == c: 
    print ("Hay numero que no son unicos")
    
else:
    if a > b and a < c or a < b and a > c:
        print("El numero medio es: ",a)
    elif b > a and b < c or b < a and b > c:
        print("El numero medio es: ",b)
    else:
        print("El numero medio es: ",c)
    