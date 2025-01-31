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
    if pyxel.btnp(pyxel.KEY_P):
        pass  #open bag to use a potion
    
    if pyxel.btnp(pyxel.KEY_Q):
        pass #quit the game


def encounter(hero):
    if hero.position in fruit_location:
        hero.food += 1
        fruit_location.remove(hero.position)
        print("You've found some food! You can use it by pressing 'e'.")
    if hero.position in weapon_location:
        hero.weapon = "sword"
        weapon_location.remove(hero.position)
        print("You've found a sword! You can now attack monsters.")
    if hero.position in shield_location:
        hero.shield = "wooden shield"
        hero.health += 10
        shield_location.remove(hero.position)
        print("You've found a wooden shield! You can now protect yourself from monsters.")
    if hero.position in potion_location:
        hero.potion += 1
        potion_location.remove(hero.position)
        print("You've found a potion! You can now heal yourself.")    
    if hero.position in gold_location:
        gold = np.random.randint(20,50)
        hero.gold += gold
        gold_location.remove(hero.position)
        print(f"You've found {gold} gold!")


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
    
   