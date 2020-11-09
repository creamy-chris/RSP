import random
from random import randint
import time
import json

def print_choices():
    #Player is chosing a character.
    for x in thisdict:
        print(thisdict[x], "(", x, ")", end =" ")        
#set number of rounds
def main():
    with open("games.json") as f:
        games = json.load(f)
    all_known_games = 0
    for gg in games["dictionary"]:        
        for item in gg.values():
                print("-", item, end="")
        all_known_games += 1
        print("(", all_known_games, ")\n")
    input_choosen = input("what game would you like to play?\n")
    if input_choosen.isnumeric() != True:
        game_choosen = 1
    else: game_choosen = int(input_choosen)
    if game_choosen > all_known_games:
        game_choosen = all_known_games
    elif game_choosen == 0:
        return
    print(game_choosen)
if __name__ == "__main__":
    main()