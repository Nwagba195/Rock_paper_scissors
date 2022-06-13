import random

moves = ["r", "p", "s"]


keep_playing = "true"


while keep_playing == "true":

    cmove = random.choice(moves)
  
    pmove = input("choose an option: 'R' for rock, 'P' for paper or 'S' for scissors?")
 
    print ("The computer chose",cmove)
   
    if cmove == pmove:
        print ("Tie")
   
    elif pmove == "r" and cmove == "s":
        print ("Player wins")
    elif pmove == "r" and cmove == "p":
        print ("Computer wins")
    elif pmove == "p" and cmove == "r":
        print ("Player wins")
    elif pmove == "p" and cmove == "s":
        print ("Computer wins")
    elif pmove == "s" and cmove == "p":
        print ("Player wins")
    elif pmove == "s" and cmove == "r":
        print ("Computer wins")
