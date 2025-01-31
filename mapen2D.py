import numpy as np
import random as rd
width, height = 40, 40
def place(L,x,y): 
    a,b = 0,0
    ia = x
    ib = y
    while ia <= len(L)-2:
        if L[ia][y] == ' ':
            a+=1
            ia+=1
        else:
            break
    while ib <= len(L[x])-2:
        if L[x][ib] == ' ':
            b+=1
            ib+=1
        else:
            break
    return a,b

def generate_map(width, height):
    # Création d'une grille vide
    grid = [[' ' for _ in range(height)] for _ in range(width)]
    
    def draw_room(x, y, w, h):
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1:
                    grid[x + j][y + i] = '|'
                elif j == 0 or j == w - 1:
                    grid[x + j][y + i] = '-'
                else:
                    grid[x + j][y + i] = '.'
        print('----  ', grid[x][y], x, ' ', y, ' ', w, ' ', h)

    xsalle = 1
    i = 0
    nbrsalle = rd.randint(3,6)
    Lx = []
    Ly = []
    longueurX = []
    hauteurY = []
    Y = []
    X = []
    while i<nbrsalle or len(Y) == height or len(X) == width:
        y,x =  rd.randint(0,height-4),rd.randint(0,width-4)
        if grid[x][y] == ' ' and y not in Y and x not in X:
            i+=1
            for j in range(12):
                X.append(x+j)
                Y.append(y+j)
            a,b = place(grid,x,y)
            c,d = min(rd.randint(5,10),a-1), min(rd.randint(5,10),b-1)
            Lx.append(x)
            longueurX.append(c)
            Ly.append(y)
            hauteurY.append(d)
            draw_room(x,y,c,d)
            
            print(i)
        
    
    
    # Créer un passage entre les salles
    #for i in range(10, 12):
     #   grid[5][i] = '#'
    
    return grid, nbrsalle
def liaison(Lx, Ly, hauteurY, longueurX,grid):
    def chemin(grid,x1,x2,y1,y2):

        if x1>x2:
            x2 = x1 
        for i in range(x1,x2):
            grid[i][y1] = '#'
        for i in range(y1,y2):
            grid[x2][i] = '#'
    y_sorted, x_sorted, Lx_sorted, Ly_sorted = zip(*sorted(zip(Ly, Lx, longueurX, long)))
    LX = list(x_sorted)
    for i in range(len(LY)-1):
        dy_i = LY[i] + hauteurY[i] - LY[i+1]
        if LX[i]>LX[i+1]:
            x_i = LX[i] 
            y_i = LY[i] + rd.randint(1,3)
            x_j = LX[i+1] + rd.randint(1,3)
            y_j = LY[i+1]
            chemin(grid,x_i,x_j,y_i,y_j)
        else : 
            x_i = LX[i]
            y_i = LY[i] + rd.randint(1,3)
            x_j = LX[i+1] + rd.randint(1,3)
            y_j = LY[i+1]




def print_map(grid):
    for row in grid:
        print("".join(row))

#if _name_ == "main":
  # Taille de la carte
dungeon_map , nbrsalle = generate_map(width, height)
print_map(dungeon_map)
print(nbrsalle)