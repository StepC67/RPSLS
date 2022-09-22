import random
results = ["rock","scissors)",("scissors", "paper"), ("paper", "rock")("rock", "lizard"), ("lizard", "spock"), ("spock", "scisscors"),("scissors","lizard"),("lizard","paper"),("paper","spock"),("spock","rock")]

moves = [results[1] for result in results]
player = input ("Enter rock / paper / scisscors / quit: ").lower()
while player != "quit":
    computer = random.choice(moves)
    print("You chose {}, I chose {}".format(player, computer))
    if player == computer:
        print("It's a tie!")
    elif (player, computer) in results:
        print("You win")
    player_score += 1
    elif (computer, player) in results:
        print ("I win")
        computer_score += 1
    else:
        print ("Invalid input")
    player = input("Enter rock / paper / scisscors / quit: ").lower()

    print("FINAL SCORES")
    print("You {}, Me {}".format(player_score, computer_score))  
