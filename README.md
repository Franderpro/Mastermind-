Descripción General
Este proyecto implementa una versión digital del clásico juego de mesa Mastermind. En este juego, el jugador debe adivinar un código secreto de colores dentro de un número limitado de intentos. El proyecto incluye diferentes niveles de dificultad y modos, incluyendo un modo en el que la computadora intenta adivinar el código secreto del jugador.

Reglas del Juego
Colores: Hay seis colores diferentes disponibles: rojo, azul, verde, amarillo, naranja, morado.
Modos de Juego:
Modo de Adivinanza del Jugador: El jugador intenta adivinar el código secreto de colores generado por la computadora.
Modo de Adivinanza de la Computadora: La computadora intenta adivinar el código secreto de colores proporcionado por el jugador.
Niveles de Dificultad:
Fácil: Se proporcionan tres pistas que indican si algún color está en la combinación, aunque no esté en la posición correcta.
Intermedio: Solo se indica si el color y la posición son correctos; si no, la respuesta seguirá en blanco.
Difícil: No se proporcionan pistas, solo se informa cuando todos los colores y posiciones son correctos.
Intentos: Ambos modos tienen un límite de 12 intentos para adivinar el código correcto.
Cómo Jugar
Inicio del Juego:
El juego comienza pidiendo el nombre del jugador.
Se explican las reglas del juego.
Selección de Modo:
El jugador elige entre adivinar el código o crear un código para que la computadora lo adivine.
Adivinanza del Jugador:
El jugador selecciona el nivel de dificultad.
El jugador intenta adivinar la combinación de 4 colores ingresándolos separados por comas.
Después de cada intento, se proporciona un resultado que indica cuántos colores son correctos y están en la posición correcta (🟢), cuántos colores son correctos pero están en la posición incorrecta (🟠), y cuántos colores no están en la combinación (⚪).
Adivinanza de la Computadora:
El jugador elige el nivel de inteligencia de la computadora (aleatoria o inteligente).
El jugador ingresa una combinación secreta de 4 colores.
La computadora intenta adivinar la combinación secreta del jugador, proporcionando feedback en cada intento.