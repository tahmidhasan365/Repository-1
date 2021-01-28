#A short program: Rock, paper, scissors

import random, sys

print("Rock, Paper, Scissors")

#These variables keep track of the number of wins, losses, and draws.
wins = 0
losses = 0
draws = 0

#The main game loop
while True:
   print("%s Wins, %s Losses, %s Drawn"%(wins,losses,draws))
   while True: #The player input loop
      print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
      playerMove = input()
      if playerMove == "q":
          sys.exit() #Quit the program.
      if playerMove == "r" or playerMove == "p" or playerMove == "s":
          break #Break out of the player input loop.
      print("Type one of r, p, s, or q.")

   #Display what the player chose:
   if playerMove == "r":
       print("Rock versus...")
   elif playerMove == "p":
       print("Paper versus...")
   elif playerMove == "s":
       print("Scissors versus...")

    #Display what the computer chose:
   randomNumber = random.randint(1,3)
   if randomNumber == 1:
       computerMove = "r"
       print("Rock")
   elif randomNumber == 2:
       computerMove = "p"
       print("Paper")
   elif randomNumber == 3:
       computerMove = "s"
       print("Scissors")

   #Display and record the win/loss/draw:
   if playerMove == computerMove:
       print("It's a tie")
       draws = draws + 1
   elif playerMove == "r" and computerMove == "s":
       print("You win!")
       wins = wins + 1
   elif playerMove == "p" and computerMove == "r":
       print("You win!")
       wins = wins + 1
   elif playerMove == "s" and computerMove == "p":
       print("You win!")
       wins = wins + 1
   elif playerMove == "r" and computerMove == "p":
       print("You lose.")
       losses = losses + 1
   elif playerMove == "p" and computerMove == "s":
       print("You lose.")
       losses = losses + 1
   elif playerMove == "s" and computerMove == "r":
       print("You lose.")
       losses = losses + 1