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
        