#RPS.py
#Name: Emma Zechmann
#Date: 2/8/2026
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  play_Again = "yes"
  
  while play_Again == "yes" :
      bot = random.choice (["rock","paper","sissors"])
      user =input("Type rock, paper or sissors: ").lower()

      if user == bot : 
        print("We Tied Good Game!")
        ties+=1

      elif (user == "rock" and bot== "paper") or (user == "sissors" and bot=="rock") or  (user== "paper"and bot=="sissors"):
        print("You Lose!") 
        losses+=1

      else:
        print("Congrats You Win!")
        wins+=1

        print("Bot chose", bot)
        play_Again= input("Do You Want To Play Again? Yes Or No?: ").lower()
        print(f"Wins:{wins},Ties:{ties}, losses:{losses}")

     #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  

if __name__ == '__main__':
  main()
