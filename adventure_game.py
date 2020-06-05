import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt)
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_pause("Please enter 1 or 2.")
    return response


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger\n")


def first_door():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a dragon.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon attacks you!")
    print_pause("You feel a bit under-prepared for this,"
                " what with only having a tiny dagger.")
    response = valid_input("Would you like to (1)"
                           " fight or (2) run away?\n", "1", "2")
    if '1' in response:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        print_pause("You have been defeated!")
        play_again()
    elif '2' in response:
        print_pause("You run back into the field. Luckily,"
                    " you don't seem to have been followed.")
        adventure()


def second_door():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger "
                "and take the sword with you.")
    print_pause("You walk back out to the field.")
    adventure()


def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", 'y', 'n')
    random.choice(response)
    if 'y' == response:
        print_pause("Excellent! Restarting the game ...")
        adventure()
    elif 'n' == response:
        print_pause("Thanks for playing! See you next time.")


def adventure():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. ")
    print_pause("What would you like to do?")
    door = valid_input("(Please enter 1 or 2.)\n", '1', '2')
    if door == '1':
        first_door()
    elif door == '2':
        second_door()


def play_game():
    intro()
    adventure()


play_game()
