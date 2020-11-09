import screen
import front
import config

from config import preciosE, numEntradas, entradasQ

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

def main():
    front.printScreen()

    edad = front.pedirEdad()
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

        edad = front.pedirEdad()

    screen.locate(11, 1)

main()