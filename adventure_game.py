import time
import random
items = []
monster = ["Dragon", "Gargoyle", "Troll"]
monster = random.choice(monster)


def print_pause(text):
    print(text)
    time.sleep(3)


def valid_input(prompt):
    while True:
        answer = input(prompt + "\n")
        if answer == '1':
            break
        elif answer == '2':
            break
        else:
            print_pause("Sorry I don't understand you.")
            valid_input(prompt)
    return answer


def intro(monster):
    print_pause("You find yourself in a large feild,"
                "filled with grass and yellow flowers.")
    print_pause(f"Rumor has it that a wicked {monster} is around here,")
    print("and has been teriffying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (lv.1) dagger.")


def feild():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to walk into the cave.")
    while True:
        answer = input("What would you like to do? Enter 1 or 2.")
        if answer == '1':
            house(monster)
        elif answer == '2':
            cave(items)
        else:
            print_pause("Sorry, that's no answer.")
            feild()
        break


def cave(items):
    if "sword" in items:
        print_pause("You walk back into the cave, but it is empty.")

    else:
        print_pause("You walk cautiously into the cave.")
        print_pause("It turns out to be a really small cave.")
        print_pause("A glint of metal behind a rock catches your eye.")
        print_pause("You found the (lv.100) Magical Sword of Fiyera!")
        print_pause("You lay down your trusty dagger and pick up the sword.")
        items.append("sword")
    print_pause("You walk back out into the feild.")
    feild()


def fight(items, monster):
    if "sword" in items:
        print_pause(f"The {monster} moves to attack!")
        print_pause("You unsheath your new sword.")
        print_pause("The Sword of Fiyera glowes bright in your hand.")
        print_pause("You brace for the attack.")
        print_pause(f"The {monster} dives at you.")
        print_pause("You roll to the left,")
        print("and harshly drive your sword to the right.")
        print_pause(f"You land your blow! The {monster} lay defeated!")
        print_pause(f"You rid the village of the {monster}!")
        print_pause("You are victorious!")

    else:
        print_pause("You try your hardest...")
        print_pause(f"But you dagger was no match for the {monster}.")
        print_pause("You were defeated.")
    play_again()


def play_again():
    while True:
        answer = input("Would you like to play again? y/n").lower()
        if answer == 'y':
            play_game(items, monster)
        elif answer == 'n':
            print_pause("Okay, Goodbye!")
        else:
            print_pause("Sorry, I don't understand.")
            play_again()
        break


def house(monster):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock...")
    print_pause(f"When the door swings open and the {monster} appears!")
    print_pause(f"AHH! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    while True:
        answer = input("What would you like to do? (1) Run. (2) Fight!")
        if answer == '1':
            feild()
        elif answer == '2':
            fight(items, monster)
        else:
            print_pause("Sorry, I don't understand.")
            house(monster)
        break


def play_game(items, monster):
    items = []
    monster = ["Dragon", "Gargoyle", "Troll"]
    monster = random.choice(monster)
    intro(monster)
    feild()


play_game(items, monster)
