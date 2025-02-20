class Student():
    def __init__(self, nombre, seccion, notas):
        self.nombre = nombre
        self.seccion = seccion
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas.values()) / len(self.notas)

    def convertirDiccionario(self):
        return {
            "Nombre": self.nombre,
            "Sección": self.seccion,
            "Español": self.notas.get("Español", 0),
            "Inglés": self.notas.get("Inglés", 0),
            "Sociales": self.notas.get("Sociales", 0),
            "Ciencias": self.notas.get("Ciencias", 0)
        }

    def texto (self):
        notas_str = ""
        for materia, nota in self.notas.items():
            notas_str += f"{materia}: {nota}\n"
        return f"{self.nombre} (Sección {self.seccion})\n{notas_str}"