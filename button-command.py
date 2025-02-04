import pyxel
import numpy as np

def button_pressed(state, hero):
    if pyxel.btnp(pyxel.KEY_UP):
        if greed(hero.position[0],hero.position[1]-1) == ' ' or greed(hero.position[0],hero.position[1]-1) == '|' or greed(hero.position[0],hero.position[1]-1) == '-':
            pass
        else :
            hero.position[1] -= 1
            
    if pyxel.btnp(pyxel.KEY_DOWN):
        if greed(hero.position[0],hero.position[1]+1) == ' ' or greed(hero.position[0],hero.position[1]+1) == '|' or greed(hero.position[0],hero.position[1]+1) == '-':
            pass
        else :
            hero.position[1] += 1
    
    if pyxel.btnp(pyxel.KEY_LEFT):
        if greed(hero.position[0]-1,hero.position[1]) == ' ' or greed(hero.position[0]-1,hero.position[1]) == '|' or greed(hero.position[0]-1,hero.position[1]) == '-':
            pass
        else :
            hero.position[0] -= 1

    if pyxel.btnp(pyxel.KEY_RIGHT):
        if greed(hero.position[0]+1,hero.position[1]) == ' ' or greed(hero.position[0]+1,hero.position[1]) == '|' or greed(hero.position[0]+1,hero.position[1]) == '-':
            pass
        else :
            hero.position[0] += 1
    

    w = 0
    if pyxel.btnp(pyxel.KEY_W):
        if len(weapons) > 1:
            w += 1
            hero.weapon = weapons[w%len(weapons)]
            print(f"You've selected {hero.weapon} as your weapon.")
        else:
            print("You don't have enough weapon.")
    
    
    if pyxel.btnp(pyxel.KEY_E): 
        if hero.food > 0:
            hero.food -= 1
            hero.health += 1
            print("You've eaten some food! You've gained 1 health point.")
        else:
            print("You don't have enough food.")


    
    if pyxel.btnp(pyxel.KEY_I):
        print(f"Your health is {hero.health}.")
        print(f"You have {hero.food} food.")
        print(f"Your current weapon is {hero.weapon}.")
        print(f'Your weapons are {weapons}.')
        print(f"Your potion is {hero.potion}.")
        print(f"Your gold is {hero.gold}.")
    
    
    
    if pyxel.btnp(pyxel.KEY_P):
        if hero.potion > 0:
            hero.potion -= 1
            hero.health += 5
            print("You've used a potion! You've gained 10 health points.")
        else:
            print("You don't have enough potion.")

    if pyxel.btnp(pyxel.KEY_Q):
        state=State.MENU

def insert_name(state, name):
        for key in range(pyxel.KEY_A, pyxel.KEY_Z + 1):
            if pyxel.btnp(key):
                name += chr(key)
        if pyxel.btnp(pyxel.KEY_DELETE):
            name=name[:-1]
        if pyxel.btnp(pyxel.KEY_SPACE):
            state=State.PLAY
        if pyxel.btnp(pyxel.KEY_ENTER):
            state=State.HIGHSCORES


def leaving_hs(state):
        if pyxel.btnp(pyxel.KEY_DELETE):
            state=State.MENU



def encounter(hero):
    
    if hero.position in food_location:
        hero.food += 1
        hero.score += 2
        food_location.remove(hero.position)
        print("You've found some food! You can use it by pressing 'e'.")
    
    if hero.position in weapon_location:
        weapons.append("sword")
        if hero.weapon == None:
            hero.weapon = "sword"
        hero.score += 5
        weapon_location.remove(hero.position)
        print("You've found a sword! You can now attack monsters.")
    
    if hero.position in shield_location:
        hero.shield = "wooden shield"
        hero.health += 10
        hero.score += 5
        shield_location.remove(hero.position)
        print("You've found a wooden shield! You can now protect yourself from monsters.")
    
    
    if hero.position in potion_location:
        hero.potion += 1
        potion_location.remove(hero.position)
        hero.score += 5
        print("You've found a potion! You can now heal yourself.")    
   
    if hero.position in gold_location:
        gold = np.random.randint(20,50)
        hero.gold += gold
        hero.score += gold
        gold_location.remove(hero.position)
        print(f"You've found {gold} gold!")


    if hero.health == 0:
        print("You died! Game over.")
       
    
    if hero.position == [i_monster,j_monster] and hero.weapon == "sword":
        print("You've killed the monster!")
        hero.position = [i_monster_out,j_monster_out]
        hero.score += 50
    
    if hero.position == [i_monster,j_monster] and hero.weapon != "sword":
        print("You've been attacked by a monster! You lost 1 health point.")
        hero.health -= 1
    
    if hero.position == [i_monster_out,j_monster_out]:
        hero.position = [i_monster,j_monster]
       