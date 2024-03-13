from Usuario import Usuario

class Guardia(Usuario):
    def __init__(self, correo, matricula, nombre, zona, horario):
        super().__init__(correo, matricula, nombre)
        self.zona = zona
        self.horario = horario

    def apagarAlarmas(self):
        print("Apagando alarmas...")

    def capacitacion(self):
        print("Recibiendo capacitación...")
