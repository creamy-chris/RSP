from random import randint
import time

#set number of rounds

print ('Welcome to my game of Rock, Paper, Scissors!!!')
time.sleep (1)
rounds = int(input ('Best out of ...? (1 to 10)'))
print ('Let us play', rounds, 'rounds')



#main Game Loop
player_score = 0
cpu_score =0
keep_going = 0
while keep_going < rounds:
    
    #Player is chosing a character.       
    playerC = input('Rock (r), Paper (p), Scissors (s)')
    if playerC == ('r'):
        player = ('Rock')
    elif playerC == ('s'):
        player = ('Scissors')
    elif playerC == ('p'):
        player = ('Paper')
    else:
        player = ("That's not a choice")
    print (player, 'vs', end= ' ')

    #Computer is chosing a character.

    c_choice = randint (1,3)
    if c_choice == (1):
        computer = ('Rock')
    elif c_choice == (2):
        computer = ('Paper')
    elif c_choice == (3):
        computer = ('Scissors')
    print (computer)

    # Compare the two and define the winner
    
    if computer == player:
        print (player, 'likes', computer, "-it's a draw!!!")
    elif computer == ('Rock') and player == ('Scissors'):
        print (computer, 'blunts', player, ', you loose.')
        cpu_score += 1
    elif computer == ('Scissors') and player == ('Paper'):
        print (computer, 'cuts', player, ', you loose.')
        cpu_score += 1
    elif computer == ('Paper') and player == ('Rock'):
        print (computer, 'covers', player, ', you loose.')
        cpu_score += 1
    elif player == ('Rock') and computer == ('Scissors'):
        print (player, 'blunts', computer, ', you win.')
        player_score += 1
    elif player == ('Scissors') and computer == ('Paper'):
        print (player, 'cuts', computer, ', you win.')
        player_score += 1
    elif player == ('Paper') and computer == ('Rock'):
        print (player, 'covers', computer, ', you win.')
        player_score += 1
    #Count the winners
    print (player_score, 'vs', cpu_score)
    keep_going += 1
while keep_going == rounds:
    if cpu_score > player_score:
        print ('You lose... :(')
    elif cpu_score == player_score:
        print ("It's a DRAW!!!")
    else :
        print ('You win...:)')
    break



