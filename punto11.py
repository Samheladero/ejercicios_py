#aceptar o rechazar varilla 
Longitud = float(input("Digite la longitud: "))
Diametro = float(input("Digite el diametro: "))
Densidad = 3.5
Masa = Diametro * Longitud / Densidad

if Longitud <= 7.5 or Longitud > 9:
    print ("No cumple con la longitud establecida")
elif Diametro < 0.5 or Diametro > 1.3:
    print ("No cumple con el diametro")
elif Masa > 5.8:
    print ("No cumple con la masa")
else: 
    print ("Cumple con todos los estandares")
