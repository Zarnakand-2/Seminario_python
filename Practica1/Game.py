import random
# Lista de palabras posibles

def option_menu ():
    print ("---- Existen 3 niveles de dificultad: ----")
    print ("")
    print ("Ingrese 1 si desea jugar en dificultad facil, se le mostraran todas las vocales de la palabra secreta.")
    print ("")
    print ("Ingrese 2 si desea jugar en dificultad media, se le mostraran la primer y ultima letra de la palabra secreta.")
    print ("")
    print ("Ingrese 3 si desea jugar en dificultad dificil, no se le mostrara ninguna letra de la palabra secreta.")
    print ("")
    option = int (input ("Opcion: "))
    if (option != 1 and option != 2 and option != 3):
        print ("")
        print ("---- Se ingreso una opcion inexistente,por favor ingrese una opcion valida. ----")
        print ("")
        option_menu ()
    return option

words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
# max_attempts = 10
max_fails = 5
fails = 0
# Lista para almacenar las letras adivinadas
# guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Opcion 1- facil, 2-media, 3-dificil
letters = []
opt = option_menu()
if opt == 1:
    guessed_letters = ["a", "e", "i", "o", "u"]
    print('------ Se selcciono la dificultad Facil ------')
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print()
    print ("---- Se agregaron las letras vocales que correspondan. ----")
    print()
elif opt == 2:
    guessed_letters = [secret_word[0], secret_word[-1]]
    print('------ Se selcciono la dificultad Media ------')
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print()
    print ("---- Se agrego la primer y ultima letra de la palabra secreta. ----")
    print()
else:
    guessed_letters = []
    word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

# for i in range(max_attempts):
while fails < max_fails:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     # guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter != "":
        guessed_letters.append(letter)
        if letter in secret_word:
             print("¡Bien hecho! La letra está en la palabra.")
        else:
             print("Lo siento, la letra no está en la palabra.")
             fails += 1
     else:
         print ("No se ingreso nada, por favor ingrese un caracter valido.")
         continue
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     # print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
     print(f"¡Oh no! Has agotado tus {max_fails} fallos posibles.")
     print(f"La palabra secreta era: {secret_word}")