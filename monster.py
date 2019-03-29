from character import Character
from random import randint

class Monster:
  def __init__(self, name, level, damage, health):
    self.name = name
    self.level = level
    self.damage = damage
    self.health = health
    self.alive = True

  def Attack(self, target_character: Character):
    damage_delt = randint(0, self.damage)
    print("Attacking " + target_character.name + " for " + str(damage_delt) + " damage!")
    target_character.InflictDamage(damage_delt)

  def Die(self):
    if self.alive:
      self.alive = False
      print("Oh no i've died")
    else:
      print("You can only die once")

  def InflictDamage(self, damage_amount):
    self.health -= damage_amount

    print(self.name + " has " + str(self.health) + " left.")

    if self.health <= 0:
      self.Die()
