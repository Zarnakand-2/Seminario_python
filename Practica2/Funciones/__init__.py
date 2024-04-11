# 1. Generar una estructura todas las estadísticas asociadas a cada jugador o jugadora.

def inciso_a():
    names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia, 
    Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
    goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
    goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
    assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]
    nombres = names.split()
    jugadores = {}
    for i in range(len(nombres)):
        anidados = {"goles": goals[i], "goles evitados": goals_avoided[i], "asistencias": assists[i]}
        jugadores[nombres[i]] = anidados
    return jugadores

 # 2. Conocer el nombre y la cantidad de goles del goleador o goleadora.

def inciso_b(jugadores):
    max_goles = -1
    goleador = ""
    for jugador, datos in jugadores.items():
        if (datos["goles"] > max_goles):
            max_goles = datos["goles"]
            goleador = jugador
    return goleador, max_goles