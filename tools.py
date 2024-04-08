def create_dictionary (names, goals, goals_avoided, assists):
    """Este modulo recibe cuatro listas y las agrupa en un diccionario con el nombre de clave y de valor una tupla con sus estadisticas"""
    dictionary={}
    for n,g,g_a,a in zip(names,goals,goals_avoided,assists):
        dictionary[n]=(g,g_a,a)
    return dictionary
    