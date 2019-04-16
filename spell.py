from random import randint

class Spell:
  def __init__(self, incantation):
    self.incantation = incantation
    assert 0, "Spell init() not implemented"

  def cast(self, caster, target):
    assert 0, "Spell cast() not implemented"

class Fireball(Spell):
  def __init__(self, incantation):
    self.incantation = incantation

  def cast(self, caster, target):
    damage = randint(1, caster.damage * 2)
    print("The fireball roars across the battlefield, dealing {} damage!".format(damage))
    target.inflict_damage(damage)
