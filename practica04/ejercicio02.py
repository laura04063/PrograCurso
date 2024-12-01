nombre= input ("Ingrese su nombre: ")
apellido= input ("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))

if edad <= 2:
    print(f"{nombre} {apellido} eres un bebe" )
elif (edad <=10):
    print(f"{nombre} {apellido} eres un niño" )
elif (edad <=14):
    print(f"{nombre} {apellido} eres un preadolescente" )
elif (edad <= 18):
    print(f"{nombre} {apellido} eres un adolescente" )
elif (edad <= 25):
    print(f"{nombre} {apellido} eres un adulto joven" )
elif (edad <= 60):
    print(f"{nombre} {apellido} eres un adulto" )
else:
    print(f"{nombre} {apellido} eres un adulto mayor" )