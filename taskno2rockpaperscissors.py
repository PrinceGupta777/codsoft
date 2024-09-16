import random

options=("rock", "paper", "scissor")
player=None
computer = random.choice(options)

while player not in options :
    player= input("Enter a choice( rock, paper, scissor ): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player==computer:
    print("it is Tie")
elif player== "rock" and computer=="paper":
    print("YOU LOST")
elif player=="paper"  and computer=="rock":
    print("YOU WIN")
elif player== "rock"   and computer=="scissor":
    print("YOU WIN")
elif player== "scissor" and computer=="rock":
    print("YOU LOST")
elif player== "scissor" and computer=="paper":
    print("YOU WIN")
elif player== "paper"  and computer=="scissor":
    print("YOU LOST")
