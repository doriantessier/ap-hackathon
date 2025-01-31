import pyxel
import numpy as np

def button_pressed(hero):
    if pyxel.btnp(pyxel.KEY_UP):
        hero.position[1] -= 1
    if pyxel.btnp(pyxel.KEY_DOWN):
        hero.position[1] += 1
    if pyxel.btnp(pyxel.KEY_LEFT):
        hero.position[0] -= 1
    if pyxel.btnp(pyxel.KEY_RIGHT):
        hero.position[0] += 1
    
    if pyxel.btnp(pyxel.KEY_W):
        pass  #open bag to use a new weapon
    if pyxel.btnp(pyxel.KEY_E): 
        pass  #open bag to eat
    if pyxel.btnp(pyxel.KEY_D):
        pass  #open bag to drop an item
    if pyxel.btnp(pyxel.KEY_I):
        pass  #open bag to see inventory
    if pyxel.btnp(pyxel.KEY_T):
        pass  #open bag to throw an item


def encounter(hero):
    if hero.position == [i_fruit,j_fruit]:
        hero.health += 1
        print("You've eaten a fruit! You gained 1 health point.")
    if hero.position == [i_weapon,j_weapon]:
        hero.weapon = "sword"
        print("You've found a sword! You can now attack monsters.")
    if hero.position == [i_shield,j_shield]:
        hero.shield = "wooden shield"
        print("You've found a wooden shield! You can now protect yourself from monsters.")
    if hero.position == [i_potion,j_potion]:
        hero.potion += 1
        print("You've found a potion! You can now heal yourself.")    
    
    if hero.health == 0:
        print("You died! Game over.")
       
    
    if hero.position == [i_monster,j_monster] and hero.weapon == "sword":
        print("You've killed the monster!")
        hero.position = [i_monster_out,j_monster_out]
    if hero.position == [i_monster,j_monster] and hero.weapon != "sword":
        print("You've been attacked by a monster! You lost 1 health point.")
        hero.health -= 1
    
    if hero.position == [i_monster_out,j_monster_out]:
        hero.position = [i_monster,j_monster]
    
   