# Solicitar las tres notas del estudiante
note1 = float(input("Introduce la primera nota de 1-100: "))
note2 = float(input("Introduce la segunda nota 1-100: "))
note3 = float(input("Introduce la tercera nota 1-100: "))

# Calcular la nota total (promedio de las 3 notas)
promedio = (note1 + note2 + note3) / 3
final = round(promedio, 1)

# Determinar si el estudiante aprobó o reprobó
if final >= 60:
    print("Has aprobado la materia con una nota de: ", final)
else:
    print("Has reprobado la materia con una nota de: ",final)