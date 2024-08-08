import random

class JuegoMastermindCompu:
    def __init__(self, jugador1: str) -> None:
        self.__colores_disponibles = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']
        self.__combinacion_secreta = []
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

    def establecer_combinacion_secreta(self, combinacion):
        if len(combinacion) != 4:
            print("La combinación debe contener 4 colores.")
            return False
        for color in combinacion:
            if color not in self.__colores_disponibles:
                print(f"Color {color} no está disponible.")
                return False
        self.__combinacion_secreta = combinacion
        return True

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
            elif conjetura[i] in self.__combinacion_secreta:
                resultado.append(f"🟠")
                print(f"🟠 {conjetura[i]} está en la combinación pero en la posición incorrecta")
            else:
                resultado.append(f"⚪")
                print(f"⚪ {conjetura[i]} no está en la combinación")

        print(f"Conjetura: [{', '.join(conjetura)}]")
        print(f"Resultado: [{', '.join(resultado)}]")
        return resultado

    def adivinar_combinacion(self):
        max_intentos=12
        intentos = 0
        conjetura = [random.choice(self.__colores_disponibles) for _ in range(4)]
        resultado = self.verificar_conjetura(conjetura)
        while intentos <= max_intentos:
            if resultado.count("🟢") != 4:
                
                conjetura = [random.choice(self.__colores_disponibles) for _ in range(4)]
                print(f"\nIntento {intentos}:")
                resultado = self.verificar_conjetura(conjetura)
                intentos += 1
                

            print(f"\n¡La computadora adivinó la combinación secreta en {intentos + 1} intentos!")
            print(f"Combinación secreta: {self.__combinacion_secreta}")


"""juego = JuegoMastermindCompu("Jugador 1")


combinacion_usuario = input("Ingrese la combinación secreta de 4 colores separados por comas (ej. rojo,verde,azul,amarillo): ").split(',')
combinacion_usuario = [color.strip() for color in combinacion_usuario]

if juego.establecer_combinacion_secreta(combinacion_usuario):
    juego.adivinar_combinacion()
else:
    print("Error al establecer la combinación secreta.")"""
