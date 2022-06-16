class Practice:
    pass


import time
import random

print("Welcome to the rock, paper, scissors game,", end=" ")
print("to play you have to choose one:")
print("a = rock\nb = paper\nc = scissors")
h = ["a", "b", "c"]
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
while True:
    player1 = str(input("Player one, chose your fighter "))
    player2 = str(random.choice(h))
    player1_l = list(player1)
    if player1_l == ['a'] or player1_l == ['b'] or player1_l == ['c']:
        time.sleep(0.5)
        print()
        print("Your choice was confirmed!")
        break
    else:
        print("wrong input")
        continue
print()
time.sleep(0.5)
print("wait...")
time.sleep(1)
print()

if (player1 == 'a' and player2 == 'c') or (player1 == 'c' and player2 == 'b') or (player1 == 'b' and player2 == 'a'):
    print("Congratulations! You won!")
elif player1 == player2:
    print("It's a draw!")
else:
    print('You lost! :((')

if player2 == 'a':
    print('Computer choose rock')
elif player2 == 'b':
    print('Computer choose paper')
elif player2 == 'c':
    print('Computer choose scissors')

exit()
