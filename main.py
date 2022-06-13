"""
Name(s): William Zhou, Benson Zhang
Name of Project: Super Idol Turn Based Fighting Game
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
import os
import time
import sys

os.system('clear')

# Character Classes
class AmongUs:
  def __init__(self):
    self.name = "AMONG US"
    self.hp = 69
    self.moves = [["Self Report (LV.1 Attack)",1],["Vent (LV.2 Attack)",2],["Kill (LV.3 Attack)",3],["Eject (LV.4 Attack)",4],["LV.1 Counter",5],["LV.2 Counter",6], ["LV.3 Counter",7],["LV.4 Counter",8]]
    
class Elsa:
  def __init__(self):
    self.name = "ELSA FROM FROZEN"
    self.hp = 69
    self.moves = [["Freeze (LV.1 Attack)",1],["Ice Spikes (LV.2 Attack)",2],["Throw Anna (LV.3 Attack)",3],["LET IT GO LET IT GO CANT HOLD IT BACK ANYMORE LET IT GO LET IT GO TURN AWAY AND SLAM THE DOOR (LV.4 Attack)",4],["LV.1 Counter",5],["LV.2 Counter",6], ["LV.3 Counter",7],["LV.4 Counter",8]]
    
class Shrek:
  def __init__(self):
    self.name = "SHREK"
    self.hp = 69
    self.moves = [["Donkey (LV.1 Attack)",1],["Lord Farquaad (LV.2 Attack)",2],["Dragon (LV.3 Attack)",3],["GET OUT OF MY SWAMP (LV.4 Attack)",4],["LV.1 Counter",5],["LV.2 Counter",6], ["LV.3 Counter",7],["LV.4 Counter",8]]
    
class Mannix:
  def __init__(self):
    self.name = "MANNIX CHENG"
    self.hp = 69
    self.moves = [["hi (LV.1 Attack)",1],["please (LV.2 Attack)",2],["give (LV.3 Attack)",3],["A+ (LV.4 Attack)",4],["LV.1 Counter",5],["LV.2 Counter",6], ["LV.3 Counter",7],["LV.4 Counter",8]]


    
# Misc Functions
    
# Function for Delay Printing
def delayPrint(string):
  for l in string:
     sys.stdout.write(l)
     sys.stdout.flush()
     time.sleep(0.015)


    
# Game Functions
 
#Character Selection Display Function - Prints out Character Selection screen
def instructions():
  yes = input("(DO NOT SKIP IF FIRST TIME PLAYING)\nHi, would you like to view the instructions for this game?\n(input yes to view, input anything else to skip): ")
  if yes == "yes":
    delayPrint("\nThe goal of this game is to reduce the enemy's health to zero. \nEach character has four attacks and four counters levels 1,2,3, and 4. \nEach counter can reflect an attack of its respective level. \nHowever, it cannot reflect any other attacks. \nAn attack deals damage equal to ten times its level. \nIn each round, both players choose a move, and then the damage is calculated. \nIn the event that both players defend, nothing happens. \nRounds are repeated until one player's health reaches zero.\n")
    input("Input anything to continue: ")
  time.sleep(1)
  os.system('clear')

#Character Selection Display Function - Prints out Character Selection screen
def characterSelection(playerChar):
  while playerChar not in ['1','2','3','4']:
    print("That's not a valid character number!")
    playerChar = input("Player choose character(1,2,3, or 4): ")
  playerChar = int(playerChar)-1
  if playerChar == 0:
    playerChar = AmongUs()
  elif playerChar == 1:
    playerChar = Elsa()
  elif playerChar == 2:
    playerChar = Shrek()
  else:
    playerChar = Mannix()
  return playerChar

def chooseMove(move):
  while move not in ['1','2','3','4','5','6','7','8']:
    print("That's not a valid move number!")
    move = input("Choose a move(1,2,3,4,5,6,7,or 8): ")
  move = int(move)-1
  return move
    
def turn(player):
  global player1
  global player2
  if player == 0:
    current = player1
    enemy = player2
  else:
    current = player2
    enemy = player1
  delayPrint(f"It is player {player+1}'s turn. They are: {current.name}.\nYou have {current.hp} hp left.\nThe enemy {enemy.name} has {enemy.hp} hp left.\nYou can do 8 moves:\n1. {current.moves[0][0]}\n2. {current.moves[1][0]}\n3. {current.moves[2][0]}\n4. {current.moves[3][0]}\n5. {current.moves[4][0]}\n6. {current.moves[5][0]}\n7. {current.moves[6][0]}\n8. {current.moves[7][0]}\n")
  moveselectioninitial = input("Choose a move(1,2,3,4,5,6,7,or 8): ")
  moveselectionfinal = chooseMove(moveselectioninitial)
  time.sleep(0.5)
  os.system('clear')
  return current.moves[moveselectionfinal][1]

def mathCalcuations(move1, move2):
  if (move1 - move2) == 4:
    damage = move2 * 10
    player2.hp -= damage
    delayPrint(f"Player 1 has countered Player 2's attack. Player 2 recieves {damage} damage.")
  elif (move2 - move1) == 4:
    damage = move1 * 10
    player1.hp -= damage
    delayPrint(f"Player 2 has countered Player 1's attack. Player 1 receives {damage} damage.")
  elif (move1>4) and (move2>4):
    delayPrint("Both players defended, and nothing happened.")
  elif (move1<5) and (move2<5):
    player1.hp -= move2*10
    player2.hp -= move1*10
    delayPrint(f"Both players attacked! Player 1 recieved {move2*10} damage, and Player 2 recieved {move1*10} damage.")
  else:
    if move1<5:
      player2.hp -= move1*10
      delayPrint(f"Player 2 defended incorrectly, and took {move1*10} damage.")
    else:
      player1.hp -= move2*10
      delayPrint(f"Player 1's defended incorrectly, and took {move2*10} damage.")
  time.sleep(2)
  os.system('clear')
  
def selectionScreen():
  for i in range(10):
    print("Loading" + "." * i)
    sys.stdout.write("\033[F")
    time.sleep(0.25)
  os.system('clear')
  delayPrint("Character options:\n1. among us\n2. elsa from frozen\n3. shrek\n4. mannix cheng\n")
  time.sleep(0.5)
  player1char = input("Player 1 choose character(1,2,3, or 4): ")
  Player1 = characterSelection(player1char)
  player2char = input("Player 2 choose character(1,2,3, or 4): ")
  Player2 = characterSelection(player2char)
  delayPrint(f'Player 1 has selected: {Player1.name}. Player 2 has selected: {Player2.name}.\n')
  delayPrint(f'The Execution Begins!\n')
  time.sleep(0.5)
  print("*confetti*\r")
  time.sleep(1)
  os.system('clear')

  delayPrint("Welcome to the Colosseum. Defeat the other person!\n")
  time.sleep(1)
  os.system('clear')
  return [Player1,Player2]
  
  
  
  

# Execution:
instructions()
players = selectionScreen()
player1 = players[0]
player2 = players[1]
while (player1.hp > 0) and (player2.hp > 0):
  player1move = turn(0)
  player2move = turn(1)
  mathCalcuations(player1move,player2move)
if player1.hp > 0:
  delayPrint("Player 1 wins!\n")
  if player1.name == "MANNIX CHENG":
    delayPrint("Hi you won as MANNIX CHENG, Mr. Cheng please give us an A+\n")
elif player2.hp >0:
  delayPrint("Player 2 wins!\n")  
  if player2.name == "MANNIX CHENG":
    delayPrint("Hi you won as MANNIX CHENG, Mr. Cheng please give us an A+\n")
else:
  delayPrint("It's a draw!\n")
time.sleep(5)
os.system('clear')
delayPrint("Game Over\n")