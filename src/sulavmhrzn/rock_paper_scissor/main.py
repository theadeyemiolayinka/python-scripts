from enum import IntEnum
import random

class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2

print(f"{list(Choice._member_names_)}")


def computer_choices() : 
    return random.choice(list(Choice)).value


def user_choices() :
    user_value = str(input("Enter your choice: ").upper().strip().rstrip())
    return Choice[f"{user_value}"].value
    

def selection(user_choice:int  = int(user_choices()),computer_choice:int =int(computer_choices())) ->None  :
    while True: 
        if user_choice == computer_choice:
            print("Draw")
            break
        if user_choice > computer_choice:
            if user_choice == 2  and computer_choice == 0:
                print("You loose")
                break
            else: 
                print("you win")
                break    
        if user_choice < computer_choice:
            if user_choice == 0  and computer_choice == 2 :
                print("You win ")
                break
            else: 
                print("you loose")
                break    



if __name__ == "__main__":
    selection()
