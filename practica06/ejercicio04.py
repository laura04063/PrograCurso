# Cree una función que le de la vuelta a un string y lo retorne.
    #1. Esto ya lo hicimos en iterables.
    #2. “Hola mundo” → “odnum aloH”

def vuelta_string():
    nombre = "Hola mundo"
    for string in reversed(nombre): 
        print (string)
        
vuelta_string()