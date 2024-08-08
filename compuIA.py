import itertools

class JuegoMastermindCompuIA:
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
        return resultado, correcto_color_posicion

    def feedback(self, guess, solution):
        black = sum(g == s for g, s in zip(guess, solution))
        white = sum(min(guess.count(j), solution.count(j)) for j in set(guess)) - black
        return black, white

    def adivinar_combinacion(self):
        colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']
        posibilidades = list(itertools.product(colores, repeat=4))
        conjetura = ['rojo', 'rojo', 'azul', 'azul']
        intentos = 0

        while True:
            intentos += 1
            resultado, correctos = self.verificar_conjetura(conjetura)
            if correctos == 4:
                print(f"\n¡La computadora adivinó la combinación secreta en {intentos} intentos!")
                print(f"Combinación secreta: {self.__combinacion_secreta}")
                break
            feedback_result = self.feedback(conjetura, self.__combinacion_secreta)
            posibilidades = [p for p in posibilidades if self.feedback(conjetura, p) == feedback_result]
            if posibilidades:
                conjetura = list(posibilidades[0])
            else:
                break
