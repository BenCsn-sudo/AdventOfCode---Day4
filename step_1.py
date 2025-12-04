with open('input.txt', 'r', encoding='utf-8') as fichier:
    data = fichier.read()

# On fait une liste de liste pour représenter chaque ligne de la grille
grid = [[i for i in line] for line in data.split('\n')]

# On supprime le dernier élément de la liste qui est égale à 0
grid.pop(-1)

res = 0

def voisins(grid, p):
    compteur = 0
    x0, y0 = p
    # On détermine les voisins des 8 cellules adjacentes à p
    for x1, y1 in [(x0 - 1, y0 - 1), (x0, y0 - 1), (x0 + 1, y0 + -1), (x0 - 1, y0), 
                   (x0 + 1, y0), (x0 - 1, y0 + 1), (x0, y0 +1), (x0 + 1, y0 + 1)]:
        
        # On vérifie que les coordonnées sont dans la grille
        if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
            # Si c'est une cellule avec un rouleau on incrémente
            if grid[x1][y1] == '@':
                compteur += 1

    return compteur

for i in range(len(grid)):
    for n in range(len(grid[0])):
        if grid[i][n] == '@':
            if voisins(grid, (i, n)) < 4:
                res += 1

print("La réponse est: ", res)