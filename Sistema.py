from AnalizadorIA import AnalizadorIA
from Administrador import Administrador
from Guardia import Guardia

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.analizador = AnalizadorIA("Modelo XYZ")

    def registrarCasos(self):
        print("Registrando casos...")

    def crearUsuarios(self, tipo, **kwargs):
        if tipo == "administrador":
            self.usuarios.append(Administrador(**kwargs))
        elif tipo == "guardia":
            self.usuarios.append(Guardia(**kwargs))
        else:
            print("Tipo de usuario no reconocido")

    def configuracion(self):
        print("Configurando sistema...")
