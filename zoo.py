import screen

def calcularPrecioEntrada(e):
    if e > 0 and e <=2:
        precio = 0
    elif e <=12:
        precio = 14
    elif e < 65:
        precio = 23
    else:
        precio = 18
    return precio

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n>=0:
            return True        
        return False
    except:
        return False

def pedirEdad():
    screen.locate(1,1)
    edad = input("¿Qué edad tienes? ")
    while validaEdad(edad) == False:
        print("Edad incorrecta, vuelva a intentarlo")
        edad = input("¿Qué edad tienes? ")
    return int(edad)

screen.clear()
edad = pedirEdad()
precioTotal = 0
linea = 4

numEntradasB = 0
numEntradasN = 0
numEntradasA = 0
numEntradasJ = 0

while edad != 0:
    precioE = calcularPrecioEntrada(edad)
    if precioE == 0:
        linea = 4
        numEntradasB += 1
        screen.locate(linea, 1)
        print("Precio entrada: {} €\tNum. Entradas: {}".format(precioE, numEntradasB))
    if precioE == 14:
        linea = 5
        numEntradasN += 1
        screen.locate(linea, 1)
        print("Precio entrada: {} €\tNum. Entradas: {}".format(precioE, numEntradasN))
    if precioE == 23:
        linea = 6
        numEntradasA += 1
        screen.locate(linea, 1)
        print("Precio entrada: {} €\tNum. Entradas: {}".format(precioE, numEntradasA))
    if precioE == 18:
        linea = 7
        numEntradasJ += 1
        screen.locate(linea, 1)
        print("Precio entrada: {} €\tNum. Entradas: {}".format(precioE, numEntradasJ))
    linea += 1
    precioTotal += precioE
    
    edad = pedirEdad()

screen.locate(linea, 1)
print("Total: {} €".format(precioTotal))