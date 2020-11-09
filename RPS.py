import random
from random import randint
import time
import json


# display options for current game
def print_choices(thisdict):
    for x in thisdict:
        print(thisdict[x], "(", x, ")", end=" ")


# get rules from config file
def get_game_library(games):
    all_known_games = 0
    for gg in games["dictionary"]:
        for item in gg.values():
            print("-", item, end="")
        all_known_games += 1
        print(" (", all_known_games, ")\n")
    if all_known_games == 0:
        return
    # make sure the message make sense
    if all_known_games > 1:
        input_choosen = input("what game would you like to play?\n")
        if input_choosen.isnumeric() != True:
            game_choosen = 1
        else:
            game_choosen = int(input_choosen)
    # the one and only choice
    else:
        game_choosen = 1
    # please return something plausible
    if game_choosen > all_known_games:
        game_choosen = all_known_games
    # return the index of game chosen
    return game_choosen


def main():
    # open the settings file and pass it to the function that loads the rules
    with open("games.json") as f:
        games = json.load(f)
    # player choice
    game_choosen = get_game_library(games)
    # maybe he doesn't wish to play?
    if game_choosen == 0:
        return
    # but if he does, we load the options
    thisdict = games["dictionary"][game_choosen - 1]
    # load the rules also
    rules = games["rules"][game_choosen - 1]
    # show that we understand what he chosen
    print('Welcome to my game of', end=" ")
    for x in thisdict:
        print("-", thisdict[x], end="")
    print('!!!')
    # pretend that the game is loading
    time.sleep(1)
    #set number of rounds
    player_request = input('Best out of ...? (1 to 10)')
    # make sure it is not something silly
    if player_request.isnumeric():
        rounds = int(player_request)
    else:
        rounds = 3
    # also that is not something too big
    if rounds > 10:
        rounds = 10
    # maybe he changed his mind
    if rounds == 0:
        return
    print('Let us play', rounds, 'rounds')

    # main Game Loop
    # keep track of the score
    player_score = 0
    cpu_score = 0
    keep_going = 0
    # count the rounds
    while keep_going < rounds:
        is_in = False
        # search the choice in allowed options
        while is_in == False:
            #Player is chosing a character.
            print_choices(thisdict)
            playerC = input()
            playerC = playerC.lower()
            is_in = playerC in thisdict
        player = thisdict[playerC]
        # current move is:
        print(player, 'vs', end=' ')
        #Computer is chosing an item.
        computer = random.choice(list(thisdict.values()))
        print(computer)

        # Compare the two and define the winner
        # first compose the rule
        fight = player + ' ' + computer
        # if choice is identical, then is a draw
        if computer == player:
            print(player, 'likes', computer, "-it's a draw!!!")
        # else check if this is defined as a win
        elif fight in rules:
            print(rules[fight], ", you win!")
            player_score += 1
        # but maybe this is defined as a lose
        else:
            fight = computer + ' ' + player
            if fight in rules:
                print(rules[fight], ", you loose!")
                cpu_score += 1
            # if we do not find the rule, declare a draw
            else:
                print(player, 'likes', computer, "-it's a draw!!!")
        #Count the winners
        print(player_score, 'vs', cpu_score)
        keep_going += 1

    if cpu_score > player_score:
        print('You lose... :(')
    elif cpu_score == player_score:
        print("It's a DRAW!!!")
    else:
        print('You win...:)')


if __name__ == "__main__":
    main()