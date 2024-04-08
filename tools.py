def create_dictionary (names, goals, goals_avoided, assists):
    """Este modulo recibe cuatro listas y las agrupa en un diccionario con el nombre de clave y de valor una tupla con sus estadisticas"""
    dictionary={}
    for n,g,g_a,a in zip(names,goals,goals_avoided,assists):
        dictionary[n]=(g,g_a,a)
    return dictionary

def get_topScorer (dictionary):
    """Esta funcion recibe un diccionario con las estadisticas de los jugadores y retorna los datos del mayor goleador"""
    max_goals=-1
    max_name=None
    max_ga=None
    max_a=None
    for name, (g,g_a,a) in dictionary.items():
        if max_goals < g:
            max_goals=g
            max_name=name
            max_ga=g_a
            max_a=a
    
    return max_name,max_goals,max_ga,max_a


def get_mostInfluentialPlayer(dictionary):
    """Esta funcion recibe un diccionario con las estadisticas de los jugadores y retorna en base a unos puntajes el jugador mas influyente"""
    points_goals= 1.5
    points_goalsAvoided= 1.25
    points_assists=1
    max=-1
    aux=None
    for name, (g,g_a,a) in dictionary.items():
        aux=(g*points_goals)+(g_a*points_goalsAvoided)+(a*points_assists)
        if max<aux:
            max=aux
            most_player=name
    return most_player

def get_teamAverageGoalsPerGame (dictionary):
    """Recibe un diccionario con las estadisticas de los jugadores y retorna el promedio de gol del equipo"""
    total_goals=0
    for name,(g,g_a,a) in dictionary.items():
        total_goals+=g
    return(total_goals/25)

def get_topScorerAveregeGoalsPerGame (goals):
    """Esta funcion recibe una cantidad de goles y retorna el promedio de goles en la temporada"""
    return goals/25
