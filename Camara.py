class Camara:
    def __init__(self, id, ubicacion, ip, estado):
        self.id = id
        self.ubicacion = ubicacion
        self.ip = ip
        self.estado = estado

    def grabar(self):
        print(f"Camara {self.id} grabando en {self.ubicacion}. Estado: {self.estado}")
