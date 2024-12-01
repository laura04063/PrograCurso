numero_secreto= 4

while(True):
    print ("Adivina cual es el numero secreto del 1 al 10")
    numero= int(input("Ingrese un numero: "))
    if numero == numero_secreto:
        print ("Adivinaste el numero")
        break 
    else:
        print ("Numero incorrecto, continua intentando")