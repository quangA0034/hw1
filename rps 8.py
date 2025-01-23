import random

options = ['Rock','Paper','Scissor']
def user_choice():
    user_input = input('Select your option Rock/Paper/Scissor: ')
    if user_input in options:
        return user_input
    print('Invalid choice do again')

def computer_choice():
    return random.choice(options)

def main_game():
    user_score = 0
    com_score = 0
    while user_score < 3 and com_score <3:
        u_choice = user_choice()
        c_choice = computer_choice()
        print(u_choice)
        print('Computer chose', c_choice)
        if u_choice == c_choice:
            user_score += 0
            com_score += 0
            print('Its a tie')
            print(f"current score User:{user_score} Computer:{com_score}")
        elif u_choice == "Rock" and c_choice == "Scissor" or \
            (u_choice == "Paper" and c_choice == "Rock") or \
            (u_choice == "Scissor" and c_choice == "Paper"):
            print("u won this round")
            user_score += 1
            print(f"current score User:{user_score} Computer:{com_score}")
        else:
            print('u lost this round')
            com_score += 1
            print(f"current score User:{user_score} Computer:{com_score}")
    if user_score == 3:
        print(f"U won with {user_score} against {com_score}")
    else:
        print(f"U lost with {user_score} to {com_score}")

main_game()