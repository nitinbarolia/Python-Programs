import  random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You Win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer,"cut", player)
            cpu_score+=1
        else:
            print("You Win!", player,"covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose :P", computer, "smashes", player)
            cpu_score+=1
        else:
            print("Final Scores:")
            print(f"CPU:{cpu_score}")
            print(f"PLAYER:{player_score}")
            break