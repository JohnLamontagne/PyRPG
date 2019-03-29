from random import randint

class Character:
  def __init__(self, name):
    self.name = name
    self.alive = True
    self.health = 100
    self.damage = 10
    print("Your character has been created with name " + self.name)

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

  def Attack(self, target_monster):
    damage_delt = randint(0, self.damage)
    print("Attacking " + target_monster.name + " for " + str(damage_delt) + " damage!")
    target_monster.InflictDamage(damage_delt)
