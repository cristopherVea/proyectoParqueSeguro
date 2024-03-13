from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, correo, matricula, nombre, rol):
        super().__init__(correo, matricula, nombre)
        self.rol = rol

    def verHistorial(self):
        print("Viendo historial...")

    def configurarAlarmas(self):
        print("Configurando alarmas...")

    def ponerNuevasReglas(self):
        print("Poniendo nuevas reglas...")
