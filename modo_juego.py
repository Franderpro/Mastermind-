from proyecto import JuegoMastermind
from compuIA import JuegoMastermindCompuIA
from Intermedio_jugador import JuegoMastermindI
from compu import JuegoMastermindCompu
from Dificil_jugador import JuegoMastermindD
from time import sleep

print("Bienvenido, por favor ingresa tu nombre")

jugador1 = input("Ingresa tu nombre: ")
print(f"Buenas {jugador1}, las reglas del juego son muy sencillas.")
sleep(2)
print("1. Habrá un total de 6 colores diferentes.")
sleep(2)
print("2. Hay dos modos de juego: uno donde tú debes adivinar el código de colores que decida el algoritmo, y otro donde la máquina deberá adivinar el código que tú elijas. Ambos tienen solo 12 intentos.")
sleep(2)
print("3. Hay tres niveles de dificultad: fácil, intermedio y difícil.")
sleep(2)
print("   - En fácil tendrás tres pistas que te dirán si algún color está en la combinación aunque no esté en la posición correcta.")
sleep(2)
print("   - En intermedio solo te dirá si acertaste el color y la posición; si no, seguirá en blanco.")
sleep(2)
print("   - En difícil no te dirá ninguna pista, solo cuando aciertes todo.")
sleep(2)
print("Espero que estés listo para poner a prueba tus habilidades de deducción.")
sleep(2)

def Modo_Juego(modo_de_juego):
    if modo_de_juego == "1":
        nivel = input("Escribe 1 para jugar fácil, 2 para nivel intermedio y 3 para difícil: ")
        if nivel == "1":
            juego = JuegoMastermind(jugador1)
        elif nivel == "2":
            juego = JuegoMastermindI(jugador1)
        else:
            juego = JuegoMastermindD(jugador1)
        
        print(f"Jugador: {jugador1}")
        sleep(2)
        print("Colores disponibles: ", juego.colores_disponibles)
        sleep(2)
        print("Intenta adivinar la combinación de 4 colores. Ejemplo de entrada: rojo, azul, verde, amarillo:")
        sleep(2)
        intentos = 0
        max_intentos = 12
        while intentos < max_intentos:
            conjetura = input("Ingresa tu conjetura separando los colores por comas: ").strip().lower().split(",")
            intentos += 1
            resultado = juego.verificar_conjetura(conjetura)
            print("Resultado: ", resultado)
            if resultado and all(item == "🟢" for item in resultado) and len(resultado) == 4:
                print(f"¡Felicidades {jugador1}! Adivinaste la combinación en {intentos} intentos.")
                sleep(2)
                break
        else:
            print(f"Lo siento {jugador1}, has agotado tus {max_intentos} intentos. Mejor suerte la próxima vez.")
            sleep(2)
        
        print("Combinación secreta de la máquina (solo para prueba): ", juego.combinacion_secreta)
        sleep(2)
    
    else:
        nivel2 = input("Elige nivel de la computadora: 1 para que sea aleatoria y 2 para que lo haga de manera consciente e inteligente: ")
        if nivel2 == "1":
            juego = JuegoMastermindCompu(jugador1)
            print("Colores disponibles: 'rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado'")
            combinacion_usuario = input("Ingrese la combinación secreta de 4 colores separados por comas (ej. rojo, verde, azul, amarillo): ").split(',')
            combinacion_usuario = [color.strip() for color in combinacion_usuario]
            if juego.establecer_combinacion_secreta(combinacion_usuario):
                juego.adivinar_combinacion()
            else:
                print("Error al establecer la combinación secreta.")
        else:
            juego = JuegoMastermindCompuIA(jugador1)
            print("Colores disponibles: 'rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado'")
            combinacion_usuario = input("Ingrese la combinación secreta de 4 colores separados por comas (ej. rojo, verde, azul, amarillo): ").split(',')
            combinacion_usuario = [color.strip() for color in combinacion_usuario]
            if juego.establecer_combinacion_secreta(combinacion_usuario):
                juego.adivinar_combinacion()
            else:
                print("Error al establecer la combinación secreta.")

print("Elige si quieres adivinar el código o crear el código")
modo_de_juego = input("Escribe 1 si quieres adivinar, 2 si quieres crear el código: ")
Modo_Juego(modo_de_juego)
