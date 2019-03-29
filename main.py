from random import randint
from character import Character
from monster import Monster

our_character = None

monsters = {}

def GameLoop():

  global our_character
  
  while True:
    print("Enter action: ")
    user_input = input()

    if 'exit' in user_input:
      break
    elif 'suicide' in user_input:
      our_character.Die()
    elif 'attack' in user_input:
      print("What monster do you want to attack? ")
      monster_to_attack = input()

      if monster_to_attack in monsters:
        our_character.Attack(monsters[monster_to_attack])
      else:
        print("That monster does not exist!")
    elif 'wander':
      if randint(0, 2) == 2:
        print("You encounter a monster!")
        monsters['minotaur'].Attack(our_character)
      else:
        print("You wander down the road")

def main():
  global our_character
  global monsters

  print("What is your characters name? ")
  characters_name = input()
  our_character = Character(characters_name)
  
  monsters['minotaur'] = Monster("Minotaur", 5, 10, 100)

  GameLoop()

main()
