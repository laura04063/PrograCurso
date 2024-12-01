# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def primera_funcion():
    print ("mi nombre completo es Maria Laura")

def segunda_funcion():
    primera_funcion()
    print ("tengo 18 años")

segunda_funcion()