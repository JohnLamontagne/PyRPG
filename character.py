from random import randint

class Character:
  def __init__(self, name):
    self.name = name
    self.alive = True
    self.health = 100
    self.damage = 10
    print("Your character has been created with name " + self.name)

  def die(self):
    if self.alive:
      self.alive = False
      print("Oh dear, you are dead!")
    else:
      print("You can only die once")

  def inflict_damage(self, damage_amount):
    self.health -= damage_amount  

    print(self.name + " has " + str(self.health) + " health left.")

    if self.health <= 0:
      self.Die()

  def attack(self, target_monster):
    damage_delt = randint(0, self.damage)
    print(self.name + " attacks " + target_monster.name + " for " + str(damage_delt) + " damage!")
    target_monster.inflict_damage(damage_delt)
