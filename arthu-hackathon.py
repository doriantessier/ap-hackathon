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
    for i in range(nbrsalle):
                
                   hauteur = rd.randint(6,12)
                   largeur = rd.randint(4,9)
                   xsalle += rd.randint(2,5) + largeur + 2
                   draw_room(xsalle, 2, largeur, hauteur)

    
    
    # Créer un passage entre les salles
    #for i in range(10, 12):
     #   grid[5][i] = '#'
    
    return grid, nbrsalle

def print_map(grid):
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    width, height = 110, 20  # Taille de la carte
    dungeon_map , nbrsalle= generate_map(width, height)
    print_map(dungeon_map)
    print(nbrsalle)


