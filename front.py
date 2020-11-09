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