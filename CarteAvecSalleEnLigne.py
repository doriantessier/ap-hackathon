import numpy as np
import random as rd

def generate_map(width, height):
    # Création d'une grille vide
    grid = [[' ' for _ in range(height)] for _ in range(width)]
    
    def draw_room(x, y, w, h):
        for i in range(w):
            for j in range(h):
                if i == 0 or i == w - 1:
                    grid[x + i][y + j] = '|'
                elif j == 0 or j == h - 1:
                    grid[x + i][y + j] = '-'
                else:
                    grid[x + i][y + j] = '.'
    
    # Dessiner plusieurs salles
    xsalle = 1
    nbrsalle = rd.randint(4, 9)
    print(nbrsalle)
    Lx = []
    Llg = []
    Lh = []
    
    for i in range(nbrsalle):
        largeur = rd.randint(6, 12)
        hauteur = rd.randint(4, 9)
        xsalle += largeur + 3 + rd.randint(3, 6)
        Lx.append(xsalle)
        Llg.append(largeur)
        Lh.append(hauteur)
        draw_room(xsalle, 1, largeur, hauteur)

    
    # Créer un passage entre les salles
    for j in range(nbrsalle - 1):
        minh = min(Lh[j], Lh[j + 1])
        h = rd.randint(2, minh - 1)
        for i in range(Lx[j], Lx[j + 1]):
            if grid[i][h] == ' ':
                grid[i][h] = '#'
            if j != nbrsalle - 1:
                grid[Lx[j] + Llg[j] - 1][h] = '='
                grid[Lx[j + 1]][h] = '='


    dico = {}
    dico['coin']=[]
    dico['arme']=[]
    dico['potion']=[]
    dico['bouclier']=[]
    for i in range(width):
        for j in range(height):
            if grid[i][j] == '.':
                prob = rd.random()
                if prob < 0.10 :
                    
                    p = rd.random()

                    if p < 0.5:
                        grid[i][j] = 'c'
                        dico['coin'].append([i,j])
                    elif 0.5 < p < 0.75 :
                        grid[i][j] = 'p'
                        dico['potion'].append([i,j])
                    elif 0.75 < p < 0.9 :
                        grid[i][j] = 'a'
                        dico['arme'].append([i,j])
                    else : 
                        grid[i][j] = 'b'
                        dico['bouclier'].append([i,j])

    return grid, nbrsalle, dico, Lx




def print_map(grid):
    for y in range(len(grid[0])):
        print("".join(grid[x][y] for x in range(len(grid))))

if __name__ == "__main__":
    width, height = 150, 20  # Taille de la carte
    dungeon_map, nbrsalle, Lx, dico = generate_map(width, height)
    print_map(dungeon_map)
