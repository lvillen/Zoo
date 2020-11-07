import screen

preciosE = {
    'bebe': 0.0,
    'niño': 14.0,
    'adulto': 23.0,
    'jubilado': 18.0
    }

numEntradas = {'bebe':0, 'niño':0, 'adulto':0, 'jubilado':0}

entradasQ = {
    'bebe': {
        'cantidad': (4,15),
        'precioA': (4,19)
        },
    'niño': {
        'cantidad': (5,15),
        'precioA': (5,19),
        },
    'adulto': {
        'cantidad': (6,15),
        'precioA': (6,19),
        },
    'jubilado': {
        'cantidad': (7,15),
        'precioA': (7,19),
        }
    }

def tipoEntrada(e):
    if e > 0 and e <=2:
        tipo = 'bebe'
    elif e <=12:
        tipo = 'niño'
    elif e < 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'
        
    return tipo

def validaEdad(cadena):
    try:
        n = int(cadena)
        if n>=0:
            #Entonces el valor es válido
            return True        
        return False
    except:
        return False

def pedirEdad():
    edad = screen.Input("¿Qué edad tienes? ", 1, 1)
    while validaEdad(edad) == False:
        screen.Format(0, 33, 41)
        screen.Print("Edad inválida", 25, 1, True)
        screen.Reset()
        edad = screen.Input("¿Qué edad tienes? ", 1, 1)
    
    screen.clearLine(25)
        
    return int(edad)

def printScreen():
    screen.clear()
    screen.Print("Bebé....:   -", 4, 5)
    screen.Print("Niño....:   -", 5, 5)
    screen.Print("Adulto..:   -", 6, 5)
    screen.Print("Jubilado:   -", 7, 5)

    screen.Format(1)
    screen.Print("Total...:   -", 9, 8)
    screen.Reset(0)
    
def main():
    printScreen()

    edad = pedirEdad()
    precioTotal = 0 #Negocio

    while edad != 0:
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        
        numEntradas[tipoE] += 1

        screen.Print(numEntradas[tipoE], entradasQ[tipoE]['cantidad'][0], entradasQ[tipoE]['cantidad'][1])
        screen.Print("{:7.2f}€".format(numEntradas[tipoE]*precioE), entradasQ[tipoE]['precioA'][0], entradasQ[tipoE]['precioA'][1])
       
        precioTotal += precioE
        screen.Format(1)
        screen.Print("{:7.2f} €".format(precioTotal), 9, 19)
        screen.Reset()

        edad = pedirEdad()

    screen.locate(11, 1)

main()