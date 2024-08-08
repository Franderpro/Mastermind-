import random

class JuegoMastermindI:
    def __init__(self, jugador1: str) -> None:
        self.__colores_disponibles = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']
        self.__combinacion_secreta = [random.choice(self.__colores_disponibles) for _ in range(4)]
        self.__jugador1 = jugador1

    @property
    def colores_disponibles(self):
        return self.__colores_disponibles

    @property
    def combinacion_secreta(self):
        return self.__combinacion_secreta

    @property
    def jugador1(self):
        return self.__jugador1

    def verificar_conjetura(self, conjetura):
        if len(conjetura) != 4:
            print("La conjetura debe contener 4 colores.")
            return []

        resultado = []
        correcto_color_posicion = 0

        for i in range(4):
            if conjetura[i] == self.__combinacion_secreta[i]:
                resultado.append(f"🟢")
                print(f"🟢 {conjetura[i]} está en la posición correcta")
                correcto_color_posicion += 1
            else:
                resultado.append(f"⚪")
                print(f"⚪ {conjetura[i]} no está en la combinacion o no esta en la posicion correcta")

        print(f"Conjetura: [{', '.join(conjetura)}]")
        print(f"Resultado: [{', '.join(resultado)}]")
        return resultado
