import copy

# Lecture du fichier
with open('input.txt', 'r', encoding='utf-8') as fichier:
    data = fichier.read()

# Création de la grille (attention aux lignes vides à la fin du fichier)
grid = [[i for i in line] for line in data.split('\n') if line]

def voisins(grid, p):
    """
    Renvoie le nombre de voisins @ autour d'une coordonnée p (x, y)
    x = ligne, y = colonne
    """
    compteur = 0
    x0, y0 = p
    # Liste des 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for dx, dy in directions:
        x1, y1 = x0 + dx, y0 + dy
        
        if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]):
            if grid[x1][y1] == '@':
                compteur += 1

    return compteur

def step_grid(grid):
    """
    Supprime les rouleaux et renvoie le nombre de suppressions effectuées
    """
    a_supprimer = [] # Liste pour stocker les coordonnées
    
    for i in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[i][n] == '@':
                vois = voisins(grid, (i, n))
                if vois < 4:
                    a_supprimer.append((i, n))
    
    # On applique les suppressions APRES avoir tout vérifié
    for i, n in a_supprimer:
        grid[i][n] = '.'
        
    return len(a_supprimer) # On retourne combien on en a enlevé

total_removed = 0

while True:
    removed_now = step_grid(grid)
    if removed_now == 0:
        # Si on n'a rien enlevé ce tour-ci, on a fini
        break
    total_removed += removed_now


print("La réponse est :", total_removed)