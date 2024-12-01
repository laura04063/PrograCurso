#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    #1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def numero_mayusculas(letras):
    mayusculas = 0
    for  letra in letras:
        if "A" <= letra <= "Z":
            mayusculas += 1
    print ("letras mayuculas: ", mayusculas)


def numero_minusculas(letras):
    minusculas = 0  
    for  letra in letras:
        if "a" <= letra <= "z":
            minusculas += 1
    print ("letras minusculas: ", minusculas)
frase1= "I love Nación Sushi"
frase2= "There’s 3 upper cases and 13 lower cases"
numero_mayusculas(frase1)
numero_minusculas(frase1)
numero_mayusculas(frase2)
numero_minusculas(frase2)