from monster import Monster
from character import Character
import spell

monsters = {}

spells = {}

our_character = None

def init_monsters():
  monsters['minotaur'] = Monster("Minotaur", 5, 10, 100)
  monsters['goblin'] = Monster("Goblin", 2, 5, 100)
  monsters['mean fucking fairy'] = Monster("Mean Hairy Fairy", 5, 10, 100)

def init_spells():
  spells['ignis'] = spell.Fireball("ignis")



def init():
  global monsters
  global our_character

  init_monsters()
  init_spells()

  print("What is your characters name? ")
  characters_name = input()
  our_character = Character(characters_name)
  
  
