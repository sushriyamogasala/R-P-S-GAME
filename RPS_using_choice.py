import random

turns = ["Rock","Paper","Scissors"]

player1 = random.choice(turns)

player2 = False

while player2 == False:

    player2 = input("What is your choice Rock,Paper,Scissors ?")

    if player2 == player1:
        print("Wooo...It's a TIE!!!🤝")

    elif player2 == "Rock" :
        if player1 =="Scissors":
            print("You won 🥳 !!!", player2 ,"smashes",player1)
        else:
            print("OOPS you lost 🥲 !!", player1,"covers",player2)

    elif player2 == "Paper":
        if player1 == "Rock":
            print("You won 🥳 !!!", player2 ,"covers",player1)
        else:
            print("OOPS...you lost 🥲 !!", player1,"cuts",player2)
    
    elif player2 == "Scissors":
        if player1 == "Paper":
             print("You won 🥳 !!!", player2 ,"cuts",player1)
        else:
            print("OOPS...you lost 🥲 !!", player1,"smashes",player2)
    
    else :
        print("😤 😤 😤 Check your spelling you moron.... 😒 🤬 😒!!!!!")

    player2 = False

    player1 = random.choice(turns)