# solicitar notas del etudiante 
nota1 = float(input("Digite nota #1: "))
nota2 = float(input("Digite nota #2: "))
nota3 = float(input("Digite nota #3: "))

if nota1 >= nota2 and nota1 >= nota3:
    # nota1 es la más alta
    if nota2 >= nota3:
        promedio = (nota1 + nota2) / 2
    else:
        promedio = (nota1 + nota3) / 2
elif nota2 >= nota1 and nota2 >= nota3:
    # nota2 es la más alta
    if nota1 >= nota3:
        promedio = (nota2 + nota1) / 2
    else:
        promedio = (nota2 + nota3) / 2
else:
    # nota3 es la más alta
    if nota1 >= nota2:
        promedio = (nota3 + nota1) / 2
    else:
        promedio = (nota3 + nota2) / 2

# Mostrar el resultado
print("La nota final es: ",promedio)