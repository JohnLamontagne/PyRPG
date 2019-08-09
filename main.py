from random import randint
import statemachine
import gameworld


stop_game = False


state_machine = None

def handle_suicide():
  gameworld.our_character.Die()

def handle_wander():
  state_machine.current_state = statemachine.WanderState()

def handle_attack():
  print("What monster do you want to attack? ")
  monster_to_attack = input()

  if monster_to_attack in monsters:
    gameworld.our_character.Attack(monsters[monster_to_attack])
  else:
    print("That monster does not exist!")

def handle_exit():
  global stop_game
  stop_game = True

def handle_help():
  available_commands = ", ".join(command_handlers)

  print("Available commands: " + available_commands)


command_handlers = {
  "suicide": handle_suicide,
  "wander": handle_wander,
  "attack": handle_attack,
  "help": handle_help
}

def GameLoop():
  global state_machine

  gameworld.init()

  state_machine = statemachine.StateMachine(None)
  
  while not stop_game:
    # ask the user what to do next if we there's no next state
    if state_machine.current_state is None:
      print("Enter action: ")
      user_input = input()

      if user_input in command_handlers:
        command_handlers[user_input]()
      else:
        print("Invalid command: " + user_input)
    else:
      state_machine.update()

def main():
  GameLoop()

main()
