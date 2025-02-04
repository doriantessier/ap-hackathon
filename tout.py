import numpy as np
import random as rd
import pyxel
import enum
import typing
import yaml
import schema
import keyboard


from pathlib import Path


class State(enum.Enum):
    MENU= 1
    PLAY=2
    HIGHSCORES=3


SCORE_FILE_SCHEMA = schema.Schema([
    {"name":str,
     "score":int}
])

class Scores :
    """Contains instances of scores."""

    def __init__(self) :
        """Define the scores."""
        self._max_scores=5
        self._scores=sorted([Score (score=0, name="Dodo"), Score(score=0, name="Arthur"), Score(score=0,name="Lenny"), Score(score=0, name="Victor")], reverse = True)[:5]

    
    def __iter__(self):
        """Iterate on the list of scores."""
        return iter(self._scores)


    def is_highscore(self, score_player : int) -> bool :
        """Define the case highscore."""
        return len(self._scores)<self._max_scores or self._scores[-1].score < score_player

    def add_score(self, score_player) :
        """Add a score and sort the list."""
        if self.is_highscore(score_player.score):
            if len(self._scores)>=self._max_scores :
                self._scores.pop()
            self._scores.append(score_player)
            self._scores.sort(reverse=True)

    def saving_hs(self,hs_file:Path)->None:
        """Saves high score in the file."""
        high_scores=[{"name":s.name,"score":s.score} for s in self]
        with hs_file.open("w") as fd:
            yaml.safe_dump(high_scores,fd)
    
    @property 
    def print(self):
        for s in self._scores:
            print(f"name:{s.name}, score{s.score}")


    def loading_hs(self,scores_file:Path) -> None:
        """Loads high scores from the file."""
        with open(scores_file, "r") as f:
            hs = yaml.load(f, Loader=yaml.Loader)
        SCORE_FILE_SCHEMA.validate(hs)
        self._scores=[]
        for sc in hs:
            self._scores.append(Score(sc["score"],sc["name"]))
        self._scores=sorted(self._scores, reverse = True)[:self._max_scores]


class Score :



    MAX_LENGTH = 8

    def __init__(self, score : int, name : str) -> None:
        """Initialize."""
        self._score=score
        self.name=name #use the property 

    @property
    def name(self) -> str :
        """Return the name."""
        return self._name

    @name.setter
    def name(self, n : str) -> None :
        """Modify the name."""
        self._name=n[:self.MAX_LENGTH]



    @property 
    def score(self) -> int :
        """Return the score."""
        return self._score

    
    # Implemente the comparaison operators to use the function sort in the lists
    def __gt__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score > other._score

    def __lt__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score < other._score

    def __eq__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score == other._score

    def __ge__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score >= other._score

    def __le__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score <= other._score

    def __ne__(self, other : object) -> bool :
        """Define the comparaison operator."""
        return isinstance(other, Score) and self._score != other._score

    def __repr__(self) -> str:
        """Representation."""
        return f"Score(name={self._name}, score={self._score})"

def button_pressed(state, hero, greed):
    global weapons
    if keyboard.is_pressed("up"):
        if greed[hero.position[0]][hero.position[1]-1] == ' ' or greed[hero.position[0]][hero.position[1]-1] == '|' or greed[hero.position[0]][hero.position[1]-1] == '-':
            pass
        else :
            hero.position[1] -= 1
            
    if keyboard.is_pressed("down"):
        if greed[hero.position[0]][hero.position[1]+1] == ' ' or greed[hero.position[0]][hero.position[1]+1] == '|' or greed[hero.position[0]][hero.position[1]+1] == '-':
            pass
        else :
            hero.position[1] += 1
    
    if keyboard.is_pressed("left"):
        if greed[hero.position[0]-1][hero.position[1]] == ' ' or greed[hero.position[0]-1][hero.position[1]] == '|' or greed[hero.position[0]-1][hero.position[1]] == '-':
            pass
        else :
            hero.position[0] -= 1

    if keyboard.is_pressed("right"):
        if greed[hero.position[0]+1][hero.position[1]] == ' ' or greed[hero.position[0]+1][hero.position[1]] == '|' or greed[hero.position[0]+1][hero.position[1]] == '-':
            pass
        else :
            hero.position[0] += 1
    

    w = 0
    if keyboard.is_pressed("w"):
        if len(weapons) > 1:
            w += 1
            hero.weapon = weapons[w%len(weapons)]
            print(f"You've selected {hero.weapon} as your weapon.")
        else:
            print("You don't have enough weapon.")
    
    
    if keyboard.is_pressed("e"):
        if hero.food > 0:
            hero.food -= 1
            hero.health += 1
            print("You've eaten some food! You've gained 1 health point.")
        else:
            print("You don't have enough food.")


    
    if keyboard.is_pressed("i"):
        print(f"You have {hero.food} food.")
        print(f"You have {hero.potion} potion.")
        print(f"You have {hero.gold} gold.")
        print(f"Your weapon is {hero.weapon}.")
        print(f"Your health is {hero.health}.")
    
    
    
    if keyboard.is_pressed("p"):
        if hero.potion > 0:
            hero.potion -= 1
            hero.health += 5
            print("You've used a potion! You've gained 10 health points.")
        else:
            print("You don't have enough potion.")

    if keyboard.is_pressed("q"):
        state=State.MENU

def insert_name(state, name):

    for key in range(ord('A'), ord('Z') + 1):
        if keyboard.is_pressed(chr(key)):  
            name += chr(key)  

    if keyboard.is_pressed('delete'):
        name = name[:-1]

    if keyboard.is_pressed('space'):
        state = State.PLAY 

    if keyboard.is_pressed('enter'):
        state = State.HIGHSCORES  


def leaving_hs(state):
        if keyboard.is_pressed("delete"):
            state=State.MENU



def encounter(hero, dico):
   
    '''if hero.position in dico['food']:
        hero.food += 1
        hero.score += 2
        dico['food'].remove(hero.position)
        print("You've found some food! You can use it by pressing 'e'.")'''
    
    if hero.position in dico['weapons']:
        hero.weapon = "sword"
        hero.score += 5
        dico['weapons'].remove(hero.position)
        print("You've found a sword! You can now attack monsters.")
    
    if hero.position in dico['shield']:
        hero.shield = "wooden shield"
        hero.health += 10
        hero.score += 5
        dico['shield'].remove(hero.position)
        print("You've found a wooden shield! You can now protect yourself from monsters.")
    
    
    if hero.position in dico['potion']:
        hero.potion += 1
        dico['potion'].remove(hero.position)
        hero.score += 5
        print("You've found a potion! You can now heal yourself.")    
   
    if hero.position in dico['gold_nuggets']:
        gold = np.random.randint(20,50)
        hero.gold += gold
        hero.score += gold
        dico['gold_nuggets'].remove(hero.position)
        print(f"You've found {gold} gold!")


    if hero.health == 0:
        print("You died! Game over.")
       
    '''
    if hero.position == [i_monster,j_monster] and hero.weapon == "sword":
        print("You've killed the monster!")
        hero.position = [i_monster_out,j_monster_out]
        hero.score += 50
    
    if hero.position == [i_monster,j_monster] and hero.weapon != "sword":
        print("You've been attacked by a monster! You lost 1 health point.")
        hero.health -= 1
    
    if hero.position == [i_monster_out,j_monster_out]:
        hero.position = [i_monster,j_monster]'''

def rogue():
    stay=True
    state=State.PLAY
    scores=Scores()
    while stay:

        if state==State.MENU:
            s=Score(0,"")
            while state==State.MENU:
                if keyboard.read_event():
                    insert_name(state, s.name)
                    print(f"insert your name:{s.name}\n",
                          "press space to start the game \n",
                          "press enter to see highscores\n",
                            state, s)

        if state==State.PLAY:
            """save score ?"""
            s.score=Game(state)
            scores.add_score(s)
            scores.saving_hs("snake_scores.yml")
        
        if state==State.HIGHSCORES:
            scores.print()
            while state==State.HIGHSCORES:
                leaving_hs(state)

class Object:
    def __init__(self,s):
        self.symbole=s

    def print(self):
        print(self.symbole)


class Hero():
    def __init__(self):
        self.position=np.array([0,0])
        self.score = 0
        self.health = 10
        self.position = (0,0)
        self.weapon = None
        self.shield = None
        self.potion = 0
        self.gold = 0
        self.food = 0

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
    dico['gold_nuggets']=[]
    dico['weapons']=[]
    dico['potion']=[]
    dico['shield']=[]
    for i in range(width):
        for j in range(height):
            if grid[i][j] == '.':
                prob = rd.random()
                if prob < 0.10 :
                    p = rd.random()
                    if p < 0.5:
                        grid[i][j] = 'c'
                        dico['gold_nuggets'].append([i,j])
                    elif 0.5 < p < 0.75 :
                        grid[i][j] = 'p'
                        dico['potion'].append([i,j])
                    elif 0.75 < p < 0.9 :
                        grid[i][j] = 'a'
                        dico['weapons'].append([i,j])
                    else : 
                        grid[i][j] = 'b'
                        dico['shield'].append([i,j])

    return grid, nbrsalle, Lx, dico




def print_map(grid):
    for y in range(len(grid[0])):
        print("".join(grid[x][y] for x in range(len(grid))))



width, height = 140, 20  # Taille de la carte



def Game(state):
    hero = Hero()
    gameboard, nbrsalle, Lx, dico = generate_map(width, height)
    print(gameboard)
    while state == State.PLAY :
        if keyboard.read_event():
            button_pressed(state, hero, gameboard)
            encounter(hero, dico)
            print(gameboard)
            


rogue()


