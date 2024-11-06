#leer registro 
Name = input("Digite su numbre: ")
Age = int (input("Digigte su edad: "))
Sex = input("Digite su sexo (H para Hombre, M para mujer): ").upper()
Civil = input("Digite su estado civil (S para soltero, C para comprometido, CA para casado): ").upper()

#imprimir con condiciones 
if Sex == "H" and Civil == "CA" and Age > 40:
    print("Nombre: ",Name)
elif Sex == "M" and Civil == "S" and Age < 50:
    print("Nombre: ",Name)
else:
    print("No cumples con los requisitos")
