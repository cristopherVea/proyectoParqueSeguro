class Usuario:
    def __init__(self, correo, matricula, nombre):
        self.correo = correo
        self.matricula = matricula
        self.nombre = nombre

    def recibirAlarma(self):
        print(f"{self.nombre} ha recibido una alarma")

    def verVideos(self):
        print(f"{self.nombre} está viendo los videos")
