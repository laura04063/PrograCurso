#2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person:
    def __init__(self, name):
        self.name = name  

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers 

    def añadir_pasajeros(self, person, passengers):
        if len(passengers) < self.max_passengers:
            passengers.append(person) 
            print(person.name + " ingreso al bus.")
        else:
            print(person.name + " el bus está lleno, no se puede subir más pasajeros.")

    def bajar_pasajeros(self, passengers):
        if passengers:  
            person = passengers.pop(0)  
            print(person.name + " bajó del bus.")
        else:
            print("No hay pasajeros en el bus para bajar.")

bus = Bus(2)  
passengers = [] 

p1 = Person("Mikel")
p2 = Person("María")
p3 = Person("Sofia")

bus.añadir_pasajeros(p1, passengers) 
bus.añadir_pasajeros(p2, passengers)  
bus.añadir_pasajeros(p3, passengers)  

bus.bajar_pasajeros(passengers)  
bus.bajar_pasajeros(passengers)