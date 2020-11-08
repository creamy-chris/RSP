import random
from random import randint
import time

thisdict = {  
  "r":"Rock",
  "p":"Paper",
  "s":"Scissors"
}
rules_loose = {
    "Scissors Rock": "Rock blunts Scissors, you loose",
    "Paper Scissors": "Scissors cuts Paper, you loose",        
    "Rock Paper": "Paper covers Rock, you loose"
}
rules_win = {
    "Rock Scissors": "Rock blunts Scissors, you win",
    "Scissors Paper": "Scissors cuts Paper, you win",
    "Paper Rock": "Paper covers Rock, you win"
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
      print(thisdict[x], end =" ")
    print ('!!!')
    time.sleep (1)
    rounds = int(input ('Best out of ...? (1 to 10)'))
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
        elif fight in rules_loose:
            print(rules_loose[fight])
            cpu_score += 1
        elif fight in rules_win:
            print(rules_win[fight])
            player_score += 1
        #Count the winners
        print (player_score, 'vs', cpu_score)
        keep_going += 1
    if keep_going == rounds:
        if cpu_score > player_score:
            print ('You lose... :(')
        elif cpu_score == player_score:
            print ("It's a DRAW!!!")
        else :
            print ('You win...:)')
        break

if __name__ == "__main__":
    main()