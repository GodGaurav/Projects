import random 

#Building a simple rock paper scissors game where we take input from the user and decide who wins 

def game(player1):
    computerplayer = random.choices(["Rock", "Paper", "Scissors"], k=1)
    print(computerplayer)
    for a in computerplayer:
        if player1 == computerplayer :
            print("Draw")
        elif player1 == "Rock" and a == "Paper":
            print(" The computer wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        elif player1 == "Rock" and a == "Scissors":
            print(" The User wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        elif player1 == "Paper" and a == "Rock":
            print(" The User wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        elif player1 == "Paper" and a == "Scissors":
            print(" The computer wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        elif player1 == "Scissors" and a == "Rock":
            print(" The computer wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        elif player1 == "Scissors" and a == "Paper":
            print(" The User wins! Congratulations. The computer picked {} and the user picked {}".format(computerplayer, player1))
        else:
            print("No outcome! which is very unusual!!")


game1 = game(input("Rock,paper or scissors?"))
