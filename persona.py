from datetime import date

from Jugador import jugador


class persona:
    fechaNac:date
    def __init__(self,nombre,nif,fechaNac):
        self.nombre=nombre
        self.nif=nif
        self.fechaNac=fechaNac

persona.jugador=jugador
