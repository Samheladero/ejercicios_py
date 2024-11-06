#leer un numero e imprimir su equivalente en positivo
Num = float(input("Digite un numero: "))

if Num < 0:
    print("su numero negativo es: ",Num)
    print("su numero positivo es: ",-Num)
else:
    print("su numero es positivo o cero: ",Num)