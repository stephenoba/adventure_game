import random
import time
import sys


def print_pause(message, seconds=2.0):
    print(message)
    time.sleep(float(seconds))


def valid_input(user_input, valid_inputs, input_message):
    if user_input not in valid_inputs:
        valid_input(input(input_message), valid_inputs, input_message)
    return user_input


def intro(monster, item, arsenal):
    print_pause('You find yourself standing in an open field, filled with grass and yellow wildflowers.')
    print_pause(f'Rumor has it that a {monster} is somewhere around here, and has been terrifying the nearby village.')
    print_pause('In front of you is a house.')
    print_pause('To your right is a dark cave.')
    print_pause('In your hand you hold your trusty (but not very effective) dagger.')
    field(monster, item, arsenal)


def fight(monster, arsenal):
    victory = False
    if arsenal:
        victory = True
    game_over(monster, victory)


def cave(monster, item, arsenal):
    item_acquired = False
    if item in arsenal:
        item_acquired = True
    print_pause('You peer cautiously into the cave.')
    if not item_acquired:
        print_pause('It turns out to be only a very small cave.')
        print_pause('Your eye catches a glint of metal behind a rock.')
        print_pause(f'You have found {item}!')
        print_pause('You discard your silly old dagger and take the sword with you.')
        arsenal.append(item)
    else:
        print_pause("you've been here before, and gotten all the good stuff. It's just an empty cave now.")
    print_pause('You walk back out to the field.')
    field(monster, item, arsenal)


def field(monster, item, arsenal):
    print_pause('Enter 1 to knock on the door of the house.  ', 1)
    print_pause('Enter 2 to peer into the cave.', 1)
    print_pause('What would you like to do?', 1)
    user_choice = valid_input(input('(Please enter 1 or 2).\n'), ['1', '2'], '(Please enter 1 or 2).\n')[0]
    if user_choice == '1':
        house(monster, item, arsenal)
    else:
        cave(monster, item, arsenal)


def house(monster, item, arsenal):
    print_pause('You approach the door of the house.')
    print_pause(f'You are about to knock when the door opens and out steps a {monster}.')
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f'The {monster} attacks you!')
    if not arsenal:
        print_pause('You feel a bit under - prepared for this, what with only having a tiny dagger.')
    user_choice = valid_input(
        input('Would you like to (1) fight or (2) run away?'),
        ['1', '2'],
        'Would you like to (1) fight or (2) run away?'
    )
    if user_choice == '1':
        fight(monster, arsenal)
    else:
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        field(monster, item, arsenal)


def game_over(monster, victory=False):
    if not victory:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {monster}.")
        print_pause("You have been defeated!")
    else:
        print_pause(f'As the {monster} moves to attack, you reveal your weapon.')
        print_pause(f'But the {monster} takes one look at your shiny new toy and runs away!')
        print_pause(f'You have rid the town of the {monster}. You are victorious!')
    user_choice = valid_input(
        input('Would you like to play again? (y/n)'),
        ["y", "n"],
        'Would you like to play again? (y/n)'
    )
    if user_choice == 'y':
        print_pause('Excellent! Restarting the game ...')
        main()
    else:
        print_pause('Thanks for playing! See you next time.')
        sys.exit()


def main():
    monsters = ["gorgon", 'dragon', 'wicked ferrie']
    items = ['Thors Hammer', 'the magical Sword of Ogoroth']
    arsenal = []
    monster = random.choice(monsters)
    item = random.choice(items)
    intro(monster, item, arsenal)


if __name__ == '__main__':
    main()
