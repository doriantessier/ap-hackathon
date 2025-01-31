import pyxel
import numpy as np

def Game(state):
    
    hero = Hero()
    

    gameboard = generate_map(widht, height)
    print(gameboard)
    while state == State.PLAY :
        if pyxel.btnp(pyxel.KEY_ANY):
            button_pressed(state, hero)
            encounter(hero)
            print(gameboard)
    
    

