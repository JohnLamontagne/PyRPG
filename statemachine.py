from random import randint
import gameworld

class State:
  def __init__(self):
    assert 0, "State init() not implemented!"

  def enter(self):
    assert 0, "State enter() not implemented!"

  def update(self):
    assert 0, "State update() not implemented!"

class WanderState(State):
  def __init__(self):
    return

  def enter(self):
    return 0

  def update(self):
    print("You wander through time and space...")

    if randint(0, 2) == 2:
      battle_state = BattleState()
      battle_state.enter()
      return battle_state

class BattleState(State):
  def __init__(self):
    return

  def enter(self):
    self.monster_key = list(gameworld.monsters)[randint(0, len(gameworld.monsters) - 1)]
    print("You encounter a " + gameworld.monsters[self.monster_key].name + "!")

  def update(self):
    gameworld.monsters[self.monster_key].attack(gameworld.our_character)

    print('What shall you do?')
    resp = input()

    if 'fight' in resp:
      gameworld.our_character.attack(gameworld.monsters[self.monster_key])
      return self
    elif 'cast' in resp:
      spell_name = ''.join(resp.split('cast', 1)[1:]).strip()
      
      if spell_name in gameworld.spells:
        gameworld.spells[spell_name].cast(gameworld.our_character, gameworld.monsters[self.monster_key])
      else:
        print('You mumble something yet nothing happens...')

      return self

    elif 'flee' in resp:
      return None
    else:
      print('You are clearly incoherent and fail to respond.')
      return self
      

class StateMachine:
  def __init__(self, init_state):
    self.current_state = init_state

  def start(self):
    self.current_state.enter()

  def update(self):
    self.current_state = self.current_state.update()
