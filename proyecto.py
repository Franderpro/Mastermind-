import random

print("Bienvenido, por favor ingresa tu nombre")
jugador1 = input("Ingresa tu nombre: ")
print(f"Buenas {jugador1}")
print("Espero estés listo para poner a prueba tus habilidades de deducción")

class JuegoMastermind:
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
            elif conjetura[i] in self.__combinacion_secreta:
                resultado.append(f"🟠")
                print(f"🟠 {conjetura[i]} está en la combinación pero en la posición incorrecta")
            else:
                resultado.append(f"⚪")
                print(f"⚪ {conjetura[i]} no está en la combinación")

        print(f"Conjetura: [{', '.join(conjetura)}]")
        print(f"Resultado: [{', '.join(resultado)}]")
        return resultado


juego = JuegoMastermind(jugador1)

print(f"Jugador: {juego.jugador1}")
print("Colores disponibles: ", juego.colores_disponibles)
print("Intenta adivinar la combinación de 4 colores. Ejemplo de entrada: rojo, azul, verde, amarillo")

intentos = 0
max_intentos = 12
while intentos < max_intentos:
    conjetura = input("Ingresa tu conjetura separando los colores por comas: ").strip().lower().split(", ")
    intentos += 1
    resultado = juego.verificar_conjetura(conjetura)
    
    if resultado and all(item == "🟢" for item in resultado) and len(resultado) == 4:
        print(f"¡Felicidades {juego.jugador1}! Adivinaste la combinación en {intentos} intentos.")
        break
else:
    print(f"Lo siento {juego.jugador1}, has agotado tus {max_intentos} intentos. Mejor suerte la próxima vez.")

print("Combinación secreta de la máquina (solo para prueba): ", juego.combinacion_secreta)
