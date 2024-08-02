import random
from abc import ABC
print("bienvenido, por favor ingresa tu nombre")
jugador1 = input("ingresa tu nombre: ")
print(f"buenas {jugador1}")
print("espero estes listo para poner a prueba tus habiidades de deducción")
class juego:
    def __init__(self, color:str,jugador2:str, jugador1:str) -> None:
        self.__color= colores_disponibles = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']
        self.__jugador2= [random.choice(colores_disponibles) for _ in range(4)]
        self.__jugador1=jugador1
    @property
    def color(self):
        return self.__color 
    @property
    def jugador2(self):
        return self.__jugador2
    @property
    def jugador1(self):
        return self.__jugador1
