import numpy as np
import random as rd
def generate_map(width, height):
    # Création d'une grille vide
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    def draw_room(x, y, w, h):
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1:
                    grid[y + i][x + j] = '-'
                elif j == 0 or j == w - 1:
                    grid[y + i][x + j] = '|'
                else:
                    grid[y + i][x + j] = '.'
    
    # Dessiner deux salles
    xsalle = 1
    nbrsalle = rd.randint(4,9)
    print(nbrsalle)
    L=[]
    for i in range(nbrsalle):
                
                   hauteur = rd.randint(6,12)
                   largeur = rd.randint(4,9)
                   xsalle += largeur + 3 + rd.randint(3,6)
                   Lx.append(xsalle)
                   draw_room(xsalle, 1, largeur, hauteur)

    
    
    # Créer un passage entre les salles
    #for i in range(len(L)-1):
    #    for j in range(L[i+1][1]-L[i][1]):
    #         grid[5][L[i][1]+ L[i][2] + j] = '#'

    for i in range(L[0], L[-1]):
        if grid[5][i] == ' ':
            grid[5][i] = '#'
    
    return grid, nbrsalle, L

def print_map(grid):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    width, height = 140, 20  # Taille de la carte
    dungeon_map , nbrsalle, L= generate_map(width, height)
    print_map(dungeon_map)
    print(nbrsalle, L)


