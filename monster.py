from character import Character
from random import randint

class Monster:
  def __init__(self, name, level, damage, health):
    self.name = name
    self.level = level
    self.damage = damage
    self.health = health
    self.alive = True

  def attack(self, target_character: Character):
    damage_delt = randint(0, self.damage)
    print(self.name + " attacks " + target_character.name + " for " + str(damage_delt) + " damage!")
    target_character.inflict_damage(damage_delt)

  def die(self):
    if self.alive:
      self.alive = False
      print("Oh no i've died")
    else:
      print("You can only die once")

  def inflict_damage(self, damage_amount):
    self.health -= damage_amount

    print(self.name + " has " + str(self.health) + " left.")

    if self.health <= 0:
      self.die()
