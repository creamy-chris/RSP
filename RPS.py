import random
from random import randint
import time

thisdict = {
  "r":"Rock",
  "p":"Paper",
  "s":"Scissors",
  "l": "Lizard",
  "k": "Spock"
}
rules = {
    "Spock Rock": "Spock vaporizes Rock",
    "Lizard Paper": "Lizard eats Paper",
    "Lizard Spock": "Lizard poisons Spock",
    "Paper Rock": "Paper covers Rock",
    "Paper Spock": "Paper disproves Spock",
    "Rock Lizard": "Rock crushes Lizard",
    "Rock Scissors": "Rock crushes Scissors",
    "Scissors Paper": "Scissors cut Paper",
    "Scissors Lizard": "Scissors decapitate Lizard",
    "Spock Scissors": "Spock smashes Scissors"
}

def print_choices():
    #Player is chosing a character.
    for x in thisdict:
        print(thisdict[x], end =" ")
        print("(", end =" ")
        print(x, end =" ")
        print("),", end =" ")
#set number of rounds
def main():
    print ('Welcome to my game of', end =" ")
    for x in thisdict:
      print(thisdict[x], end ="-")
    print ('!!!')
    time.sleep (1)
    player_request = input ('Best out of ...? (1 to 10)')
    if player_request.isnumeric():
        rounds = int(player_request)
    else:
        rounds = 3;
    if rounds > 10:
        rounds = 10
    if rounds == 0:
        return
    print ('Let us play', rounds, 'rounds')

    #main Game Loop
    player_score = 0
    cpu_score =0
    keep_going = 0
    while keep_going < rounds:
        is_in = False
        while is_in == False:
            print_choices()
            playerC = input()
            playerC = playerC.lower()
            is_in = playerC in thisdict
        player = thisdict[playerC]
        print (player, 'vs', end= ' ')

        #Computer is chosing an item.
        computer = random.choice(list(thisdict.values()))
        print (computer)

        # Compare the two and define the winner
        fight = player + ' ' + computer
        if computer == player:
            print (player, 'likes', computer, "-it's a draw!!!")
        elif fight in rules:
            print(rules[fight], ", you win!")
            player_score += 1
        else:
            fight = computer + ' ' + player
            if fight in rules:
                print(rules[fight], ", you loose!")
                cpu_score += 1
            else: print (player, 'likes', computer, "-it's a draw!!!")
        #Count the winners
        print (player_score, 'vs', cpu_score)
        keep_going += 1

    if cpu_score > player_score:
        print ('You lose... :(')
    elif cpu_score == player_score:
        print ("It's a DRAW!!!")
    else :
        print ('You win...:)')

if __name__ == "__main__":
    main()