#4. Cree las siguientes clases:
#    1. `Head`
#    2. `Torso`
#    3. `Arm`
#    4. `Hand`
#    5. `Leg`
#    6. `Feet`
#    7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.

class Cabeza:
    def __init__(self, color_cabello, color_ojos):
        self.color_cabello = color_cabello  
        self.color_ojos = color_ojos 

class Mano:
    def __init__(self, tamañoMano):
        self.tamañoMano = tamañoMano  

class Brazo:
    def __init__(self, largoBrazo):
        self.largoBrazo = largoBrazo 

class Torso:
    def __init__(self, cabeza, brazo_derecho, brazo_izquierdo):
        self.cabeza = cabeza  
        self.brazo_derecho = brazo_derecho  
        self.brazo_izquierdo = brazo_izquierdo 

class Pierna:
    def __init__(self, largoPierna):
        self.largoPierna = largoPierna

class Pie:
    def __init__(self, tamañoPie):
        self.tamañoPie = tamañoPie  

class Humano:
    def __init__(self, color_cabello, color_ojos, tamañoMano, largoBrazo, largoPierna, tamañoPie):
        self.cabeza = Cabeza(color_cabello, color_ojos)
        self.mano_derecha = Mano(tamañoMano)
        self.mano_izquierda = Mano(tamañoMano)
        self.brazo_derecho = Brazo(largoBrazo)
        self.brazo_izquierdo = Brazo(largoBrazo)
        self.torso = Torso(self.cabeza, self.brazo_derecho, self.brazo_izquierdo)
        self.pierna_derecha = Pierna(largoPierna)
        self.pierna_izquierda = Pierna(largoPierna)
        self.pie_derecho = Pie(tamañoPie)
        self.pie_izquierdo = Pie(tamañoPie)

    def describir(self):
        print("Cabeza: \nColor de Cabello = ", self.cabeza.color_cabello, ",\nColor de Ojos = ", self.cabeza.color_ojos)
        print("Brazos: \nTamaño Mano Izquierda = ", self.mano_izquierda.tamañoMano, ",\nTamaño Mano Derecha = ", self.mano_derecha.tamañoMano)
        print("Torso: \nContiene Cabeza, Brazo Derecho, Brazo Izquierdo")
        print("Piernas: \nLargo Pierna Izquierda = ", self.pierna_izquierda.largoPierna, ", \nLargo Pierna Derecha = ", self.pierna_derecha.largoPierna)
        print("Pies: \nTamaño Pie Izquierdo = ", self.pie_izquierdo.tamañoPie, ", \nTamaño Pie Derecho = ", self.pie_derecho.tamañoPie)


humano = Humano("Castaño", "Verde", 15, 65, 75, 35)
humano.describir()
humano1 = Humano("Rubio", "Azules", 15, 65, 75, 35)
humano1.describir()
humano1 = Humano("Pelirrojo", "Verde", 15, 65, 75, 35)
humano1.describir()
humano2 = Humano("Azul", "Azules", 15, 65, 75, 35)
humano2.describir()