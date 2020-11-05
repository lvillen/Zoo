import screen

preciosE = {
    'bebe': 0.0,
    'niño': 14.0,
    'adulto': 23.0,
    'jubilado': 18.0
    }

totales = {'bebe':0, 'niño':0, 'adulto':0, 'jubilado':0}

entradasQ = {
    'bebe': {
        'cantidad': (4,15),
        'precioA': (4,19),
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
    screen.locate(1,1)
    edad = input("¿Qué edad tienes? ")
    while validaEdad(edad) == False:
        print("Edad incorrecta, vuelva a intentarlo")
        screen.locate(1,1)
        edad = input("¿Qué edad tienes? ")
        
    return int(edad)

def printScreen():
    screen.locate(5, 5)
    print("Bebé....:   -")
    screen.locate(6, 5)
    print("Niño....:   -")
    screen.locate(7, 5)
    print("Adulto..:   -")
    screen.locate(8, 5)
    print("Jubilado:   -")
    
    screen.locate(10,8)
    print("Total...: ")
    
    
screen.clear()
printScreen()

edad = pedirEdad()
precioTotal = 0 #Negocio

while edad != 0:
    tipoE = tipoEntrada(edad)
    precioE = preciosE[tipoE]
    screen.locate(entradasQ[tipoE]['cantidad'][0], entradasQ[tipo]['cantidad'][1])
    print(1)
    screen.locate(entradasQ[tipoE]['precioA'][0], entradasQ[tipoE]['precioA'][1])
    print("{:7.2f}€".format(precioE))
    precioTotal += precioE
    
    edad = pedirEdad()

screen.locate(linea, 12)
print("Total: {:7.2f} €".format(precioTotal))

print("Lo que sea...")