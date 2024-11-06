#sueldo inferior a 300.000 se le agrega un 15%
Sueldo = float(input("Digite el monto de su salario: "))
Aumento = Sueldo * 0.15
Total = Sueldo + Aumento 

if Sueldo < 300000:
    print("Su sueldo aumento a: ",Total)
else:
    print("su sueldo no aumento")
