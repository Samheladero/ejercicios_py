#solicitar un valor para realizar acciones si es int o float 
Valor = input("Digite un numero: ")

#intentar convertir en entero 
try:
    NumInt = int(Valor)
    Kelvin = NumInt + 273.15
    print (NumInt,"°C son ",Kelvin,"K")
except:
    #si no convierte en entero convertir en flotante 
    try:
        NumFloat = float(Valor)
        if NumFloat > 10.5:
            print("El numero es mayor a 10.5")
        else:
            print("El numero no es mayor a 10.5")
    except: 
        #si no convierte en flotante asumir que es un caracter
        print("El caracter ingresado es: ",Valor)