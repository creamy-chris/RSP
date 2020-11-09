import random
from random import randint
import time
import json


def print_choices(thisdict):
    for x in thisdict:
        print(thisdict[x], "(", x, ")", end=" ")


def get_game_library(games):
    all_known_games = 0
    for gg in games["dictionary"]:
        for item in gg.values():
            print("-", item, end="")
        all_known_games += 1
        print(" (", all_known_games, ")\n")
    if all_known_games == 0:
        return
    if all_known_games > 1:
        input_choosen = input("what game would you like to play?\n")
        if input_choosen.isnumeric() != True:
            game_choosen = 1
        else:
            game_choosen = int(input_choosen)
    else:
        game_choosen = 1
    if game_choosen > all_known_games:
        game_choosen = all_known_games
    return game_choosen


def main():
    with open("games.json") as f:
        games = json.load(f)
    game_choosen = get_game_library(games)
    if game_choosen == 0:
        return
    thisdict = games["dictionary"][game_choosen - 1]
    rules = games["rules"][game_choosen - 1]

    print('Welcome to my game of', end=" ")
    for x in thisdict:
        print("-", thisdict[x], end="")
    print('!!!')
    time.sleep(1)
    #set number of rounds
    player_request = input('Best out of ...? (1 to 10)')
    if player_request.isnumeric():
        rounds = int(player_request)
    else:
        rounds = 3
    if rounds > 10:
        rounds = 10
    if rounds == 0:
        return
    print('Let us play', rounds, 'rounds')

    #main Game Loop
    player_score = 0
    cpu_score = 0
    keep_going = 0
    while keep_going < rounds:
        is_in = False
        while is_in == False:
            #Player is chosing a character.
            print_choices(thisdict)
            playerC = input()
            playerC = playerC.lower()
            is_in = playerC in thisdict
        player = thisdict[playerC]
        print(player, 'vs', end=' ')

        #Computer is chosing an item.
        computer = random.choice(list(thisdict.values()))
        print(computer)

        # Compare the two and define the winner
        fight = player + ' ' + computer
        if computer == player:
            print(player, 'likes', computer, "-it's a draw!!!")
        elif fight in rules:
            print(rules[fight], ", you win!")
            player_score += 1
        else:
            fight = computer + ' ' + player
            if fight in rules:
                print(rules[fight], ", you loose!")
                cpu_score += 1
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