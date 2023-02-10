import random

options = ["Rock", "Paper", "Scissors"]
i= True
player_score = 0
bot_score = 0
leaderboard = 0

while i == True:
    bot = random.choice(options)
    player = str(input("Choose a option(Rock, Paper, Scissors): "))
    player_i= player.lower()
    player_ii= player_i.capitalize()
    if player_ii in options:

        print(f"\nYou choosed {player_ii}")
        print(f"The bot choosed: {bot}")

        if player_ii == bot:
            print("Oh its a draw!")

        elif player_ii == "Rock" and bot == options[2]:
            print("Oh you won!")
            player_score += 1

        elif player_ii == "Rock" and bot == options[1]:
            print("Oh you lost!")
            bot_score += 1

        elif player_ii == "Paper" and bot == options[2]:
            print("Oh you lost!")
            bot_score += 1

        elif player_ii == "Paper" and bot == options[0]:
            print("Oh you won!")
            player_score += 1

        elif player_ii == "Scissors" and bot == options[1]:
            print("Oh you won!")
            player_score += 1

        elif player_ii == "Scissors" and bot == options[0]:
            print("Oh you lost!")
            bot_score += 1


        print(f"\nplayer score: {player_score}")
        print(f"bot score: {bot_score}")
        question = input("\nDo u wanna keep playing?(y/n)\n")

        if question == "y" or question == "yes":
            i= True
        else:
            i= False

    else:
        print("\nMake you choosed a available option.\n")
        i= True




